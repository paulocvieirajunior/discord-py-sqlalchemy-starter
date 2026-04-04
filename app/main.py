from core import settings

from discord import Intents
from discord.ext.commands import Bot

from os import listdir

class Client(Bot):
    async def _load_cogs(self):
        for cog in listdir("app/cogs"):
            if cog.endswith(".py"):
                await self.load_extension(f"cogs.{cog[:-3]}")

    async def setup_hook(self):
        await self._load_cogs()

    async def on_ready(self):
        print(f"🚀 Bot started as {self.user}")

intents = Intents.all()
client = Client(command_prefix="$", intents=intents, owner_id=settings.OWNER_ID)

client.run(settings.BOT_TOKEN)