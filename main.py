import discord
from discord.ext import commands
import music

cogs = [music]

client = commands.Bot(command_prefix='?', intents = discord.Intents.all())

for i in range(len(cogs)):
    cogs[i].setup(client)


client.run("OTU5OTIzNDcwNjYwMTU3NDUw.Yki8ZQ.EH-CNM8Xv8ixeQndL-hQ1cogVJU")