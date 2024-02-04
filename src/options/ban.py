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

    async def ban(self, interaction: discord.Interaction):

        users = [user for user in interaction.guild.members if not (user.bot or user == interaction.guild.owner)]

        if not users:
            await interaction.response.send_message("No users found")
            return

        chosen_user = random.choice(users)

        embed = discord.Embed(title="Ban", description="")
        embed.add_field(name="", value=chosen_user.mention + " has been chosen to be banned.")
        embed.add_field(name="Countdown", value="3", inline=False)
        embed.set_thumbnail(url=chosen_user.avatar)
        await interaction.response.send_message(embed=embed)

        message = await interaction.original_response()

        # edit the message for a countdown
        embed.set_field_at(index=1, name="Countdown", value="2", inline=False)
        await asyncio.sleep(1)
        await message.edit(embed=embed)
        embed.set_field_at(index=1, name="Countdown", value="1", inline=False)
        await asyncio.sleep(1)
        await message.edit(embed=embed)
        embed.set_field_at(index=1, name="Countdown", value="0", inline=False)
        await asyncio.sleep(1)
        await message.edit(embed=embed)

        channel = interaction.channel
        #await chosen_user.ban(reason="")
        await channel.send(f'{chosen_user.mention} has been banned.')




async def setup(bot):
    await bot.add_cog(ban(bot))
