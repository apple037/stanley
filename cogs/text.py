import io
import os

from discord.ext import commands
from dotenv import load_dotenv

from core.classes import Cog_Extension
from script import func, common

load_dotenv()
open_api_key = os.getenv("OPENAI_API_KEY")


class Text(Cog_Extension):
    @commands.command(
        help="Use openAI chatGPT 3.5 api to achieve the chat completion"
    )
    async def ask(self, ctx, *args):
        prompt = ''
        for arg in args:
            prompt = prompt + ' ' + arg
        prompt = prompt.lstrip()
        print(prompt)
        msg = func.get_answer(prompt, open_api_key)
        await ctx.channel.send("Hi " + ctx.author.mention + " Here is my reply: \n" + msg)


async def setup(bot):
    await bot.add_cog(Text(bot))
