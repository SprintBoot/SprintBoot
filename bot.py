import discord
import os
from discord.ext import commands
from discord.utils import get
from discord.ext import tasks

import json
from module.sb import config
import nest_asyncio
import requests
from numba import njit

from module.sb.loops import Loop
from colorama import Fore, Style
from colorama import init 
import datetime
import asyncio
import random

from module.sb.paginator import Paginator as pr

PREFIX = config.PREFIX
COLOR_ERROR = config.COLOR_ERROR

client = commands.Bot( command_prefix =  PREFIX )
client.remove_command('help')
init()

@client.event
async def on_ready():
    print('''

░██████╗██████╗░  ██████╗░░░░░█████╗░
██╔════╝██╔══██╗  ╚════██╗░░░██╔══██╗
╚█████╗░██████╦╝  ░█████╔╝░░░██║░░██║
░╚═══██╗██╔══██╗  ░╚═══██╗░░░██║░░██║
██████╔╝██████╦╝  ██████╔╝██╗╚█████╔╝
╚═════╝░╚═════╝░  ╚═════╝░╚═╝░╚════╝░
    ''')
    print(Fore.CYAN + "===================================" + Style.RESET_ALL)
    print(
        Fore.CYAN + '|' + Style.RESET_ALL + f' Смена статуса на стандартный... ' + Fore.CYAN + '|' + Style.RESET_ALL)
    await client.change_presence( status = discord.Status.do_not_disturb, activity = discord.Game( 's*info / s*help' ) )
    print(
        Fore.CYAN + '|' + Style.RESET_ALL + f'        Бот активирован!         ' + Fore.CYAN + '|' + Style.RESET_ALL)
    print(Fore.CYAN + "===================================" + Style.RESET_ALL)
    print(f'  Имя бота - {client.user.name}')
    print(f'  ID бота  - {client.user.id}  ')
    print(Fore.CYAN + "===================================" + Style.RESET_ALL)
    print(" ")

    loop = Loop(client)
    try:
        loop.activator()
    except AssertionError:
        pass

@client.command()
async def load(ctx, extensions):
    if ctx.author.id == 529720195418423296:
        client.load_extension(f'cogs.{extensions}')
        await ctx.send(f'**Был загружен** {extensions}')
    else:
        await ctx.send(f'Вы не создатель {ctx.author}')

@client.command()
async def reload(ctx, extensions):
    if ctx.author.id == 529720195418423296:
        client.unload_extension(f'cogs.{extensions}')
        client.load_extension(f'cogs.{extensions}')
        await ctx.send(f'**Был перезапущен** {extensions}')
    else:
        await ctx.send(f'Вы не создатель {ctx.author}')

@client.command()
async def unload(ctx, extensions):
    if ctx.author.id == 529720195418423296:
        client.unload_extension(f'cogs.{extensions}')
        await ctx.send(f'**Был отключен** {extensions}')
    else:
        await ctx.send(f'Вы не создатель {ctx.author}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

@client.event
async def on_message(message):
    try:
        try:
            if isinstance(message.channel, discord.DMChannel):
                return
        except AttributeError:
            return
        await client.process_commands(message)
    except TypeError:
        return 

@njit
def f(n):
    s = 0.
    for i in range(n):
        s += sqrt(i)
    return s

@client.command(aliases = ['розыгрыш','giveaway','giawey','р-старт','конкурс'])
@commands.has_permissions(view_audit_log = True)
async def gstart(ctx, arg: str, prize: str, *, reason = None):
    now_date = datetime.datetime.now()
    channel = ctx.channel
   # giveaway = discord.utils.get(ctx.message.guild.roles, name = f'{prize}')
    amount = int(arg[:-1])
    tip = arg[-1]
    if tip == "s":  
        if reason is None:
            embed = discord.Embed(colour=discord.Color.red())
            embed.add_field(name = f'<:warning2:779398023095648276> Ошибка:', value = f'Вы не указали описание.')
            message = await channel.send(embed=embed)
        else:
            embed = discord.Embed(title= "**🎉Giveaway**", color = 0x00ff2a)

            embed.add_field(name = f'Приз:', value = f'{prize}')
            embed.add_field(name = f"Описание:", value = f"{reason}")
            # embed.add_field(name = f'победителей:', value = f'{winners}')
            embed.set_footer(text = f"Закончится через {amount} секунд")

            message = await channel.send(embed=embed)


            await message.add_reaction('🎉')


            await asyncio.sleep(amount)


            message = await ctx.channel.fetch_message(message.id)


            users = await message.reactions[0].users().flatten()
            users.pop(users.index(client.user))

            winner = random.choice(users)

            await channel.send(f"🎉Поздравляю! {winner.mention} выиграл {prize}")

    elif tip == "m":
        if reason is None:
            embed = discord.Embed(colour=discord.Color.red())
            embed.add_field(name = f'<:warning2:779398023095648276> Ошибка:', value = f'Вы не указали описание.')
            message = await channel.send(embed=embed)
        else:
            embed = discord.Embed(title= "**🎉Giveaway**", color = 0x00ff2a)

           # end = datetime.datetime.utcnow() + datetime.timedelta(seconds = min*60)

            embed.add_field(name = f'Приз:', value = f'{prize}')
            embed.add_field(name = f"Описание:", value = f"{reason}")
            # embed.add_field(name = f'победителей:', value = f'{winners}')
            embed.set_footer(text = f"Закончится через {amount} минут")

            message = await channel.send(embed=embed)


            await message.add_reaction('🎉')


            await asyncio.sleep(amount* 60)


            message = await ctx.channel.fetch_message(message.id)


            users = await message.reactions[0].users().flatten()
            users.pop(users.index(client.user))

            winner = random.choice(users)

            await channel.send(f"🎉Поздравляю! {winner.mention} выиграл {prize}")
    elif tip == "h":
        if reason is None:
            embed = discord.Embed(colour=discord.Color.red())
            embed.add_field(name = f'<:warning2:779398023095648276> Ошибка:', value = f'Вы не указали описание.')
            message = await channel.send(embed=embed)
        else:
            embed = discord.Embed(title= "**🎉Giveaway**", color = 0x00ff2a)

            embed.add_field(name = f'Приз:', value = f'{prize}')
            embed.add_field(name = f"Описание:", value = f"{reason}")
            # embed.add_field(name = f'победителей:', value = f'{winners}')
            embed.set_footer(text = f"Закончится через {amount} часов")

            message = await channel.send(embed=embed)


            await message.add_reaction('🎉')


            await asyncio.sleep(amount * 60 * 60)


            message = await ctx.channel.fetch_message(message.id)


            users = await message.reactions[0].users().flatten()
            users.pop(users.index(client.user))

            winner = random.choice(users)

            await channel.send(f"🎉Поздравляю! {winner.mention} выиграл {prize}")
    elif tip == "d":
        if reason is None:
            embed = discord.Embed(color = 0x00ff2a)
            embed.add_field(name = f'<:warning2:779398023095648276> Ошибка:', value = f'Вы не указали описание.')
            message = await channel.send(embed=embed)
        else:
            embed = discord.Embed(title= "**🎉Giveaway**", colour=discord.Color.red())

            embed.add_field(name = f'Приз:', value = f'{prize}')
            embed.add_field(name = f"Описание:", value = f"{reason}")
            # embed.add_field(name = f'победителей:', value = f'{winners}')
            embed.set_footer(text = f"Закончится через {amount} дней")

            message = await channel.send(embed=embed)


            await message.add_reaction('🎉')


            await asyncio.sleep(amount* 60 * 60 * 24)


            message = await ctx.channel.fetch_message(message.id)


            users = await message.reactions[0].users().flatten()
            users.pop(users.index(client.user))

            winner = random.choice(users)

            await channel.send(f"🎉Поздравляю! {winner.mention} выиграл {prize}")

@gstart.error
async def clear_error( ctx, error ):
    if isinstance( error, commands.errors.MissingRequiredArgument ):
        emb = discord.Embed(colour = discord.Color.red())
        emb.add_field( name = '<:warning2:779398023095648276> Ошибка:', value = 'Использование команды: `s*giveaway [Время  на анг] [Приз] [Описание приза]`' )
        await ctx.send( embed = emb, delete_after = 30 )
    
@client.command()
async def settings(ctx):
    embed1 = discord.Embed(title = 'Настройки сервера',
        description = 'Если вы не знаете как настроить ваш сервер и меня, то вам помогу. Нажмите на ➡ чтоб начать настройку')
    embed2 = discord.Embed(title = 'Жалобы',
        description = 'Настройте команду жалобы. Просто пропишите s*report-channel on/off #ваш канал')

    embeds = [embed1, embed2]
    message = await ctx.send(embed = embed1)
    page = pr(client, message, only = ctx.author, use_more = False, embeds = embeds)
    await page.start()

client.run('ТОКЕН')