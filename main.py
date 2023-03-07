import discord
from discord.ext import commands
import music, comm


cogs = [music, comm]

client = commands.Bot(command_prefix='$', intents = discord.Intents.all())

@client.event
async def on_ready():
    print("The bot is now ready for use!")
    print("------------------------------")

for i in range(len(cogs)):
    cogs[i].setup(client)


client.run("OTQ5MTg2NzQ0NzY5NzE2MjY0.YiGtCg.edTnAUBN-FzIbitFsXSesydtp9E")
