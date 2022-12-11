import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        game = discord.Game('lol')
        await client.change_presence(status=discord.Status.online, activity=game)

    async def on_message(self, message):
        # print(f'Message from {message.author}: {message.content}')
        if message.content == "lmao" or message.content == "test":
            await message.channel.send('Hi')
        elif message.content=="哭阿":
            await message.channel.send("Never gonna give you up ~ Never gonna get you down")
        
intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('MTA0MTY4MDM3MzAxODUyOTc5Mg.G5IlUD.7ZPz4gX91AnObNQIuL5-NFCjweHQ5sXIigVSv4')