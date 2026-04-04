from discord.ext.commands import Cog, Bot, command, Context

class Admin(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

        super().__init__()
    
    @command()
    async def sync(self, ctx: Context):
        commands = await self.bot.tree.sync()
        return await ctx.reply(f"🤖 {len(commands)} synchronized commands!")

async def setup(bot: Bot):
    await bot.add_cog(Admin(bot))