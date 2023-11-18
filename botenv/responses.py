# responses.py

from discord.ext import commands

class Responses(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name='hello', help='Say hello to the bot.')
    async def hello_command(self, ctx):
        await ctx.send('Hello!')

def setup(client):
    client.add_cog(Responses(client))


    

