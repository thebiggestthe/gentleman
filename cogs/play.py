from disnake.ext import commands

class PlayCommand(commands.Cog):

    def __init__(self, client):
        self.client = client

def setup(client):
    client.add_cog(PlayCommand(client))