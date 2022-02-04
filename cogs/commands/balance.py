from asyncio import constants
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from constants import get_database, get_collection

class Balance(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.database = get_database()
        self.collection = get_collection()

    @cog_ext.cog_slash(name="balance", guild_ids=[937826820106125362])
    async def _balance(self, ctx: SlashContext):
        # ctx.
        return

def setup(bot):
    bot.add_cog(Balance(bot))