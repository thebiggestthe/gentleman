import disnake
from disnake.ext import commands

import youtube_dl
import asyncio

class PingCommand(commands.Cog):
    def __init__ (self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command()
    async def ping(self, inter: disnake.ApplicationCommandInteraction):
        """Get the bot's current websocket latency."""
        await inter.response.send_message(f"Pong! {round(self.bot.latency * 1000)}ms")

class PlayCommand(commands.Cog):
    def __init__ (self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command()
    async def play(self, inter: disnake.ApplicationCommandInteraction):
        """Play Youtube Video"""
        await inter.response.send_message("Playing")

def setup(client):
    client.add_cog(PingCommand(client))