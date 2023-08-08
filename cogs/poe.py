from discord.ext import commands

from core.classes import Cog_Extension
from script import func


class Poe(Cog_Extension):
    @commands.command(help="Get the price of the currency")
    async def price(self, ctx, arg):
        msg = func.get_currency_price(arg)
        await ctx.channel.send(msg)

    @commands.command(help="Get the name mapping")
    async def mapping(self, ctx):
        await ctx.channel.send(func.get_map())


async def setup(bot):
    await bot.add_cog(Poe(bot))
