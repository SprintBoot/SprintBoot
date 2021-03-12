import discord
from discord.ext import commands
from discord.utils import get
from pymongo import MongoClient
import time
import asyncio
import os 
import datetime

cluster = MongoClient("mongodb+srv://SprintBoot:Avakum132@sprintboot.kghvy.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
collection = cluster.settings.settinglogs

class logs(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.cog_name = ["Логи!"]



def setup(client):
    client.add_cog(logs(client)) 