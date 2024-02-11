import discord
import random
import asyncio
from discord.ext import commands

class nickname_change(commands.Cog):

    # Vulgar I know, but we have to make these presets.
    # TODO: find a better way of generating these nick names
    possible_names = ["piss baby", "shit head", "gargle nuts", "thing 1", "dumb bitch"]

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.__class__.__name__} cog loaded')

    async def change_user_nickname(self, interaction: discord.Interaction):
        users = [user for user in interaction.guild.members if not (user.bot or user == interaction.guild.owner)]

        if not users:
            await interaction.response.send_message("No users found")

        chosen_user = random.choice(users)

        embed = discord.Embed(title="Nickname Change", description="")
        embed.add_field(name="", value=chosen_user.mention + " has a new nickname! Go took a look.")
        embed.set_thumbnail(url=chosen_user.avatar)
        await interaction.response.send_message(embed=embed)

        chosen_nickname = random.choice(self.possible_names)
        await chosen_user.edit(nick=chosen_nickname)



async def setup(bot):
    await bot.add_cog(nickname_change(bot))
