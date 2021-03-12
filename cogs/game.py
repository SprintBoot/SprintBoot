import discord
from discord.ext import commands
from discord.utils import get
from discord.ext.commands import Bot 

import json
import random
import asyncio
import requests
import datetime

kybe = ["1","2","3","4","5","6","7","8","9","10","11","12"]

class game(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.cog_name = ["игры"]

    @commands.command(
        aliases=['кубик'],
        )
    async def kubik(self, ctx):
        kuboid = random.choice(kybe)
        embedkub = discord.Embed(title=" Игра в кубик", color=0x00ff00)
        embedkub.add_field(name="<:Kube:782300085819539456> Вам выпало:", value=kuboid, inline=False)
        await ctx.send(embed=embedkub)

    @commands.command(
        aliases=['монетка', 'орел_решка','о_р','орёл_решка'],
        description='Бот подбрасывает монетку',
        usage='монетка'
    )
    async def o_r(self, ctx):
        robot = ["орёл", "решка"]
        robot_choice = random.choice(robot)
                                   
        emb = discord.Embed(title="Орел или решка", colour=discord.Colour.red(), timestamp=ctx.message.created_at)
        emb.set_footer(text='Команда вызвана: {}'.format(ctx.author.name), icon_url=ctx.author.avatar_url)
                                   
        if robot_choice == "орёл":
            emb.add_field(name="Подбрасываем монетку....", value="**Орёл** <:coin:779788586358407178> ")

        if robot_choice == "решка":
            emb.add_field(name="Подбрасываем монетку....", value="**Решка** <:coin:779788586358407178> ")

        await ctx.send(embed=emb)
                                   
    @commands.command( 
        name = "волшебный шар", # Имя комманды
        description='Игра в волшебный шар',
        aliases = ["шар", "magicball"], # Обходы на комманду
        usage='шар [вопрос]'
    )
    async def eightball(self, ctx):
        answers = [
            "🧊 Несомненно! 🕯️",
            "🧊 Можете быть уверены! 🕯️",
            "🧊 Сомневаюсь в этом... 🕯️",
            "🧊 Спроси позже... 🕯️"
        ] # Тут наши ответы, сюда можно добавить ещё

        embed = discord.Embed(
            title = "🔮 Магический шар 🧙‍♀️", # Верхняя часть (название) эмбеда
            description = random.choice(answers), # Описание, где будет наш ответ, который подберется через random
            color = 0x00ff2a # Цвет эмбеда
        )

        await ctx.send(embed = embed) # Ну тут всё ясно, отправка самого эмбеда

    @commands.command()
    async def knb(self,ctx):
        num = 0
        embed = discord.Embed(title = 'Суефа',description = '''Сделайте ход!
🗿 - камень
📜 - бумага
✂ - ножницы''',
        color=0x00ff2a)
        mess = await ctx.send(embed = embed)
        await mess.add_reaction('✂')
        await mess.add_reaction('🗿')
        await mess.add_reaction('📜')
        try:
            def check(reaction,user):
                if reaction.message == mess:
                    return user == ctx.author and reaction.emoji in '🗿📜✂'
            reaction,user = await self.client.wait_for('reaction_add', timeout=60.0, check=check)
        except:
            await mess.delete()
        if reaction.emoji == '🗿':
            num = 1
            await mess.delete()
        if reaction.emoji == '📜':
            num = 2
            await mess.delete()
        if reaction.emoji == '✂':
            num = 3
            await mess.delete()
        if num != 0:
            num2 = random.randint(1,3)
            nums = {1:'🗿',2:'📜',3:'✂'}
            a = nums[num2]
            if num == num2:
                victory = 'Ничья'
            if num == 1 and num2 == 2:
                victory = self.client.user.mention
            if num == 2 and num2 == 1:
                victory = ctx.author.mention
            if num == 2 and num2 == 3:
                victory = self.client.user.mention
            if num == 3 and num2 == 2:
                victory = ctx.author.mention
            if num == 3 and num2 == 1:
                victory = self.client.user.mention
            if num == 1 and num2 == 3:
                victory = ctx.author.mention
            embed = discord.Embed(title = 'Суефа',description = f'''
-Ваш ход: {reaction.emoji}
-Ход бота: {a}
-Победитель: {victory}
''',
            color=0x00ff2a)
            await ctx.send(embed = embed)

    @commands.command()
    async def sap(self, ctx):

        r_list = ['🟩', '🟧', '🟥']

        msg = await ctx.send(f'Выберете сложность :\n\n{r_list[0]}— Easy\n{r_list[1]}— Medium\n{r_list[2]}— Hard')
        for r in r_list:
            await msg.add_reaction(r)
        try:
            react, user = await self.client.wait_for('reaction_add', timeout=30.0, check=lambda react,
                                                                                             user: user == ctx.author and react.message.channel == ctx.channel and react.emoji in r_list)
        except Exception:
            await msg.delete()
        else:
            if str(react.emoji) == r_list[0]:
                columns = 4
                rows = 4
                await msg.clear_reactions()
            elif str(react.emoji) == r_list[1]:
                columns = 8
                rows = 8
                await msg.clear_reactions()
            elif str(react.emoji) == r_list[2]:
                columns = 12
                rows = 12
                await msg.clear_reactions()
            else:
                await msg.delete()
                await ctx.send('Неверная реакция!', delete_after=10.0)

        bombs = columns * rows - 1
        bombs = bombs / 2.5
        bombs = round(random.randint(5, round(bombs)))

        columns = int(columns)
        rows = int(rows)
        bombs = int(bombs)

        grid = [[0 for num in range(columns)] for num in range(rows)]

        loop_count = 0
        while loop_count < bombs:
            x = random.randint(0, columns - 1)
            y = random.randint(0, rows - 1)

            if grid[y][x] == 0:
                grid[y][x] = 'B'
                loop_count = loop_count + 1

            if grid[y][x] == 'B':
                pass

        pos_x = 0
        pos_y = 0
        while pos_x * pos_y < columns * rows and pos_y < rows:

            adj_sum = 0

            for (adj_y, adj_x) in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]:

                try:
                    if grid[adj_y + pos_y][adj_x + pos_x] == 'B' and adj_y + pos_y > -1 and adj_x + pos_x > -1:
                        adj_sum = adj_sum + 1
                except Exception as error:
                    pass

            if grid[pos_y][pos_x] != 'B':
                grid[pos_y][pos_x] = adj_sum

            if pos_x == columns - 1:
                pos_x = 0
                pos_y = pos_y + 1
            else:
                pos_x = pos_x + 1

        not_final = []

        for the_rows in grid:
            not_final.append(''.join(map(str, the_rows)))

        not_final = '\n'.join(not_final)

        not_final = not_final.replace('0', '||:zero:||')
        not_final = not_final.replace('1', '||:one:||')
        not_final = not_final.replace('2', '||:two:||')
        not_final = not_final.replace('3', '||:three:||')
        not_final = not_final.replace('4', '||:four:||')
        not_final = not_final.replace('5', '||:five:||')
        not_final = not_final.replace('6', '||:six:||')
        not_final = not_final.replace('7', '||:seven:||')
        not_final = not_final.replace('8', '||:eight:||')
        final = not_final.replace('B', '||:bomb:||')

        percentage = columns * rows
        percentage = bombs / percentage
        percentage = 100 * percentage
        percentage = round(percentage, 2)

        emb = discord.Embed(
            description=final,
            color=0xC0C0C0
        )
        emb.add_field(
            name='Кол-во столбцов :',
            value=columns,
            inline=True
        )
        emb.add_field(
            name='Кол-во строк:',
            value=rows,
            inline=True
        )
        emb.add_field(
            name='Всего клеток :',
            value=columns * rows,
            inline=True
        )
        emb.add_field(
            name='Кол-во бомб:',
            value=bombs,
            inline=True
        )

        await msg.edit(embed=emb, content=None)

    @commands.command(
        aliases=["флаги", "flags"],
        description="Сыграть в угадывания флагов стран",
        usage="флаги"
    ) # создаём команду
    async def _флаги(self, ctx): # функцию
        event_members = {} # создаём словарь, он нужен для того, чтобы подсчитывать баллы каждого участника игры
        with open('./Data/DataBase/flags.json','r',encoding='utf8') as f: # открываем файл с кодировкой utf8, чтобы всё было ок
            flags = json.load(f) # превращаем в словарь
            count = 1 # подсчёт раундов
            flags_list = [] # создаётся список, в который будут добавляться названия флагов, для того чтобы потом при помощи проверки не допускать повторов в игре
            while count <= 10:# всего 10 раундов, Вы можете изменить это значение
                otvet = random.choice(flags['Флаги']) # выбираем рандомный флаг, который скинет бот и будет ожидать ответа к нему (всё из файла flags.json)
                if otvet in flags_list: # проверка, был ли этот флаг уже в списке или нет
                    pass
                elif otvet not in flags_list: # проверка, срабатывающая, когда флага в списке нет
                    flags_list.append(otvet) # добавляет флаг в список, чтобы потом при проверке избежать повторов
                    e = discord.Embed(title = f"Флаг {count}") # создаём эмбед, с названием "Флаг №", на месте номера будет число раунда
                    e.set_image(url = otvet['url']) # ставит изображение, взяв ссылку из файла flags.json
                    await ctx.send(embed = e) # отправляет эмбед
                    def check(m):
                        return m.content.lower() == otvet['answer'].lower() and m.channel == ctx.channel

                    msg = await self.client.wait_for('message', check=check) # ожидает ответа
                    if str(msg.author.id) not in event_members: # проверка на то, есть ли автор ответа в нашем созданном ранее словаре, если нет то заносит и даёт количество очков 1
                        event_members[str(msg.author.id)] = {} # заносим в словарь
                        event_members[str(msg.author.id)]["score"] = 1 # количество очков задаём
                    elif str(msg.author.id) in event_members: # если автор ответа уже есть в ранее созданном словаре - срабатывает эта проверка
                        event_members[str(msg.author.id)]["score"] += 1 # добавляет 1 очко
                    em = discord.Embed(title = "Правильный ответ!") # создаём эмбед, который говорит о том что был правильный ответ
                    em.add_field(name = "Ответил:", value = f"{msg.author.mention}") # кто ответил
                    em.add_field(name = "Правильный ответ:",value = f"{otvet['answer']}") # какой правильный ответ
                    await ctx.channel.send(embed = em) # отправляет
                    count = count + 1 # следующий раунд
                    await asyncio.sleep(1) # ждём, чтобы всё слишком быстро не было
                    if count == 11: # если так называемый 11 раунд (конец по умолчанию) то эта проверка срабатывает
                        e = discord.Embed(title = "Конец игры!", description = f"Таблица лидеров:") # создаёт эмбед с таблицой участников, и их баллами
                        leaders = sorted(event_members, key=lambda score: event_members[score]['score'], reverse=True) # сортирует словарь по ключу score (очки)
                        position = 1 # начинаем с 1 чела в таблице
                        for leader in leaders: # создаём цикл для перебора словаря
                            leader = self.client.get_user(int(leaders[position-1])) # получаем человека
                            leader_score = event_members[str(leader.id)]['score'] # получаем очки этого человека
                            e.add_field(name=f"{position} место:", value=f"{leader.mention} | очки: **{leader_score}**",inline=False) # заносим в его нашу таблицу
                            position += 1 # строчка, чтобы далее перебирать всех
                        await ctx.send(embed = e) # отправляет эмбед объявляя конец
                        return # конец, ценок!  
        
def setup(client):
    client.add_cog(game(client))
