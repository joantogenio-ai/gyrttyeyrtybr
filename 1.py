import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send(f'Hola, soy un bot {client.user}!')
    elif  message.content.startswith('joaquin'):
         await message.channel.send(f'Hola soy tu asistente virtual!')
    elif  message.content.startswith('7548'):
         await message.channel.send(f'grfiwqygergfgew7f')
    elif  message.content.startswith('4245'):
         await message.channel.send(f'https://discord.com/channels/1502690870841839687/1502690871525642443')
    elif  message.content.startswith('$heh'):
        if len(message.content) > 4:
            count_heh = int(message.content[4:])
        else:
            count_heh = 5
        await message.channel.send("he" * count_heh)
        
        
client.run("MTUwMjY4MzM4MDU1MzIyNDIwMg.GS0_tP.3JE0T8eUoGHw2Xlhz1q-4jBHse042A7ebNACIE")