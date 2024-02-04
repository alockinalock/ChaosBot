import discord
import random
import asyncio
from discord.ext import commands

class vc_mute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.__class__.__name__} cog loaded')

    async def mute_for_vc(self, interaction: discord.Interaction):
        users = [user for user in interaction.guild.members if not(user.bot or user == interaction.guild.owner)]

        print(users)

        if not users:
            await interaction.response.send_message("No users found")
            return

        chosen_user = random.choice(users)

        # FIXME: doesnt mute in vc or in text
        chosen_user.edit(mute=True)
        await interaction.response.send_message(f'{chosen_user.mention} has been muted.')


async def setup(bot):
    await bot.add_cog(vc_mute(bot))