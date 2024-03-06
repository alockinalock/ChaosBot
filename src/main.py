import discord
import os
import asyncio

from dotenv import load_dotenv
# 'app_commands' may be redundant
from discord import app_commands
from discord.ext import commands

load_dotenv()
token = os.getenv("token")

bot = commands.Bot(command_prefix='cb!', intents = discord.Intents.all())

@bot.event
async def on_ready():
    print(f"{bot.user} is online: All command types enabled")
    try:
        # ensure this statement is printed or else COGS dont work
        print(f"Loaded {len(await bot.tree.sync())} command(s).")
    except Exception as error:
        print(error)


    # load all cogs in the options directory
    current_working_directory = os.path.dirname(os.path.abspath(__file__))
    extension_directory = "options"
    target_directory = os.path.join(current_working_directory, extension_directory)
    extension_files = [file for file in os.listdir(target_directory) if file.endswith(".py")]

    for file in extension_files:
        file_name = file[:-3]
        full_extension_file_path = f"{extension_directory}.{file_name}"
        await bot.load_extension(full_extension_file_path)


async def larger_num_of_reactions(ctx: discord.Interaction):
    # TODO: maybe provide a countdown for this
    await asyncio.sleep(15)

    # returns a discord.InteractionMessage object
    interactionMessageObject = await ctx.original_response()

    # returns a discord.Message object
    messageObject = await interactionMessageObject.fetch()
    highest_reaction_symbol = ""
    highest_reaction_number = 0
    for reaction in messageObject.reactions:
        if (reaction.count-1) > highest_reaction_number:
            highest_reaction_number = reaction.count-1
            highest_reaction_symbol = reaction.emoji

    # send msg w/o interaction
    id = interactionMessageObject.channel.id
    channel = bot.get_channel(id)

    # TODO: invoke the actual chaos sequence
    await channel.send(f"{highest_reaction_symbol} wins with {highest_reaction_number} vote(s)!")

@bot.tree.command(name="chaos", description="Are you sure about this?")
async def start_chaos_sequence(interaction: discord.Interaction):
    # send an embed
    user_invoke = interaction.user.mention
    embedVar = discord.Embed(title="", description=user_invoke + " wants to invoke the Chaos Sequence. Waiting for majority vote for permission.", color=0x00ff00)
    embedVar.add_field(name="Protocol 0x0001", value="React with green or red to either: permit the Chaos Sequence; forbid the Chaos Sequence.", inline=False)
    await interaction.response.send_message(embed=embedVar)

    # emoji reactions to embed
    msg = await interaction.original_response()
    await msg.add_reaction("🟩")
    await msg.add_reaction("🟥")
    await larger_num_of_reactions(interaction)

# temporary methods
@bot.tree.command(name="bantest")
async def ban_test(interaction: discord.Interaction):
    test = bot.get_cog('ban')
    if test is not None:
        await test.ban(interaction)

@bot.tree.command(name="spampingtest")
async def spam_ping_test(interaction: discord.Interaction):
    test = bot.get_cog('spam_ping')
    if test is not None:
        await test.spam(interaction)

@bot.tree.command(name="mutevctest")
async def ban_test(interaction: discord.Interaction):
    test = bot.get_cog('vc_mute')
    if test is not None:
        await test.mute_for_vc(interaction)

@bot.tree.command(name="monkeytest")
async def monkeytypewriter_test(interaction: discord.Interaction):
    test = bot.get_cog('monkeys_and_typewriters')
    if test is not None:
        await test.to_be_or_not_to_be(interaction)

@bot.tree.command(name="nicktest")
async def nickname_changer_test(interaction: discord.Interaction):
    test = bot.get_cog('nickname_change')
    if test is not None:
        await test.change_user_nickname(interaction)

@bot.tree.command(name="giftest")
async def gif_test(interaction: discord.Interaction):
    test = bot.get_cog('send_gif')
    if test is not None:
        await test.send_gif(interaction)

@bot.tree.command(name="channel_create_test")
async def create_channel_test(interaction: discord.Interaction):
    test = bot.get_cog("channel_create")
    if test is not None:
        await test.create_channel_test(interaction)

if __name__ == "__main__":
    print(f"Booting up {bot.user}: All command types enabled.")
    bot.run(token)

# Would be preferable if mute and ban had unban/unmute waves as functions.
