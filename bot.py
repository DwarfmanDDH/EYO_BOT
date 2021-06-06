import os

from discord.ext import commands
import random
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='>')

@bot.event
async def on_ready():
    for guild in bot.guilds:
        if guild.name == GUILD:
            break
    print(f'{bot.user.name} has connected to Discord')
    print(f'{guild.name}(id: {guild.id})')


@bot.command(name="EYO", help="bot EYOss Requires admin role")
@commands.has_role('admin')
async def EYO(ctx):

    EYO = ""

    x = random.randint(1, 99)

    while x != 0:
        EYO = "o" + EYO
        x = x - 1

    x = random.randint(1, 99)

    while x != 0:
        EYO = "y" + EYO
        x = x - 1

    x = random.randint(1, 99)

    while x != 0:
        EYO = "e" + EYO
        x = x - 1


    response = EYO
    await ctx.send(response)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')

@bot.event
async def on_message(ctx):
    print(f'{message.content}')

    if message.content == "test":

        EYO = ""

        x = random.randint(1, 99)

        while x != 0:
            EYO = "o" + EYO
            x = x - 1

        x = random.randint(1, 99)

        while x != 0:
            EYO = "y" + EYO
            x = x - 1

        x = random.randint(1, 99)

        while x != 0:
            EYO = "e" + EYO
            x = x - 1


        response = EYO
        await ctx.send(response)
        print(f'{response} I said')

@bot.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise

bot.run(TOKEN)