from discord.ext import commands


# Initialize the bot
class Cog_Extension(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
