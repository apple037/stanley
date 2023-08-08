import enum

from discord.ext import commands


# Initialize the bot
class Cog_Extension(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


class Dance(enum.Enum):
    quick_sort = "Big O(nlogn)"
    bubble_sort = "Big O(N^2)"
    merge_sort = "Big O(nlogn)"
    insertion_sort = "Big O(N^2)"
    selection_sort = "Big O(N^2)"
    heap_sort = "Big O(nlogn)"
