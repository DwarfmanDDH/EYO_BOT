import os

import discord
from main import EYOrand
from dotenv import load_dotenv
import keep_alive

load_dotenv()
TOKEN = os.environ['DISCORD_TOKEN']
GUILD = os.environ['DISCORD_GUILD']
CHANNEL = os.environ['CLAN_TRIUMPHS_ID']
USERNAME = os.environ['USERNAME_CHECK']

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
#runs the local server
keep_alive.keep_alive()
#logs into discord
client.run(TOKEN)