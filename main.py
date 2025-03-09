import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the bot token from the environment variable
TOKEN = os.getenv("BOT_TOKEN")

# Enable message content intent explicitly
intents = discord.Intents.default()
intents.message_content = True

# Create a bot instance with the command prefix 'prefix'
bot = commands.Bot(command_prefix="prifix", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

bot.run(TOKEN)
