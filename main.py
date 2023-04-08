import os
import json
import asyncio

import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.presences = True

client = commands.Bot(intents=intents, command_prefix='>')

with open('data/token.json') as f:
    token_dic = json.load(f)


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("What are you saying, homie?")


async def load_cogs():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await client.load_extension(f'cogs.{filename[:-3]}')


token = token_dic["default"]
print("starting...")

asyncio.run(load_cogs())
client.run(token)
