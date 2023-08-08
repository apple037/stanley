import enum

from discord.ext import commands


# Initialize the bot
class Cog_Extension(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


class Dance(enum.Enum):
    quick_sort = 'quick_sort'
    merge_sort = 'merge_sort'
    bubble_sort = 'bubble_sort'
    insertion_sort = 'insertion_sort'
    selection_sort = 'selection_sort'
    heap_sort = 'heap_sort'
