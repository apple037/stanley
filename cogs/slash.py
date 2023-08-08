import discord
from discord import app_commands

from core.classes import Cog_Extension, Dance


class Slash(Cog_Extension):
    @app_commands.command(name="hello", description="Hello world!")
    async def hello(self, interaction: discord.Interaction):
        await interaction.response.send_message("Hello " + interaction.user.mention)

    @app_commands.command(name="dance", description="你還能起舞嗎?")
    @app_commands.describe(dance='Which dance style do you like?')
    async def dance(self, interaction: discord.Interaction, dance: Dance):
        await interaction.response.send_message("You can really dance " + dance.name + " Style!" + "\n" + "The dance steps are: " + dance.value)


async def setup(bot):
    await bot.add_cog(Slash(bot))
