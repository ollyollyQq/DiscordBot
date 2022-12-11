import discord
client = discord.Client()

async def on_ready(client):
    print('Login As：', client.user)
    game = discord.Game('lol')
    await client.change_presence(status=discord.Status.online, activity=game)

async def on_message(message):
    if message.author == client.user:
        return
    if message.content == "test" or message.content == "Test":
        await message.channel.send('Hi')
    if message.content == 'ping':
        await message.channel.send('pong')

client.run("MTA0MTY4MDM3MzAxODUyOTc5Mg.G5IlUD.7ZPz4gX91AnObNQIuL5-NFCjweHQ5sXIigVSv4")