import discord
from discord import app_commands

from core.classes import Cog_Extension, Dance


def get_step(dance):
    if dance in ("quick_sort", "merge_sort", "selection_sort", "heap_sort", "insertion_sort"):
        return "BigO(nlogn)"
    elif dance in "bubble_sort":
        return "BigO(n^2)"


class Slash(Cog_Extension):
    @app_commands.command(name="hello", description="Hello world!")
    async def hello(self, interaction: discord.Interaction):
        await interaction.response.send_message("Hello " + interaction.user.mention)

    @app_commands.command(name="dance", description="你還能起舞嗎?")
    @app_commands.describe(dance='Which dance style do you like?')
    async def dance(self, interaction: discord.Interaction, dance: Dance):
        await interaction.response.send_message(
            "You can really dance " + dance.value + " Style!" + "\n" + "The dance steps are: " + get_step(dance.value))


async def setup(bot):
    await bot.add_cog(Slash(bot))
