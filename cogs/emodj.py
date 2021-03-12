import discord
from discord.ext import commands
from discord.utils import get
import sqlite3
import asyncio
import nekos

import random

class love(commands.Cog):
    
    def __init__(self, client):
        self.client = client
        self.cog_name = ['эмоции']

    @commands.command(
        aliases = ['обнять', 'hug'],
        description='обнять игрока',
        usage='обнять <@ник>'
    )
    async def _hug(self, ctx, member: discord.Member):
        if member == ctx.author:
            return await ctx.send(embed = discord.Embed(description = '<:warning2:779398023095648276> Ты не можешь обнять самого себя!',color=0xff2929))
 
        if member == None:
            return await ctx.send(embed = discord.Embed(description = '<:warning2:779398023095648276> Обязательно укажи пользователя!',color=0xff2929))

        g = ['hug']
        gnek = nekos.img(random.choice(g))
        emb = discord.Embed(title = f'**Обнимашки!**',description = f'{ctx.author.mention} обнял(а) {member.mention}', color=0xFF0000)
        emb.set_image(url = gnek) 
        emb.set_footer(text=f'Вызвано: {ctx.message.author}',icon_url=ctx.message.author.avatar_url) 
        await ctx.send(embed=emb)

    @_hug.error
    async def clear_error( self, ctx, error ):
        if isinstance( error, commands.errors.MissingRequiredArgument ):
            emb = discord.Embed(colour = discord.Color.red())
            emb.add_field( name = '<:warning2:779398023095648276> Ошибка:', value = 'Использование команды: `s*hug [Пользователь]`' )
            await ctx.send( embed = emb, delete_after = 30 )

    @commands.command(
        aliases = ['тыкнуть', 'poke'],
        description='тыкнуть игрока',
        usage='тыкнуть <@ник>'
    )
    async def _poke(self, ctx, member: discord.Member):
        if member == ctx.author:
            return await ctx.send(embed = discord.Embed(description = '<:warning2:779398023095648276> Ты не можешь тыкнуть самого себя!',color=0xff2929))
 
        if member == None:
            return await ctx.send(embed = discord.Embed(description = '<:warning2:779398023095648276> Обязательно укажи пользователя!',color=0xff2929))

        n = ['poke']
        nnek = nekos.img(random.choice(n))
        emb = discord.Embed(title = f'**Тыкание!**',description = f'{ctx.author.mention} тыкнул(а) {member.mention}', color=0xFF0000)
        emb.set_image(url = nnek) 
        emb.set_footer(text=f'Вызвано: {ctx.message.author}',icon_url=ctx.message.author.avatar_url) 
        await ctx.send(embed=emb)

    @_poke.error
    async def clear_error( self, ctx, error ):
        if isinstance( error, commands.errors.MissingRequiredArgument ):
            emb = discord.Embed(colour = discord.Color.red())
            emb.add_field( name = '<:warning2:779398023095648276> Ошибка:', value = 'Использование команды: `s*poke [Пользователь]`' )
            await ctx.send( embed = emb, delete_after = 30 )

    @commands.command(
        aliases = ['погладить', 'pat'],
        description='погладить игрока',
        usage='погладить <@ник>'
    )
    async def _pat(self, ctx, member: discord.Member):
        if member == ctx.author:
            return await ctx.send(embed = discord.Embed(description = '<:warning2:779398023095648276> Ты не можешь погладить самого себя!', color=0xff2929))
 
        if member == None:
            return await ctx.send(embed = discord.Embed(description = '<:warning2:779398023095648276> Обязательно укажи пользователя!', color=0xff2929))

        snek = 'https://some-random-api.ml/animu/pat'
        emb = discord.Embed(title = f'**Внимание!**',description = f'{ctx.author.mention} погладил(а) {member.mention}', color=0xFF0000)
        emb.set_image(url = snek) 
        emb.set_footer(text=f'Вызвано: {ctx.message.author}',icon_url=ctx.message.author.avatar_url) 
        await ctx.send(embed=emb)

    @_pat.error
    async def clear_error( self, ctx, error ):
        if isinstance( error, commands.errors.MissingRequiredArgument ):
            emb = discord.Embed(colour = discord.Color.red())
            emb.add_field( name = '<:warning2:779398023095648276> Ошибка:', value = 'Использование команды: `s*pat [Пользователь]`' )
            await ctx.send( embed = emb, delete_after = 30 )

    @commands.command(
        aliases = ['поцеловать', 'kiss'],
        description='поцеловать игрока',
        usage='поцеловать <@ник>'
    )
    async def _kiss(self, ctx, member: discord.Member):
        if member == ctx.author:
            return await ctx.send(embed = discord.Embed(description = '<:warning2:779398023095648276> Ты не можешь поцеловать самого себя!', color=0xff2929))
 
        if member == None:
            return await ctx.send(embed = discord.Embed(description = '<:warning2:779398023095648276> Обязательно укажи пользователя!', color=0xff2929))

        k = ['kiss']
        knek = nekos.img(random.choice(k))
        emb = discord.Embed(title = f'**Поцелуйчик!**',description = f'{ctx.author.mention} поцеловал(а) {member.mention}', color=0xFF0000)
        emb.set_image(url = knek) 
        emb.set_footer(text=f'Вызвано: {ctx.message.author}',icon_url=ctx.message.author.avatar_url) 
        await ctx.send(embed=emb)

    @_kiss.error
    async def clear_error( self, ctx, error ):
        if isinstance( error, commands.errors.MissingRequiredArgument ):
            emb = discord.Embed(colour = discord.Color.red())
            emb.add_field( name = '<:warning2:779398023095648276> Ошибка:', value = 'Использование команды: `s*kiss [Пользователь]`' )
            await ctx.send( embed = emb, delete_after = 30 )

def setup(client):
    client.add_cog(love(client))