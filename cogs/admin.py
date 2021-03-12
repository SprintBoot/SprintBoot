import discord
from discord.ext import commands
from discord.utils import get

import random

import asyncio
import os 
import datetime
from urllib.parse import urlparse
from discord import utils
import pip  
import io
import json
import time
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://SprintBoot:Avakum132@sprintboot.kghvy.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
collection = cluster.settings.settingreport


answer7 = ['Моя роль одинаковая с эти пользователем!','Роль у этого пользователя похоже на мою!']
answer6 = ['Роль бота ниже ,чем у  этого пользователя!', 'Роль этого пользователя выше моей!','Он выше меня и из-за этого я не могу это сделать!']
answer5 = ['Вы не можете выгнать пользователя с такой же ролью!', 'Ваши роли одинаковы, я не могу так сделать!', 'Вы не можете выгнать такого же модератора как и вы!']
answer4 = ['Это невозможно сделать, так как выгнать меня может только основатель сервера!', 'Это может сделать только основатель сервера', 'Так сделать невозможно!', 'Увы, меня нельзя так остранить...']
answer3 = ['У вас не хватает прав!', 'Его роль стоит выше вашей!', 'Это нельзя сделать!', 'Ваша роль менее значима, чем этого пользователя!']
answer2 = ['Ты быканул на основателя сервера, или мне показалось?', 'Что он такого плохого тебе сделал?', 'При всём уважении к тебе я так не могу сделать!', 'Ах если бы я так мог...', 'Я не буду этого делать!', 'Сорян, но не в моих это силах!']
answer = ['Самоубийство не приведёт ни к чему хорошему!', 'Напомню: суицид - не выход!', 'Увы, я не могу этого сделать!', 'Самоубийство - не выход!', 'Не надо к себе так относиться!', 'Я не сделаю этого!', 'Я не буду это делать!', 'Я не выполню это действие', 'Не заставляй меня это сделать!']

class administration(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.cog_name = ["администрация"]

    @commands.command(
        aliases=['очистить','удалить','cleanup','delete','clear'],
        description='очистить сообщение',
        usage='очистить <Колличество>'
        )
    @commands.has_permissions(manage_messages = True)
    @commands.cooldown(1, per = 3, type = discord.ext.commands.BucketType.guild )
    async def clean(self, ctx, amount : int):
        await ctx.message.delete()
        
        if amount > 0 and amount < 101:
            deleted = await ctx.channel.purge( limit = amount )
            emb = discord.Embed(colour=discord.Color.green())
            emb.add_field(name='<:ModClearMessages:779398022639386684> Очистка:', value = f'очищено сообщений: {len(deleted)}' )
            await ctx.send( embed = emb, delete_after = 30 )
        else:
            emb = discord.Embed(colour = discord.Color.red())
            emb.add_field( name = '<:warning2:779398023095648276> Ошибка:', value = 'Можно только очистить сообщения от 1 до 100!' )
            await ctx.send( embed = emb, delete_after = 30 ) 

    @clean.error
    async def clear_error( self, ctx, error ):
        if isinstance( error, commands.CommandOnCooldown):
            emb = discord.Embed(colour = discord.Color.red())
            emb.add_field( name = '<:warning2:779398023095648276> Ошибка:', value = 'Подождите 10 секунд перед повторным использованием!' )
            await ctx.send( embed = emb, delete_after = 10 ) 
        if isinstance( error, commands.BadArgument ):
            emb = discord.Embed(colour = discord.Color.red())
            emb.add_field( name = '<:warning2:779398023095648276> Ошибка:', value = 'Укажите число!' )
            await ctx.send( embed = emb, delete_after = 30 )
        if isinstance( error, commands.errors.MissingRequiredArgument ):
            emb = discord.Embed(colour = discord.Color.red())
            emb.add_field( name = '<:warning2:779398023095648276> Ошибка:', value = 'Использование команды: `s*clear [Кол-во сообщений]`' )
            await ctx.send( embed = emb, delete_after = 30 )
        if isinstance( error, commands.errors.MissingPermissions ):
            emb = discord.Embed(colour = discord.Color.red())
            emb.add_field( name = '<:warning2:779398023095648276> Ошибка:', value = 'У вас не хватает прав!' )
            await ctx.send( embed = emb, delete_after = 30 )
        if isinstance( error, commands.errors.CommandInvokeError ):
            emb = discord.Embed(colour = discord.Color.red())
            emb.add_field( name = '<:warning2:779398023095648276> Ошибка:', value = 'У бота не хватает прав!' )
            await ctx.send( embed = emb, delete_after = 30 )

    @commands.command(aliases=['кик'])
    @commands.has_permissions( kick_members = True )
    @commands.cooldown(1, per = 10, type = discord.ext.commands.BucketType.guild )
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await ctx.message.delete()

        if ctx.guild.me.top_role == member.top_role:
            emb = discord.Embed(colour=discord.Color.red())
            emb.add_field(name='<:warning2:779398023095648276> Кик:', value = random.choice(answer7))
            await ctx.send(embed=emb, delete_after=30)
 
            return

        if ctx.guild.me.top_role < member.top_role:
            emb = discord.Embed(colour=discord.Color.red())
            emb.add_field(name='<:warning2:779398023095648276> Кик:', value = random.choice(answer6))
            await ctx.send(embed=emb, delete_after=30)
 
            return

        elif ctx.author.top_role == member.top_role:
            emb = discord.Embed(colour=discord.Color.red())
            emb.add_field(name='<:warning2:779398023095648276> Кик:', value = random.choice(answer5))
            await ctx.send(embed=emb, delete_after=30)
 
            return
 
 
        elif member == ctx.bot.user:
            emb = discord.Embed(colour=discord.Color.red())
            emb.add_field(name='<:warning2:779398023095648276> Кик:', value = random.choice(answer4))
            await ctx.send(embed=emb, delete_after=30)
 
            return
 
        elif ctx.author.top_role < member.top_role:
            emb = discord.Embed(colour=discord.Color.red())
            emb.add_field(name='<:warning2:779398023095648276> Кик:', value = random.choice(answer3))
            await ctx.send(embed=emb, delete_after=30)
 
            return
 
        elif member == ctx.author:
            emb = discord.Embed(colour=discord.Color.red())
            emb.add_field(name='<:warning2:779398023095648276> Кик:', value = random.choice(answer))
            await ctx.send(embed=emb, delete_after=30)
 
            return
 
        elif member == ctx.guild.owner:
            emb = discord.Embed(colour=discord.Color.red())
            emb.add_field(name='<:warning2:779398023095648276> Кик:', value = random.choice(answer2))
            await ctx.send(embed=emb, delete_after=30)
 
            return

        emb = discord.Embed(color=0x00ff2a)
        emb.add_field(name='<:warning2:779398023095648276> Кик:', value = f'Вы уверены, что хотите кикнуть `{member.name}`?')
        emb.set_footer(text='Не нажимайте на галочку, если это ошибка!')
        msg = await ctx.send(embed=emb, delete_after = 30)
        await msg.add_reaction('✅')
        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) == '✅'
        try:
            reaction, user = await self.client.wait_for('reaction_add', timeout=30.0, check = check)
        except asyncio.TimeoutError:
            emb = discord.Embed(colour=discord.Color.green())
            emb.add_field(name='<:warning2:779398023095648276> Кик:', value = 'Действие отменнено!')
            await ctx.send(embed = emb, delete_after=30 )
        else:
            if reason == None:
                try:
 
                    emb = discord.Embed( colour = discord.Color.red(), timestamp = ctx.message.created_at)
                    emb.add_field( name = '<:warning2:779398023095648276> Кик:', value = f'Вы, `{member.name}` кикнуты с сервера `{ ctx.guild.name }`!', inline = False)
                    emb.add_field( name = 'Модератор:', value = f'{ctx.author}')
 
                    await member.send( embed = emb)
 
                    await member.kick(reason=reason)
                except:
                    success = False
                else:
                    success = True
 
                emb = discord.Embed( colour = discord.Color.red(), timestamp = ctx.message.created_at)
                emb.add_field( name = '<:warning2:779398023095648276> Кик:', value = f'`{member.name}` кикнут!', inline = False)
                emb.add_field( name = 'Модератор:', value = f'{ctx.author}')
 
                await ctx.send(embed=emb)
 
                return
            try:
 
                emb = discord.Embed( colour = discord.Color.red(), timestamp = ctx.message.created_at)
                emb.add_field( name = '<:warning2:779398023095648276> Кик:', value = f'Вы, `{member.name}` кикнуты с сервера `{ ctx.guild.name }`!', inline = False)
                emb.add_field( name = 'По причине:', value = reason, inline = False)
                emb.add_field( name = 'Модератор:', value = f'{ctx.author}')
 
                await member.send( embed = emb)
 
                await member.kick(reason=reason)
            except:
                success = False
            else:
                success = True
 
            emb = discord.Embed( colour = discord.Color.red(), timestamp = ctx.message.created_at)
            emb.add_field( name = '<:warning2:779398023095648276> Кик:', value = f'`{member.name}` кикнут!', inline = False)
            emb.add_field( name = 'По причине:', value = reason, inline = False)
            emb.add_field( name = 'Модератор:', value = f'{ctx.author}')
 
            await ctx.send(embed=emb)
 
    @kick.error
    async def clear_error(self, ctx, error):
        if isinstance( error, commands.CommandOnCooldown):
            emb = discord.Embed(colour = discord.Color.red())
            emb.add_field( name = '<:warning2:779398023095648276> Ошибка:', value = 'Подождите 10 секунд перед повторным использованием!' )
            await ctx.send( embed = emb, delete_after = 10 )
        if isinstance(error, commands.BadArgument):
            emb = discord.Embed(colour = discord.Color.red())
            emb.add_field( name = '<:warning2:779398023095648276> Ошибка:', value = 'Пользователь не найден!', inline = False)
            await ctx.send( embed = emb, delete_after=30 )
 
        if isinstance( error, commands.errors.MissingRequiredArgument ):
            emb = discord.Embed(colour = discord.Color.red())
            emb.add_field( name = '<:warning2:779398023095648276> Ошибка:', value = 'Использование команды: `s*kick [Пользователь] <Причина>`' )
            await ctx.send( embed = emb, delete_after=30 )
 
        if isinstance( error, commands.errors.MissingPermissions ):
            emb = discord.Embed(colour = discord.Color.red())
            emb.add_field( name = '<:warning2:779398023095648276> Ошибка:', value = 'У вас не хватает прав!' )
            await ctx.send( embed = emb, delete_after=30 )

        if isinstance( error, commands.errors.CommandInvokeError ):
            emb = discord.Embed(colour = discord.Color.red())
            emb.add_field( name = '<:warning2:779398023095648276> Ошибка:', value = 'У бота не хватает прав!' )
            await ctx.send( embed = emb, delete_after = 30 )

    @commands.command(aliases=['бан'])
    @commands.has_permissions( kick_members = True )
    @commands.cooldown(1, per = 10, type = discord.ext.commands.BucketType.guild )
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        await ctx.message.delete()

        if ctx.guild.me.top_role == member.top_role:
            emb = discord.Embed(colour=discord.Color.red())
            emb.add_field(name='<:warning2:779398023095648276> Бан:', value = random.choice(answer7))
            await ctx.send(embed=emb, delete_after=30)
 
            return

        if ctx.guild.me.top_role < member.top_role:
            emb = discord.Embed(colour=discord.Color.red())
            emb.add_field(name='<:warning2:779398023095648276> Бан:', value = random.choice(answer6))
            await ctx.send(embed=emb, delete_after=30)
 
            return

        if ctx.author.top_role == member.top_role:
            emb = discord.Embed(colour=discord.Color.red())
            emb.add_field(name='<:warning2:779398023095648276> Бан:', value = random.choice(answer5))
            await ctx.send(embed=emb, delete_after=30)
 
            return
 
 
        elif member == ctx.bot.user:
            emb = discord.Embed(colour=discord.Color.red())
            emb.add_field(name='<:warning2:779398023095648276> Бан:', value = random.choice(answer4))
            await ctx.send(embed=emb, delete_after=30)
 
            return
 
        elif ctx.author.top_role < member.top_role:
            emb = discord.Embed(colour=discord.Color.red())
            emb.add_field(name='<:warning2:779398023095648276> Бан:', value = random.choice(answer3))
            await ctx.send(embed=emb, delete_after=30)
 
            return
 
        elif member == ctx.author:
            emb = discord.Embed(colour=discord.Color.red())
            emb.add_field(name='<:warning2:779398023095648276> Бан:', value = random.choice(answer))
            await ctx.send(embed=emb, delete_after=30)
 
            return
 
        elif member == ctx.guild.owner:
            emb = discord.Embed(colour=discord.Color.red())
            emb.add_field(name='<:warning2:779398023095648276> Бан:', value = random.choice(answer2))
            await ctx.send(embed=emb, delete_after=30)

            return
        emb = discord.Embed(color=0x00ff2a)
        emb.add_field(name='<:warning2:779398023095648276> Бан:', value = f'Вы уверены, что хотите забанить `{member.name}`?')
        emb.set_footer(text='Не нажимайте на галочку, если это ошибка!')
        msg = await ctx.send(embed=emb, delete_after = 30)
        await msg.add_reaction('✅')
        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) == '✅'
        try:
            reaction, user = await self.client.wait_for('reaction_add', timeout=30.0, check = check)
        except asyncio.TimeoutError:
            emb = discord.Embed(colour=discord.Color.green())
            emb.add_field(name='<:warning2:779398023095648276> Бан:', value = 'Действие отменнено!')
            await ctx.send(embed = emb, delete_after=30 )
        else:
 
            if reason == None:
 
                try:
 
                    emb = discord.Embed( colour = discord.Color.red(), timestamp = ctx.message.created_at)
                    emb.add_field( name = '<:warning2:779398023095648276> Бан:', value = f'Вы, `{member.name}` забаннены на сервере `{ ctx.guild.name }`!', inline = False)
                    emb.add_field( name = 'Модератор:', value = f'{ctx.author}')
 
                    await member.send( embed = emb)
 
                    await member.ban(reason=None)
                except:
                    success = False
                else:
                    success = True
 
                emb = discord.Embed( colour = discord.Color.red(), timestamp = ctx.message.created_at)
                emb.add_field( name = '<:warning2:779398023095648276> Бан:', value = f'Участник `{member.name}` забаннен!', inline = False)
                emb.add_field( name = 'Модератор:', value = f'{ctx.author}')
 
 
                await ctx.send(embed=emb)
 
                return
 
            try:
 
                emb = discord.Embed( colour = discord.Color.red(), timestamp = ctx.message.created_at)
                emb.add_field( name = '<:warning2:779398023095648276> Бан:', value = f'Вы, `{member.name}` забаннены на сервере `{ ctx.guild.name }`!', inline = False)
                emb.add_field( name = 'По причине:', value = reason, inline = False)
                emb.add_field( name = 'Модератор:', value = f'{ctx.author}')
 
                await member.send( embed = emb)
 
                await member.ban(reason=reason)
            except:
                success = False
            else:
                success = True
 
            emb = discord.Embed( colour = discord.Color.red(), timestamp = ctx.message.created_at)
            emb.add_field( name = '<:warning2:779398023095648276> Бан:', value = f'Участник `{member.name}` забаннен!', inline = False)
            emb.add_field( name = 'По причине:', value = reason, inline = False)
            emb.add_field( name = 'Модератор:', value = f'{ctx.author}')
 
 
            await ctx.send(embed=emb)
 
    @ban.error
    async def clear_error( self, ctx, error ):
        if isinstance( error, commands.CommandOnCooldown):
            emb = discord.Embed(colour = discord.Color.red())
            emb.add_field( name = '<:warning2:779398023095648276> Ошибка:', value = 'Подождите 10 секунд перед повторным использованием!' )
            await ctx.send( embed = emb, delete_after = 10 )
        if isinstance( error, commands.BadArgument ):
            emb = discord.Embed(colour = discord.Color.red())
            emb.add_field( name = '<:warning2:779398023095648276> Ошибка:', value = 'Вы указали что-то не то!' )
            await ctx.send( embed = emb, delete_after=30 )
        if isinstance( error, commands.errors.MissingRequiredArgument ):
            emb = discord.Embed(colour = discord.Color.red())
            emb.add_field( name = '<:warning2:779398023095648276> Ошибка:', value = 'Использование команды: `s*ban [Пользователь] <Причина>`' )
            await ctx.send( embed = emb, delete_after=30 )
        if isinstance( error, commands.errors.MissingPermissions ):
            emb = discord.Embed(colour = discord.Color.red())
            emb.add_field( name = '<:warning2:779398023095648276> Ошибка:', value = 'У вас не хватает прав!' )
            await ctx.send( embed = emb, delete_after=30 )
        if isinstance( error, commands.errors.CommandInvokeError ):
            emb = discord.Embed(colour = discord.Color.red())
            emb.add_field( name = '<:warning2:779398023095648276> Ошибка:', value = 'У бота не хватает прав!' )
            await ctx.send( embed = emb, delete_after = 30 ) 

    @commands.command(aliases=['размут'])
    @commands.cooldown(1, per = 10, type = discord.ext.commands.BucketType.guild )
    @commands.has_permissions( kick_members = True )
    async def unmute(self, ctx, member:discord.Member, *, reason=None):
        await ctx.message.delete()

        if ctx.guild.me.top_role == member.top_role:
            emb = discord.Embed(colour=discord.Color.red())
            emb.add_field(name='<:warning2:779398023095648276> Размут:', value = random.choice(answer7))
            await ctx.send(embed=emb, delete_after=30)
 
            return

        if ctx.guild.me.top_role < member.top_role:
            emb = discord.Embed(colour=discord.Color.red())
            emb.add_field(name='<:warning2:779398023095648276> Размут:', value = random.choice(answer6))
            await ctx.send(embed=emb, delete_after=30)
 
            return
        
        if ctx.author.top_role == member.top_role:
            emb = discord.Embed(colour=discord.Color.red())
            emb.add_field(name='<:warning2:779398023095648276> Размут:', value = random.choice(answer5))
            await ctx.send(embed=emb, delete_after=30)
 
            return
        elif member == ctx.bot.user:
            emb = discord.Embed(colour=discord.Color.red())
            emb.add_field(name='<:warning2:779398023095648276> Размут:', value = random.choice(answer4))
            await ctx.send(embed=emb, delete_after=30)
 
            return
 
        elif ctx.author.top_role < member.top_role:
            emb = discord.Embed(colour=discord.Color.red())
            emb.add_field(name='<:warning2:779398023095648276> Размут:', value = random.choice(answer3))
            await ctx.send(embed=emb, delete_after=30)
 
            return
 
        elif member == ctx.author:
            emb = discord.Embed(colour=discord.Color.red())
            emb.add_field(name='<:warning2:779398023095648276> Размут:', value = random.choice(answer))
            await ctx.send(embed=emb, delete_after=30)
 
            return
 
        elif member == ctx.guild.owner:
            emb = discord.Embed(colour=discord.Color.red())
            emb.add_field(name='<:warning2:779398023095648276> Размут:', value = random.choice(answer2))
            await ctx.send(embed=emb, delete_after=30)
 
            return        
        emb = discord.Embed(color=0x00ff2a)
        emb.add_field(name='<:warning2:779398023095648276> Размут:', value = f'Вы уверены, что хотите размутить `{member.name}`?')
        emb.set_footer(text='Не нажимайте на галочку, если это ошибка!')
        msg = await ctx.send(embed=emb, delete_after = 30)
        await msg.add_reaction('✅')
        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) == '✅'
        try:
            reaction, user = await self.client.wait_for('reaction_add', timeout=30.0, check = check)
        except asyncio.TimeoutError:
            emb = discord.Embed(colour=discord.Color.green())
            emb.add_field(name='<:warning2:779398023095648276> Размут:', value = 'Действие отменнено!')
            await ctx.send(embed = emb, delete_after=30 )
        else:
            await ctx.send('Размучиваю пользователя', delete_after = 5)
            try:
                for channel in ctx.message.guild.channels:
                    await channel.set_permissions(member, overwrite=None, reason=reason)
            except:
                success = False
            else:
                success = True
 
            if reason == None:
                emb = discord.Embed( colour = discord.Color.green(), timestamp = ctx.message.created_at)
                emb.add_field( name = '<:warning2:779398023095648276> Размут:', value = f'Вы, `{member.name}` размучены на сервере `{ ctx.guild.name }`!', inline = False)
                emb.add_field( name = 'Модератор:', value = f'{ctx.author}')
 
                await member.send( embed = emb)
            
                emb = discord.Embed( colour = discord.Color.green(), timestamp = ctx.message.created_at)
                emb.add_field( name = '<:warning2:779398023095648276> Размут:', value = f'Участник `{member.name}` размучен!', inline = False)
                emb.add_field( name = 'Модератор:', value = f'{ctx.author}')
                await ctx.send( embed = emb)
 
                return
 
            emb = discord.Embed( colour = discord.Color.green(), timestamp = ctx.message.created_at)
            emb.add_field( name = '<:warning2:779398023095648276> Размут:', value = f'Вы, `{member.name}` размучены на сервере `{ ctx.guild.name }`!', inline = False)
            emb.add_field( name = 'По причине:', value = reason, inline = False)
            emb.add_field( name = 'Модератор:', value = f'{ctx.author}')
  
            await member.send( embed = emb)
            
            emb = discord.Embed( colour = discord.Color.green(), timestamp = ctx.message.created_at)
            emb.add_field( name = '<:warning2:779398023095648276> Размут:', value = f'Участник `{member.name}` размучен!', inline = False)
            emb.add_field( name = 'По причине:', value = reason, inline = False)
            emb.add_field( name = 'Модератор:', value = f'{ctx.author}')
            await ctx.send( embed = emb)
 
    @unmute.error
    async def clear_error( self, ctx, error ):
        if isinstance( error, commands.CommandOnCooldown):
            emb = discord.Embed(colour = discord.Color.red())
            emb.add_field( name = '<:warning2:779398023095648276> Ошибка:', value = 'Подождите 10 секунд перед повторным использованием!' )
            await ctx.send( embed = emb, delete_after = 10 )
        if isinstance( error, commands.BadArgument ):
            emb = discord.Embed(colour = discord.Color.red())
            emb.add_field( name = '<:warning2:779398023095648276> Ошибка:', value = 'Вы указали что-то не то!' )
            await ctx.send( embed = emb, delete_after=30 )
        if isinstance( error, commands.errors.MissingRequiredArgument ):
            emb = discord.Embed(colour = discord.Color.red())
            emb.add_field( name = '<:warning2:779398023095648276> Ошибка:', value = 'Использование команды: `s*unmute [Пользователь]`' )
            await ctx.send( embed = emb, delete_after=30 )
        if isinstance( error, commands.errors.MissingPermissions ):
            emb = discord.Embed(colour = discord.Color.red())
            emb.add_field( name = '<:warning2:779398023095648276> Ошибка:', value = 'У вас не хватает прав!' )
            await ctx.send( embed = emb, delete_after=30 )
        if isinstance( error, commands.errors.CommandInvokeError ):
            emb = discord.Embed(colour = discord.Color.red())
            emb.add_field( name = '<:warning2:779398023095648276> Ошибка:', value = 'У бота не хватает прав!' )
            await ctx.send( embed = emb, delete_after = 30 )

    @commands.command(aliases=['мут','мьют'])
    @commands.has_permissions( kick_members = True )
    @commands.cooldown(1, per = 10, type = discord.ext.commands.BucketType.guild )
    async def mute(self, ctx, member:discord.Member, duration=None, *, reason=None):
        await ctx.message.delete()

        if ctx.guild.me.top_role == member.top_role:
            emb = discord.Embed(colour=discord.Color.red())
            emb.add_field(name='<:warning2:779398023095648276> Мут:', value = random.choice(answer7))
            await ctx.send(embed=emb, delete_after=30)
 
            return

        if ctx.guild.me.top_role < member.top_role:
            emb = discord.Embed(colour=discord.Color.red())
            emb.add_field(name='<:warning2:779398023095648276> Мут:', value = random.choice(answer6))
            await ctx.send(embed=emb, delete_after=30)
 
            return

        if ctx.author.top_role == member.top_role:
            emb = discord.Embed(colour=discord.Color.red())
            emb.add_field(name='<:warning2:779398023095648276> Мут:', value = random.choice(answer5))
            await ctx.send(embed=emb, delete_after=30)
 
            return
 
 
        elif member == ctx.bot.user:
            emb = discord.Embed(colour=discord.Color.red())
            emb.add_field(name='<:warning2:779398023095648276> Мут:', value = random.choice(answer4))
            await ctx.send(embed=emb, delete_after=30)
 
            return
 
        elif ctx.author.top_role < member.top_role:
            emb = discord.Embed(colour=discord.Color.red())
            emb.add_field(name='<:warning2:779398023095648276> Мут:', value = random.choice(answer3))
            await ctx.send(embed=emb, delete_after=30)
 
            return
 
        elif member == ctx.author:
            emb = discord.Embed(colour=discord.Color.red())
            emb.add_field(name='<:warning2:779398023095648276> Мут:', value = random.choice(answer))
            await ctx.send(embed=emb, delete_after=30)
 
            return
 
        elif member == ctx.guild.owner:
            emb = discord.Embed(colour=discord.Color.red())
            emb.add_field(name='<:warning2:779398023095648276> Мут:', value = random.choice(answer2))
            await ctx.send(embed=emb, delete_after=30)
 
            return
        emb = discord.Embed(color=0x00ff2a)
        emb.add_field(name='<:warning2:779398023095648276> Мут:', value = f'Вы уверены, что хотите замутить `{member.name}`?')
        emb.set_footer(text='Не нажимайте на галочку, если это ошибка!')
        msg = await ctx.send(embed=emb, delete_after = 30)
        await msg.add_reaction('✅')
        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) == '✅'
        try:
            reaction, user = await self.client.wait_for('reaction_add', timeout=30.0, check = check)
        except asyncio.TimeoutError:
            emb = discord.Embed(colour=discord.Color.green())
            emb.add_field(name='<:warning2:779398023095648276> Мут:', value = 'Действие отменнено!')
            await ctx.send(embed = emb, delete_after=30 )
        else:
 
            if duration == None:
                if reason == None:
                    try:
                        progress = await ctx.send('Мьючу пользователя!', delete_after = 5)
 
                        emb = discord.Embed( colour = discord.Color.red(), timestamp = ctx.message.created_at)
                        emb.add_field( name = '<:warning2:779398023095648276> Мут:', value = f'Участник `{member.name}` замучен!\nОн не выйдет из мута, пока его не размутят!', inline = False)
                        emb.add_field( name = 'Модератор:', value = f'{ctx.author}')
 
                        await ctx.send( embed = emb)
   
 
                        for channel in ctx.guild.text_channels:
                            await channel.set_permissions(member, overwrite=discord.PermissionOverwrite(send_messages = False), reason=reason)
    
                        for channel in ctx.guild.voice_channels:
                            await channel.set_permissions(member, overwrite=discord.PermissionOverwrite(speak=False), reason=reason)
                    except:
                        success = False
                    else:
                        success = True
 
                    emb = discord.Embed( colour = discord.Color.red(), timestamp = ctx.message.created_at)
                    emb.add_field( name = '<:warning2:779398023095648276> Мут:', value = f'Вы, `{member.name}` замучены на сервере `{ ctx.guild.name }`!\nВы не выйдете из мута, пока вас не размутят!', inline = False)
                    emb.add_field( name = 'Модератор:', value = f'{ctx.author}')
 
                    await member.send( embed = emb)
 
 
                    return
 
 
                try:
                    progress = await ctx.send('Мьючу пользователя!', delete_after = 5)
 
                    emb = discord.Embed( colour = discord.Color.red(), timestamp = ctx.message.created_at)
                    emb.add_field( name = '<:warning2:779398023095648276> Мут:', value = f'Участник `{member.name}` замучен!\nОн не выйдет из мута, пока его не размутят!', inline = False)
                    emb.add_field( name = 'Модератор:', value = f'{ctx.author}')
 
                    await ctx.send( embed = emb)
  
 
                    for channel in ctx.guild.text_channels:
                        await channel.set_permissions(member, overwrite=discord.PermissionOverwrite(send_messages = False), reason=reason)
   
                    for channel in ctx.guild.voice_channels:
                        await channel.set_permissions(member, overwrite=discord.PermissionOverwrite(speak=False), reason=reason)
                except:
                    success = False
                else:
                    success = True
 
                emb = discord.Embed( colour = discord.Color.red(), timestamp = ctx.message.created_at)
                emb.add_field( name = '<:warning2:779398023095648276>  Мут:', value = f'Вы, `{member.name}` замучены на сервере `{ ctx.guild.name }`!\nВы не выйдете из мута, пока вас не размутят!', inline = False)
                emb.add_field( name = 'Модератор:', value = f'{ctx.author}')
 
                await member.send( embed = emb)
 
                return
 
 
            unit = duration[-1]
            if unit == 'с':
                time = int(duration[:-1])
                longunit = 'секунд'
            elif unit == 's':
                time = int(duration[:-1])
                longunit = 'секунд'
            elif unit == 'м':
                time = int(duration[:-1]) * 60
                longunit = 'минуту/минут'
            elif unit == 'm':
                time = int(duration[:-1]) * 60
                longunit = 'минуту/минут'
            elif unit == 'ч':
                time = int(duration[:-1]) * 60 * 60
                longunit = 'час/часов'
            elif unit == 'h':
                time = int(duration[:-1]) * 60 * 60
                longunit = 'час/часов'
            elif unit == 'д':
                time = int(duration[:-1]) * 60 * 60 *24
                longunit = 'день/дней'
            elif unit == 'd':
                time = int(duration[:-1]) * 60 * 60 *24
                longunit = 'день/дней'
            else:
                await ctx.send('Неправильное написание времени!', delete_after = 30)
                return
 
            if reason == None:
                try:
                    progress = await ctx.send('Мьючу пользователя!', delete_after = 5)
 
                    emb = discord.Embed( colour = discord.Color.red(), timestamp = ctx.message.created_at)
                    emb.add_field( name = '<:warning2:779398023095648276> Мут:', value = f'Участник `{member.name}` замучен!\nОн выйдет из мута через: {str(duration[:-1])} {longunit}', inline = False)
                    emb.add_field( name = 'Модератор:', value = f'{ctx.author}')
 
                    await ctx.send( embed = emb)
 
  
                    for channel in ctx.guild.text_channels:
                        await channel.set_permissions(member, overwrite=discord.PermissionOverwrite(send_messages = False), reason=reason)
 
                    for channel in ctx.guild.voice_channels:
                        await channel.set_permissions(member, overwrite=discord.PermissionOverwrite(speak=False), reason=reason)
                except:
                    success = False
                else:
                    success = True
 
                emb = discord.Embed( colour = discord.Color.red(), timestamp = ctx.message.created_at)
                emb.add_field( name = '<:warning2:779398023095648276> Мут:', value = f'Вы, `{member.name}` замучены на сервере `{ ctx.guild.name }`!\nВы выйдете из мута через: {str(duration[:-1])} {longunit}', inline = False)
                emb.add_field( name = 'Модератор:', value = f'{ctx.author}')
 
                await member.send( embed = emb)
    
                await asyncio.sleep(time)
                try:
                    for channel in ctx.guild.channels:
                        await channel.set_permissions(member, overwrite=None, reason=reason)
                except:
                    pass
 
                return
  
            try:
                progress = await ctx.send('Мьючу пользователя!', delete_after = 5)
 
                emb = discord.Embed( colour = discord.Color.red(), timestamp = ctx.message.created_at)
                emb.add_field( name = '<:warning2:779398023095648276> Мут:', value = f'Участник `{member.name}` замучен!\nОн выйдет из мута через: {str(duration[:-1])} {longunit}', inline = False)
                emb.add_field( name = 'По причине:', value = reason, inline = False)
                emb.add_field( name = 'Модератор:', value = f'{ctx.author}')
 
                await ctx.send( embed = emb)
 
 
                for channel in ctx.guild.text_channels:
                    await channel.set_permissions(member, overwrite=discord.PermissionOverwrite(send_messages = False), reason=reason)
 
                for channel in ctx.guild.voice_channels:
                    await channel.set_permissions(member, overwrite=discord.PermissionOverwrite(speak=False), reason=reason)
            except:
                success = False
            else:
                success = True
 
            emb = discord.Embed( colour = discord.Color.red(), timestamp = ctx.message.created_at)
            emb.add_field( name = '<:warning2:779398023095648276> Мут:', value = f'Вы, `{member.name}` замучены на сервере `{ ctx.guild.name }`!\nВы выйдете из мута через: {str(duration[:-1])} {longunit}', inline = False)
            emb.add_field( name = 'По причине:', value = reason, inline = False)
            emb.add_field( name = 'Модератор:', value = f'{ctx.author}')
  
            await member.send( embed = emb)
    
            await asyncio.sleep(time)
            try:
                for channel in ctx.guild.channels:
                    await channel.set_permissions(member, overwrite=None, reason=reason)
            except:
                pass
 
 
    @mute.error
    async def clear_error( self, ctx, error ):
        if isinstance( error, commands.CommandOnCooldown):
            emb = discord.Embed(colour = discord.Color.red())
            emb.add_field( name = '<:warning2:779398023095648276> Ошибка:', value = 'Подождите 10 секунд перед повторным использованием!' )
            await ctx.send( embed = emb, delete_after = 10 )
        if isinstance( error, commands.BadArgument ):
            emb = discord.Embed(colour = discord.Color.red())
            emb.add_field( name = '<:warning2:779398023095648276> Ошибка:', value = 'Вы что-то указали не то!' )
            await ctx.send( embed = emb, delete_after=30 )
        if isinstance( error, commands.errors.MissingRequiredArgument ):
            emb = discord.Embed(colour = discord.Color.red())
            emb.add_field( name = '<:warning2:779398023095648276> Ошибка:', value = 'Использование команды: `s*mute [Пользователь] <Время> (Причина)`' )
            await ctx.send( embed = emb, delete_after=30)
        if isinstance( error, commands.errors.MissingPermissions ):
            emb = discord.Embed(colour = discord.Color.red())
            emb.add_field( name = '<:warning2:779398023095648276> Ошибка:', value = 'У вас не хватает прав!' )
            await ctx.send( embed = emb, delete_after=30 )

    @commands.command(
        aliases=['жалоба', 'send-report'],
        description = 'Отправить жалобу',
        usage = 'жалоба @ник [жалоба]'
    )
    async def report(self, ctx, member: discord.Member=None, *, reason=None):
        if not collection.find_one({"guild_id": ctx.guild.id}):
            embed = discord.Embed(title="Ошибка", description="Система жалоб на этом сервере не включена!\nЧтобы включить введите - `s*report-channel <on/off> <channel>`", color=discord.Color.red())
            await ctx.send(embed=embed)
        else:
            if member is None:
                embed = discord.Embed(title="<:warning2:779398023095648276> Ошибка", description="Укажите пользователя `s*report [Пользователь] <Причина>`", color=discord.Color.red())
                await ctx.send(embed=embed)
            elif reason is None:
                embed = discord.Embed(title="<:warning2:779398023095648276> Ошибка", description="Укажите причину жалобы `s*report [Пользователь] <Причина>`", color=discord.Color.red())
                await ctx.send(embed=embed)
            elif member == ctx.author:
                embed = discord.Embed(title="<:warning2:779398023095648276> Ошибка", description="Вы не можете отправить жалобу на себя", color=discord.Color.red())
                await ctx.send(embed=embed)
            else:
                if ctx.message.attachments:
                    for i in ctx.message.attachments:
                        channelid = collection.find_one({"guild_id": ctx.guild.id})["channel_id"]
                        channel = ctx.guild.get_channel(channelid)
                        embed = discord.Embed(title="<:warning2:779398023095648276> Жалоба", description="Жалоба была успешно отправлена в канал для жалоб!", color=discord.Color.green())
                        await ctx.send(embed=embed)
                        embed2 = discord.Embed(title="<:warning2:779398023095648276> Новая Жалоба!", description=f"**Отправитель:** {ctx.author.mention}\n**Нарушитель:** {member.mention}\n**Причина:** {reason}", color=discord.Color.green())
                        embed2.set_image(url=i.url)
                        msg = await channel.send(embed=embed2)
                        await msg.add_reaction("✅")
                        await msg.add_reaction("❌")
                        break
                else:
                    channelid = collection.find_one({"guild_id": ctx.guild.id})["channel_id"]
                    channel = ctx.guild.get_channel(channelid)
                    embed = discord.Embed(title="<:warning2:779398023095648276> Жалоба", description="Жалоба была успешно отправлена в канал для жалоб!", color=discord.Color.green())
                    await ctx.send(embed=embed)
                    embed2 = discord.Embed(title="<:warning2:779398023095648276> Новая Жалоба!", description=f"**Отправитель:** {ctx.author.mention}\n**Нарушитель:** {member.mention}\n**Причина:** {reason}", color=discord.Color.green())
                    msg = await channel.send(embed=embed2)
                    await msg.add_reaction("✅")
                    await msg.add_reaction("❌")   

    @report.error
    async def clear_error( self, ctx, error ):
        if isinstance( error, discord.ext.commands.errors.MemberNotFound ):
            emb = discord.Embed(colour = discord.Color.red())
            emb.add_field( name = '<:warning2:779398023095648276> Ошибка:', value = 'Нет такого пользователя.' )
            await ctx.send( embed = emb, delete_after=30 )
        if isinstance( error, commands.errors.MissingRequiredArgument ):
            emb = discord.Embed(colour = discord.Color.red())
            emb.add_field( name = '<:warning2:779398023095648276> Ошибка:', value = 'Использование команды: `s*report [Пользователь] <Причина>`' )
            await ctx.send( embed = emb, delete_after=30 )

def setup(client):
    client.add_cog(administration(client)) 
