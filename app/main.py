from discord.ext.commands import Bot

class Client(Bot):
    async def setup_hook(self):
        pass

client = Client()
# client.run()