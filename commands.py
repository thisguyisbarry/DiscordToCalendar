from dotenv import load_dotenv
import os 
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

    if message.content.casefold().startswith('cringe'):
        await message.channel.send('Nyaa~ uwu')

    if message.content.casefold().startswith('mew'):
        await message.channel.send('/ᐠ. ｡.ᐟ\\\ᵐᵉᵒʷˎˊ˗')

    if message.content.casefold().contains('bonk'):
        await message.channel.send('<:opalBonk:1055507310526599198>')

load_dotenv()
token = (os.environ.get('BOT_AUTH_TOKEN'))
client.run(token)