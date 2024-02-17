import discord
import random
import asyncio
import os
from discord.ext import commands

class send_gif(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.__class__.__name__} cog loaded')

    # -------------------------------------------------------
    # reliant on the gifs folder actually HAVING gifs in it.
    # using tenor links may be a better option
    # -------------------------------------------------------
    async def send_gif(self, interaction: discord.Interaction):
        current_file_dir = os.path.dirname(os.path.abspath(__file__))
        gifs_dir = os.path.join(current_file_dir, "gifs")
        gif_files = [file for file in os.listdir(gifs_dir) if file.endswith(".gif")]
        #print(gif_files)

        index = random.randint(0, len(gif_files) - 1)

        if gif_files:
            chosen_gif_path = os.path.join(gifs_dir, gif_files[index])
            file = discord.File(chosen_gif_path)
            await interaction.response.send_message(file=file)
        else:
            await interaction.response.send_message("No gifs in reserve.")



async def setup(bot):
    await bot.add_cog(send_gif(bot))
