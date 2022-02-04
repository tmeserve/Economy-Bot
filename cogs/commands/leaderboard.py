from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from constants import get_database, get_collection

class Leaderboard(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.database = get_database()
        self.collection = get_collection()

    @cog_ext.cog_slash(name="leaderboard")
    async def _leaderboard(self, ctx: SlashContext):
        return

def setup(bot):
    bot.add_cog(Leaderboard(bot))