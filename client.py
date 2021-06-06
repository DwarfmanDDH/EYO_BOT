import os

import discord
from main import EYOrand
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")
CHANNEL = os.getenv("CLAN_TRIUMPHS_ID")
USERNAME = os.getenv("USERNAME_CHECK")

client = discord.Client()

@client.event
async def on_ready():
    print(f"{client.user.name} has connected to Discord!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    #checks username of message sender
    if str(message.author.name) == USERNAME:
    #checks the message channel so it doeesn't spam all channels
        if str(message.channel.id) == CHANNEL:
    #call EYO script and uses it as the response
            response = EYOrand()
        else:
            return
    else:
        return

    await message.channel.send(response)

client.run(TOKEN)