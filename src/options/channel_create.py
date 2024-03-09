import discord
import random
import asyncio
import sys
from discord.ext import commands

# This might be stupid idea, might just refactor it into this file
sys.path.insert(0, './options')
from strict.channel_name_gen import name_gen

class channel_create(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
            
    # Create a single new channel
    async def create_channel_TXT(self, interaction: discord.Interaction):
        print(type(interaction))

        channel_generated_name = name_gen()
        # FIXME
        created_channel_instance = await interaction.guild.create_text_channel(channel_generated_name)
        
        embed = discord.Embed(title="Create Channel", description="")
        embed.add_field(name="", value="ChaosBot has created a new channel named " + channel_generated_name + "!")
        embed.set_thumbnail(url=self.bot.user.avatar_url)

        await interaction.response.send_message("New text channel created: " + created_channel_instance.mention)

        await created_channel_instance.send(embed=embed)


async def setup(bot):
    await bot.add_cog(channel_create(bot))

