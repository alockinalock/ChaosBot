import discord
import random
import asyncio
from discord.ext import commands

class spam_ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.__class__.__name__} cog loaded')

    async def spam(self, interaction: discord.Interaction):
        users = [user for user in interaction.guild.members if not(user.bot)]

        if not users:
            await interaction.response.send_message("No users found")
            return

        chosen_user = random.choice(users)
        num = random.randint(1, 25)

        channel = interaction.channel

        await interaction.response.send_message(f'{chosen_user.mention} will now be pinged {num} times')
        for i in range(num-1):
            await channel.send(chosen_user.mention)








async def setup(bot):
    await bot.add_cog(spam_ping(bot))
