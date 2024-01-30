import discord
import os

from dotenv import load_dotenv
# May be redundant
from discord import app_commands
from discord.ext import commands

load_dotenv()
token = os.getenv("token")

bot = commands.Bot(command_prefix='cb!', intents = discord.Intents.all())

@bot.event
async def on_ready():
    print(f"{bot.user} is online: All command types enabled")
    try:
        print(f"Loaded {len(await bot.tree.sync())} command(s).")
    except Exception as error:
        print(error)

@bot.tree.command(name="chaos", description="Are you sure about this?")
async def start_chaos_sequence(interaction: discord.Interaction):
    await interaction.response.send_message(f"{interaction.user.mention} wants to evoke the Chaos Sequence. Waiting for a majority vote.")

if __name___ == "__main__":
    print(f"Booting up {bot.user}: All command types enabled.")
    bot.run(token)