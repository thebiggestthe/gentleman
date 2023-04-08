import discord
from discord.ext import commands


class PingCommand(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("pong")


async def setup(client):
    await client.add_cog(PingCommand(client))
