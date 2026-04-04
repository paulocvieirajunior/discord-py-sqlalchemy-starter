from core import settings
from discord import Intents
from discord.ext.commands import Bot

class Client(Bot):
    async def setup_hook(self):
        pass

intents = Intents.all()
client = Client(command_prefix="$", intents=intents)

client.run(settings.BOT_TOKEN)