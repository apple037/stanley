import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

from core.classes import Cog_Extension

load_dotenv()
open_api_key = os.getenv("OPENAI_API_KEY")
sd_url = os.getenv("STABLE_DIFFUSION_URL")
replicate_api_key = os.getenv("REPLICATE_API_KEY")


class Main(Cog_Extension):

    @commands.command(help="Greetings")
    async def greet(self, ctx):
        await ctx.channel.send("Greeting! " + ctx.author.mention)

    @commands.command(help="Fuck GGC")
    async def fuck(self, ctx):
        msg = "{0} minds your own business".format(str(ctx.author))
        await ctx.channel.send(msg)
        sta = self.bot.Game('fuck')
        await self.bot.change_presence(status=self.bot.Status.idle, activity=sta)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        await ctx.send(f"An error occured: {str(error)}")
        await ctx.send(file=discord.File(fp='./resource/no.jpeg', filename='no.jpeg'))

    # github link
    @commands.command(help="Get the github link")
    async def github(self, ctx):
        link = discord.Embed()
        link.description = "Link: [here](https://github.com/apple037/stanley)"
        await ctx.channel.send(embed=link)


async def setup(bot):
    await bot.add_cog(Main(bot))
