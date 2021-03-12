import discord
from discord.ext import commands
from time import sleep
import random, asyncio
from discord.ext.commands import Bot 
from discord.utils import get
import json

import requests
from bs4 import BeautifulSoup

class different(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.cog_name = ["разное"]

    @commands.command(aliases=["кот"], description="Выведет рандомного кота", usage="кот")
    async def cat(self, ctx):
        for item in json.loads(requests.get("https://api.thecatapi.com/v1/images/search").text):
            embed = discord.Embed(color=discord.Color.blue())
            embed.set_image(url=item["url"])
            await ctx.send(embed=embed)
            break

    @commands.command(aliases=["собака"], description="Выведет рандомную собаку", usage="собака")
    async def dog(self, ctx):
        response = requests.get('https://api.thedogapi.com/v1/images/search')
        json_data = json.loads(response.text)
        url = json_data[0]['url']

        embed = discord.Embed(title="Вот собачка! Гаф!", color=0xff9900)
        embed.set_image(url=url)

        await ctx.send(embed=embed)

    @commands.command(aliases=["панда"], description="Выведет рандомную панду", usage="панда")
    async def panda(self, ctx):
        response = requests.get('https://some-random-api.ml/img/panda')
        jsoninf = json.loads(response.text)
        url = jsoninf['link']
        embed = discord.Embed(color=0xff9900)
        embed.set_image(url=url)
        await ctx.send(embed=embed)

    @commands.command(
        aliases=["птица"],
        description="Выведет рандомную птицу",
        usage="птица")
    async def bird(self, ctx):
        response = requests.get('https://some-random-api.ml/img/birb')
        jsoninf = json.loads(response.text)
        url = jsoninf['link']
        embed = discord.Embed(color=0xff9900)
        embed.set_image(url=url)
        await ctx.send(embed=embed)

    @commands.command(
        aliases=["лиса"],
        description="Выведет рандомную лису",
        usage="лиса")
    async def fox(self, ctx):
        response = requests.get('https://some-random-api.ml/img/fox')
        jsoninf = json.loads(response.text)
        url = jsoninf['link']
        embed = discord.Embed(color=0xff9900)
        embed.set_image(url=url)
        await ctx.send(embed=embed)

    @commands.command(
        aliases=["коала"],
        description="Выведет рандомную коалу",
        usage="коала")
    async def koala(self, ctx):
        response = requests.get('https://some-random-api.ml/img/koala')
        jsoninf = json.loads(response.text)
        url = jsoninf['link']
        embed = discord.Embed(color=0xff9900)
        embed.set_image(url=url)
        await ctx.send(embed=embed)

    @commands.command(
        aliases=["красная_панда"],
        description="Выведет рандомную красную панду",
        usage="красная_панда"
    )
    async def red_panda(self, ctx):
        response = requests.get('https://some-random-api.ml/img/red_panda')
        jsoninf = json.loads(response.text)
        url = jsoninf['link']
        embed = discord.Embed(color=0xff9900)
        embed.set_image(url=url)
        await ctx.send(embed=embed)

    @commands.command(aliases = ['anime','аниме'])
    async def user_anime(self, ctx):
        anime = [
        'https://static2.aniimg.com/upload/20170606/712/F/5/O/F5OGEF.jpg',
        'https://get.wallhere.com/photo/illustration-anime-anime-girls-short-hair-cartoon-black-hair-sweater-mouth-mangaka-41663.jpg',
        'https://static.zerochan.net/Kuroyukihime.full.1028240.jpg',
        'https://static.zerochan.net/IA.full.1212336.jpg',
        'https://wallpapercave.com/wp/wp2579738.jpg',
        'https://images.wallpaperscraft.ru/image/anime_devushka_lico_glaza_23057_1920x1200.jpg',
        'https://get.wallhere.com/photo/illustration-blonde-long-hair-anime-anime-girls-looking-at-viewer-cartoon-school-uniform-mangaka-49934.jpg',
        'http://pm1.narvii.com/6933/109db960f03a808a2d04d4f78f290fa19a9fb56dr1-1920-1200v2_uhq.jpg',
        'https://i.ucrazy.ru/files/i/2011.8.11/1313061791_anime_anime_sport_girl_018649_.jpg',
        'http://pm1.narvii.com/7065/3c4b5db0614269a1a6ae858ebfe0706ee7602bfbr1-1440-900v2_uhq.jpg',
        'https://proprikol.ru/wp-content/uploads/2019/11/kartinki-anime-s-ushkami-10.jpg',
        'https://get.wallhere.com/photo/illustration-long-hair-anime-anime-girls-clouds-blue-school-uniform-visual-novel-schoolgirl-If-My-Heart-Had-Wings-Habane-Kotori-computer-wallpaper-mangaka-143320.jpg',
        'https://wallpapercave.com/wp/wp3238040.jpg',
        'http://pm1.narvii.com/6881/7ad4347d226019de248098c5a2d65ace8cc4c494r1-1920-1080v2_uhq.jpg',
        'https://million-wallpapers.ru/wallpapers/3/69/390987900899292/denpa-onna-chtoby-seishun-otoko.jpg',
        'https://wallup.net/wp-content/uploads/2018/09/26/215906-anime-Vocaloid-Hatsune_Miku.jpg',
        'https://i.artfile.ru/1920x1080_1464584_[www.ArtFile.ru].jpg',
        'https://static.zerochan.net/Gurenka.full.1179328.jpg',
        'http://pm1.narvii.com/7117/429293446f7b6681ee4d5a2a9474969fed7282dar1-2048-1152v2_uhq.jpg',
        'https://i.ucrazy.ru/files/i/2011.8.11/1313061866_anime_bride_013359_.jpg',
        'https://img1.goodfon.ru/original/1920x1403/6/96/art-awakawayui-hatsune-miku.jpg',
        'http://pm1.narvii.com/7132/d06bb8b9ff95e99d0f12c35b8eaebc3aae6f6e1ar1-1920-1440v2_uhq.jpg',
        'https://get.wallhere.com/photo/shoufukucho-anime-girl-look-wind-1001035.jpg',
        'https://get.wallhere.com/photo/illustration-blonde-night-anime-Moon-blue-girl-sweet-screenshot-computer-wallpaper-fictional-character-725975.jpg',
        'https://i.ucrazy.ru/files/i/2011.8.11/1313061783_anime_anime_013328_.jpg'
        ]
        images = random.choice(anime)
        emb = discord.Embed(title = f'**Аниме:**', color = 0x00ff2a)
        emb.set_image(url = f'{images}')

        await ctx.send(embed = emb)
        
def setup(client):
    client.add_cog(different(client))