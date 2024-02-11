import discord
import random
import asyncio
import turtle
import os
import uuid

from discord.ext import commands

class draw(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def random_draw(self):
        turtle.speed(10)



    async def draw_something(self, interaction: discord.Interaction):
        unique_identifier = str(uuid.uuid4())[:8]



async def setup(bot):
    await bot.add_cog(draw(bot))


if __name__ == "__main__":
    turtle.speed(10)
    turtle.left(100)
