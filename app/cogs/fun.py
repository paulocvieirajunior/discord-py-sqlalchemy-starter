from discord import Interaction
from discord.app_commands import command
from discord.ext.commands import Cog, Bot

class Fun(Cog):
    def __init__(self, bot: Bot):
        super().__init__()
        
        self.bot = bot

    @command()
    async def ping(self, interaction: Interaction):
        return await interaction.response.send_message("Pong!")

async def setup(bot: Bot):
    await bot.add_cog(Fun(bot))
