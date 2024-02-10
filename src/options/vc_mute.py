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

    # TODO: unmute someone when someone else is muted
    async def mute_for_vc(self, interaction: discord.Interaction):
        users = [user for user in interaction.guild.members if not(user.bot or user == interaction.guild.owner or user.voice is None  or user.voice.mute == True)]

        if not users:
            await interaction.response.send_message("No users in voice channels")
            return

        chosen_user = random.choice(users)

        embed = discord.Embed(title="Spam Ping", description="")
        embed.add_field(name="", value=chosen_user.mention + " is now muted")
        embed.set_thumbnail(url=chosen_user.avatar)
        await interaction.response.send_message(embed=embed)
        await asyncio.sleep(1)
        await chosen_user.edit(mute=True)


async def setup(bot):
    await bot.add_cog(vc_mute(bot))