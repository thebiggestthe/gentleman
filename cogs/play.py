import disnake
import wavelink
from disnake.ext import commands

class PlayCommand(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def play(self, ctx, *, search: str) -> None:
        """Simple play command."""

        if not ctx.voice_client:
            vc: wavelink.Player = await ctx.author.voice.channel.connect(cls=wavelink.Player)
        else:
            vc: wavelink.Player = ctx.voice_client

        track = await wavelink.YouTubeTrack.search(search, return_first=True)
        await vc.play(track)


    @commands.command()
    async def disconnect(self, ctx) -> None:
        """Simple disconnect command.

        This command assumes there is a currently connected Player.
        """
        vc: wavelink.Player = ctx.voice_client
        await vc.disconnect()

def setup(client):
    client.add_cog(PlayCommand(client))