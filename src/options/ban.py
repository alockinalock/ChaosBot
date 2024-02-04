import discord
import random
import asyncio
from discord.ext import commands

class ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.__class__.__name__} cog loaded')

    # TODO: implement actual ban
    async def ban(self, interaction: discord.Interaction):

        users = [user for user in interaction.guild.members if not (user.id == self.bot.user.id or user.bot)]

        if not users:
            await interaction.response.send_message("No users can be banned.")
            return

        chosen_user = random.choice(users)

        embed = discord.Embed(title="Ban", description="")
        embed.add_field(name="", value=chosen_user.mention + " has been chosen to be banned.")
        embed.add_field(name="Countdown", value="3", inline=False) # TODO: edit this field for ther countdown
        embed.set_thumbnail(url=chosen_user.avatar)
        await interaction.response.send_message(embed=embed)



async def setup(bot):
    await bot.add_cog(ban(bot))
