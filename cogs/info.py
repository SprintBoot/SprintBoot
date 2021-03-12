import discord
from discord.ext import commands
from discord.utils import get
from module.sb import config
from mcstatus import MinecraftServer
import json
import wikipedia
import requests
import datetime
import time

COLOR_GOOD = config.COLOR_GOOD

class info(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.cog_name = ["информация"]

    @commands.command(name="banner")
    async def serv_banner(self, ctx):
        if not ctx.guild.banner:
            embed = discord.Embed(title=(f"На этом сервере нет баннера..."), colour = discord.Color.red())
            return await ctx.send(embed=embed)
        embed = discord.Embed(title=(f"Баннер сервера **{ctx.guild.name}**\n{ctx.guild.banner_url_as(format='png')}"),colour = discord.Color.green())
        embed.set_footer(text=f'Команда вызвана юзером: {ctx.author}', icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(
        aliases = ["Аватар", "аватар", "Аватарка", "аватарка", "Avatar",  ],
        description ='посмотреть аватарку игрока',
        usage='аватар <@ник>'       
    )
    async def avatar(self, ctx, member : discord.Member = None):

        user = ctx.message.author if (member == None) else member

        embed = discord.Embed(title=f'Аватарка юзера {user}', color= 0x2b86fd)

        embed.set_image(url=user.avatar_url)
        embed.set_footer(text=f'Команда вызвана юзером: {ctx.author}', icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @avatar.error
    async def clear_error( self, ctx, error ):
        if isinstance( error, commands.errors.MissingRequiredArgument ):
            emb = discord.Embed(colour = discord.Color.red())
            emb.add_field( name = '<:warning2:779398023095648276> Ошибка:', value = 'Использование команды: `s*avatar [Пользователь]`' )
            await ctx.send( embed = emb, delete_after = 30 )

    @commands.command()
    async def roleinfo(self, ctx, Role: discord.Role ):
        await ctx.message.add_reaction("✅")
        guild = ctx.guild
        emb = discord.Embed(title=f'Информация о роли {Role.name}'.format(Role.name), description=f"Роль создали {Role.created_at.strftime('%b %#d, %Y')}\n\n"
                                                                                       f"Название роли: {Role.name}\n\nЦвет: {Role.colour}\n\n"
                                                                                       f"Позиция: {Role.position}\n\n",colour= Role.colour, timestamp=ctx.message.created_at)

        emb.set_footer(text=f"ID Пользователя: {ctx.author.id}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=emb)

    @roleinfo.error
    async def clear_error( self, ctx, error ):
        if isinstance( error, commands.errors.MissingRequiredArgument ):
            emb = discord.Embed(colour = discord.Color.red())
            emb.add_field( name = '<:warning2:779398023095648276> Ошибка:', value = 'Использование команды: `s*roleinfo [Роль]`' )
            await ctx.send( embed = emb, delete_after = 30 )

    @commands.command(
        aliases=['пригласить', 'приглашение'],
        description='пригласить бота',
        usage='invite'        
        )
    async def invite(self, ctx):

        embedinvite = discord.Embed(title=f"Добавление бота на сервер:",
                                  description="Тут вы можите посмотреть ,как пригласить бота!",                                  
                                  color=0x00ff2a)
        embedinvite.add_field(name=f"Приглашение бота:", value=f"||https://discord.com/api/oauth2/authorize?client_id=812307397241602059&permissions=8&scope=bot||", inline=False)
        embedinvite.set_footer(text=f'Команда вызвана юзером: {ctx.author}', icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embedinvite)

    @commands.command(
        aliases=['сервер', 'серверинфо', 'server'],
        description="Информация о сервере",
        usage='server'
    )
    async def _server(self, ctx):    

        members = ctx.guild.members
        bots = len([m for m in members if m.bot])
        users = len(members) - bots
        online = len(list(filter(lambda x: x.status == discord.Status.online, members)))
        offline = len(list(filter(lambda x: x.status == discord.Status.offline, members)))
        idle = len(list(filter(lambda x: x.status == discord.Status.idle, members)))
        dnd = len(list(filter(lambda x: x.status == discord.Status.dnd, members)))
        allvoice = len(ctx.guild.voice_channels)
        alltext = len(ctx.guild.text_channels)
        allroles = len(ctx.guild.roles)

        embed = discord.Embed(title=f"{ctx.guild.name}", color=config.COLOR_GOOD, timestamp=ctx.message.created_at)
        embed.set_thumbnail(url=ctx.guild.icon_url)

        embed.add_field(name=f"Пользователи", value=f"<:users:794599070584930334> Участников: **{users}**\n"
                                                     f"<:bot:794599070676680724> Ботов: **{bots}**\n"
                                                     f"<:online_oxzy:779398023133659186> Онлайн: **{online}**\n"
                                                     f"<:Idle_oxzy:779398023112818748> Отошёл: **{idle}**\n"
                                                     f"<:DND_Oxzy:779398023104692265> Не Беспокоить: **{dnd}**\n"
                                                     f"<:status_offline:779398023172063233> Оффлайн: **{offline}**")

        embed.add_field(name=f"Общая информация", value=f"<:voice:794599070308106271> Голосовые: **{allvoice}**\n"
                                               f"<:text:794599070358437939> Текстовые: **{alltext}**\n"
                                               f"<:user:794599070664491038> Создатель сервера: **{ctx.guild.owner}**\n"
                                               f"<:Chugoku:779398023733182474> Регион сервера: **{ctx.guild.region}**\n"
                                               f"<:chat:794599070587944960> Дата создания: **{ctx.guild.created_at.strftime('%b %#d %Y')}**\n")

        embed.set_footer(text="Все права защищены | 𝓐𝓿𝓪𝓴𝓾𝓶 𝓟𝓻𝓸𝓭𝓾𝓬𝓻𝓲𝓸𝓷", icon_url="https://media.discordapp.net/attachments/745931540248264814/794544313027657738/printtwohiwriteme481516.png?width=494&height=494")
        await ctx.send(embed=embed)

    @commands.command(
        aliases = ['инфо', 'info'],
        description='узнать о боте',
        usage='info'
    )
    async def bote(self, ctx):
        members = 0
        for guild in self.client.guilds:
            members += guild.member_count

        embedinfo = discord.Embed(title=f"<:SyalisBear:779398024082096178> Информация О Боте",
                                  description="**<:status_idle:779398022638993439> Кто такой SprintBoot New?**\nЭто бот который создан специально для других серверов. Лучше ,чем его присшественник!",
                                  color=config.COLOR_GOOD)
        embedinfo.set_thumbnail(url=self.client.user.avatar_url)
        embedinfo.add_field(name=f"<:IMessages:779398024026652692> Серверов:", value=len(self.client.guilds), inline=True)
        embedinfo.add_field(name=f"<:users_logo:779398023183859763> Пользователей:", value=members, inline=True)
        embedinfo.add_field(name="‎‎‎‎", value="‎", inline=True)
        embedinfo.add_field(name=f"<:devNew:779398023180058634> Создатель Бота:", value=f"SprintBook#2891", inline=True)
        embedinfo.add_field(name=f"<:warning2:779398023095648276> Чтоб настроить:", value=f"Пропишите `s.settings`", inline=True)             
        embedinfo.add_field(name=f"<:online_oxzy:779398023133659186> Пинг Бота:", value=f"{self.client.ws.latency * 1000:.0f} ms", inline=True)
        embedinfo.add_field(name=f"<:PartnerServer:779390165218230272> Сервер поддержки:", value=f"https://discord.gg/SqrRUKDqn3", inline=True)
        embedinfo.set_footer(text="Все права защищены | 𝓐𝓿𝓪𝓴𝓾𝓶 𝓟𝓻𝓸𝓭𝓾𝓬𝓻𝓲𝓸𝓷", icon_url="https://media.discordapp.net/attachments/745931540248264814/794544313027657738/printtwohiwriteme481516.png?width=494&height=494")
        await ctx.send(embed=embedinfo)

    @commands.command(
        aliases = ["News", "новость", "Новость" ],
        description = 'Новость сервера',
        usage = 'новость <текст>'
    )
    @commands.has_permissions( administrator = True )
    async def news(self, ctx, *, arg):

        news = discord.Embed(title = "Новости сервера", description = f"{arg}", color = 0x800080)
        news.set_thumbnail( url = ctx.guild.icon_url )
        news.set_footer(text=f'Новость написал: {ctx.author}', icon_url=ctx.author.avatar_url)

        await ctx.send(embed = news)

    @news.error
    async def clear_error(self, ctx, error):
        if isinstance( error, commands.errors.MissingPermissions ):
            emb = discord.Embed(colour = discord.Color.red())
            emb.add_field( name = '<:warning2:779398023095648276> Ошибка:', value = 'У вас не хватает прав!' )
            await ctx.send( embed = emb, delete_after=30 )

        if isinstance( error, commands.errors.CommandInvokeError ):
            emb = discord.Embed(colour = discord.Color.red())
            emb.add_field( name = '<:warning2:779398023095648276> Ошибка:', value = 'У бота не хватает прав!' )
            await ctx.send( embed = emb, delete_after = 30 )

    @commands.command(
        aliases=['голосование', 'quickpoll'],
        description = 'Устроить голосование',
        usage = 'голосование <текст>'
    )
    @commands.has_permissions( administrator=True)
    async def poll(self, ctx, *, question=None):
        if question is None:
            embed = discord.Embed(title="Ошибка", description="Укажите тему голосования!", color=discord.Color.red())
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="Голосование", description=f"**{question}**\n \n <:greentick:779972887188209684> - **Да** \n \n <:redtick:779972887028957186>  - **Нет**\n", color=discord.Color.green())
            embed.set_footer(text=f'Команда вызвана юзером: {ctx.author}', icon_url=ctx.author.avatar_url)
            bruh = await ctx.send(embed=embed)
            await bruh.add_reaction("<:greentick:779972887188209684>")
            await bruh.add_reaction("<:redtick:779972887028957186>")

    @poll.error
    async def clear_error(self, ctx, error):
        if isinstance( error, commands.errors.MissingPermissions ):
            emb = discord.Embed(colour = discord.Color.red())
            emb.add_field( name = '<:warning2:779398023095648276> Ошибка:', value = 'У вас не хватает прав!' )
            await ctx.send( embed = emb, delete_after=30 )

        if isinstance( error, commands.errors.CommandInvokeError ):
            emb = discord.Embed(colour = discord.Color.red())
            emb.add_field( name = '<:warning2:779398023095648276> Ошибка:', value = 'У бота не хватает прав!' )
            await ctx.send( embed = emb, delete_after = 30 )

    @commands.command(
        aliases=['вики', 'wiki'],
        description='узнать информацию на вики',
        usage='вики <информация>'
    )
    async def _wiki(self, ctx, *, text):
        wikipedia.set_lang("ru")
        new_page = wikipedia.page(text)
        summ = wikipedia.summary(text)
        emb = discord.Embed(
            title= new_page.title,
            description= summ,
            color = 0x00ffff
         )
        emb.set_author(name= 'Больше информации тут!', url= new_page.url, icon_url= 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Wikipedia-logo-v2.svg/1200px-Wikipedia-logo-v2.svg.png')

        await ctx.send(embed=emb)

    @_wiki.error
    async def clear_error(self, ctx, error):
        if isinstance( error, commands.errors.MissingPermissions ):
            emb = discord.Embed(colour = discord.Color.red())
            emb.add_field( name = '<:warning2:779398023095648276> Ошибка:', value = 'У вас не хватает прав!' )
            await ctx.send( embed = emb, delete_after=30 )

        if isinstance( error, commands.errors.CommandInvokeError ):
            emb = discord.Embed(colour = discord.Color.red())
            emb.add_field( name = '<:warning2:779398023095648276> Ошибка:', value = 'Эти данные из википедии не найдены!' )
            await ctx.send( embed = emb, delete_after = 30 )

    @commands.command(aliases = ['userinfo', 'uinfo'])
    async def userin(self,ctx,member:discord.Member = None):
        if member == None:
            member = ctx.author
        if member.nick == None:
            nick = member.name
        else:
            nick = member.nick

        emb = discord.Embed(title = f'**Информация о {member.name}**', color= 0x2b86fd ,description = f'''
    **Никнейм на сервере:** {nick}
    **Айди:** {member.id}

    **Аватар:** [[клик]({member.avatar_url})]
    **Тег:** {member.discriminator}
    **Всего ролей:** {len(member.roles)}
    **Гл.Роль:** {member.top_role.name}
    
    **Дата создания аккаунта:** {str(member.created_at)[:16]}
    **Дата входа на сервер:** {str(member.joined_at)[:16]}
    ''')
        emb.set_thumbnail(url=member.avatar_url)
        await ctx.send(embed = emb)

    @userin.error
    async def clear_error( self, ctx, error ):
        if isinstance( error, commands.errors.MissingRequiredArgument ):
            emb = discord.Embed(colour = discord.Color.red())
            emb.add_field( name = '<:warning2:779398023095648276> Ошибка:', value = 'Использование команды: `s*userinfo [Пользователь]`' )
            await ctx.send( embed = emb, delete_after = 30 )

    @commands.command(
        aliases = ['хелп', 'помощь'],
    )
    async def help(self, ctx):

        embedhelp = discord.Embed(title=f"<:warning2:779398023095648276> Помощь",
                                  description="``` Тут вы можите посмотреть команды! ```",                                  
                                  color=0x00ff2a)
        embedhelp.add_field(name=f"Администрация", value=f" ```\n s*clear [Кол-во сообщений] - удаляет сообщения в опред-ном колич-ве \n s*mute [Пользователь] [Время] [Причина] - мутит пользователя времено \n s*unmute [Пользователь] - Размучивает пользователя  \n s*kick [Пользователь] - Кикает пользователя \n s*ban [Пользователь] - Банит пользователя \n s*report [Пользователь] [Причина] - Отправление жалобы \n s*settings - настройка под дс сервер \n s*giveaway [Время  на анг] [Приз] [Описание приза] - Конкурс на сервере \n``` ", inline=False)
        embedhelp.add_field(name=f"Информация", value=f" ```\n s*banner - Показывает баннер сервера \n s*avatar [Пользователь] - Показывает аватарку пользователя \n s*userinfo [Пользователь] - Информация  о пользователе \n s*wiki [Тема] - Информация из википедии \n s*poll [Вопрос] - голосование на сервере \n s*news [Новость] - Новости сервера через бота \n s*info - Информация о боте \n s*server - Информация о сервере \n s*roleinfo - Информация о роли \n``` ", inline=False)
        embedhelp.add_field(name=f"Разное", value=f" ```\n s*cat - Рандомный кот \n s*dog - Рандомная собака \n s*panda - Рандомная панда \n s*bird - Рандомная птица \n s*fox - Рандомная лиса \n s*koala - Рандомная коала \n s*red_panda - Рандомная красная панда \n s*anime - Рандомное аниме \n``` ", inline=False)
        embedhelp.add_field(name=f"РП-Эмоции", value=f" ```\n s*hug [Пользователь] - Обнять пользователя \n s*poke [Пользователь] - Тыкнуть пользователя \n s*pat [Пользователь] - Погладить пользователя \n s*kiss [Пользователь] - Поцеловать игрока \n``` ", inline=False)
        embedhelp.add_field(name=f"Игры", value=f" ```\n s*kubik - Рандомное число до 12 \n s*o_r - Рандом орёл или решка \n s*magicball [Вопрос] - Волшебный шар \n s*knb - игра камень/ножницы/бумага \n s*sap - игра в сапёр \n s*flags - игра в узнавание флагов \n``` ", inline=False)
        embedhelp.add_field(name=f"Музыка", value=f" ```\n s*play [Музыка] - Запуск музыки \n s*skip - Пропустить музыку \n s*stop - Остановить музыку \n s*leave - Выйти из голосового чата \n s*pause - Поставить музыку на паузу \n s*resume - Продолжить музыку \n s*queue - знать очередь \n s*song_info - Информация о музыке \n s*join - Подключение к голосовому каналу \n s*volume [1-200] - Изменить громкость \n``` ", inline=False)
        embedhelp.set_footer(text=f'Команда вызвана юзером: {ctx.author}', icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embedhelp)

def setup(client):
    client.add_cog(info(client)) 