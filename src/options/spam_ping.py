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
        num = random.randint(5, 25)

        channel = interaction.channel

        embed = discord.Embed(title="Spam Ping", description="")
        embed.add_field(name="", value=chosen_user.mention + " will now be pinged " + str(num) + " times.")
        embed.set_thumbnail(url=chosen_user.avatar)
        await interaction.response.send_message(embed=embed)

        await asyncio.sleep(1)

        for i in range(num):
            await channel.send(chosen_user.mention)


async def setup(bot):
    await bot.add_cog(spam_ping(bot))
