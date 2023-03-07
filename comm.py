import discord
from discord.ext import commands
import random

class comm(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ayuda(self, ctx):
        await ctx.send("----------COMANDOS----------"+
                       "\n$ayuda - Comandos del bot. \n$sacrificio - Un nombre al azar. \n$cointoss - Tirar una moneda. \n$melonboi - melonboi."+
                       "\n$join - El bot se une a la llamada. \n$leave - El bot sale de la llamada."+
                       "\n$play - Reproducir cancion. \n$pause - Pausar cancion. \n$resume - Resumir cancion."+
                       "\n------------------------------------")
        
    @commands.command()
    async def sacrificio(self, ctx):
        trigger_response = ["Luis Farrera", "Luis Adrian", "Eduardo", "Emmanuel", "Victor", "Guizar"]
        await ctx.send(random.choice(trigger_response))

    @commands.command()
    async def melonboi(self, ctx):
        await ctx.send("mitchiri neko march")

    @commands.command()
    async def cointoss(self, ctx):
        coin = ["Cara", "Cruz"]
        await ctx.send(random.choice(coin))
        



def setup(client):
    client.add_cog(comm(client))
