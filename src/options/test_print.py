import discord
from discord.ext import commands
from discord import app_commands

class cmds(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command()
    async def ping(self, interaction: discord.Interaction) -> None:
        ping1 = f"{str(round(self.bot.latency * 1000))} ms"
        embed = discord.Embed(title = "**Pong!**", description = "**" + ping1 + "**", color = 0xafdafc)
        await interaction.response.send_message(embed = embed)

async def setup(bot):
    await bot.add_cog(cmds(bot))