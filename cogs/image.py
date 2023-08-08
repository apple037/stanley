import io
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

from core.classes import Cog_Extension
from script import func, common

load_dotenv()
sd_url = os.getenv("STABLE_DIFFUSION_URL")
replicate_api_key = os.getenv("REPLICATE_API_KEY")


class Image(Cog_Extension):
    @commands.command(help="Get the server information of the Stable Diffusion")
    async def info(self, ctx):
        sd_info = await func.sd_info(sd_url)
        await ctx.channel.send("Hi " + ctx.author.mention + " " + sd_info)

    @commands.command(help="Generate image with the corresponding prompt")
    async def image(self, ctx, *args):
        prompt = ''
        for arg in args:
            prompt = prompt + ' ' + arg
        prompt = prompt.lstrip()
        # print(prompt)
        await ctx.channel.send("Image generating ..." + ctx.author.mention + " please wait patiently!")
        img = await func.generate_image(prompt, sd_url)
        img_buffer = io.BytesIO()
        img.save(img_buffer, format='PNG')
        img_buffer.seek(0)
        await ctx.channel.send("Hi " + ctx.author.mention + "The image generated with the "
                                                            "corresponding prompts (" +
                               prompt + ") is below:",
                               file=discord.File(fp=img_buffer, filename='image.png'))

    @commands.command(help="Use BLIP2 to perform image to text conversion")
    async def img2txt(self, ctx, arg):
        # 檢查是否為有效的url
        if not common.is_valid_url(arg):
            await ctx.channel.send(ctx.author.mention + " the input: " + arg + " is not a valid url")
        await ctx.channel.send("Image to text converting ..." + ctx.author.mention + " please wait patiently!")
        parsed_text = await func.img2txt(arg, replicate_api_key)
        await ctx.channel.send("Hi " + ctx.author.mention + "The text generated with the "
                                                            "corresponding image (" +
                               arg + ") is below: " + "\n" + parsed_text)

    # Get a random cat image
    @commands.command(help="Get a random cat image")
    async def cat(self, ctx):
        await ctx.channel.send("Cat image generating ..." + ctx.author.mention + " please wait patiently!")
        img = await func.random_cat()
        img_buffer = io.BytesIO()
        img.save(img_buffer, format='PNG')
        img_buffer.seek(0)
        await ctx.channel.send("Hi " + ctx.author.mention + "The cat image generated is below:",
                               file=discord.File(fp=img_buffer, filename='cat.png'))


async def setup(bot):
    await bot.add_cog(Image(bot))
