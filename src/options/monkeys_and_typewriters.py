import discord
import random
import asyncio
from discord.ext import commands

# The infinite monkey theorem states:
# A monkey hitting keys at random on a typewriter keyboard for an infinite amount of time
# will almost surely type any given text, including the complete works of William Shakespeare.
#
# We don't have time to let the monkeys write the complete works of William Shakespeare.
# Let them try to recite Hamlet from a limited dictionary... which may still take a while.
class monkeys_and_typewriters(commands.Cog):

    # TODO: pick something smaller, this quote is too long for the monkeys and it takes too much time.
    # The bot gets message limited every 5 messages about as well.
    # To be, or not to be, that is the question:
    # Whether 'tis nobler in the mind to suffer
    dict = ["to", "be", "or", "not", "that", "is", "the",
            "question", "whether", "'tis", "nobler", "in", "mind", "suffer"]

    def __init__(self, bot):
        self.bot = bot

    def __len__(self):
        return len(self.dict)

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.__class__.__name__} cog loaded')

    def format_sentence(self, sentence) -> str:
        formatted_sentence = ""
        for string in sentence :
            if string == "," or string == ":":
                formatted_sentence = formatted_sentence[:-1] + string + " "
            else:
                formatted_sentence += string + " "
        return formatted_sentence

    # TODO: break this into separate functions
    # TODO: clean this shitty code
    async def to_be_or_not_to_be(self, interaction: discord.Interaction):
        channel = interaction.channel

        embed = discord.Embed(title="Infinite Monkey Theorem", description="🐒 🐒 🐒")
        embed.add_field(name="",
                        value="The monkeys are ready to start typing on their typewriters. Good luck to them!")
        await interaction.response.send_message(embed=embed)

        sentence = []
        # What a horrible way of checking the sentence.
        final = ["to", "be", "or", "not", "to", "be", ",", "that", "is", "the", "question", ":",
                 "whether", "'tis", "nobler", "in", "the", "mind", "to", "suffer"]

        current_attempt_count = 0
        previous_random_choice_data = "" # should avoid randomly picking previous word
        while sentence != final:
            if len(sentence) == 0:
                anchor_number = self.dict.index(final[0])
            elif sentence[-1] != "," and sentence[-1] != ":":
                anchor_number = self.dict.index(final[len(sentence) - 1])
            else:
                anchor_number = self.dict.index(final[len(sentence) + 1])

            if anchor_number < 3:
                index = random.randint(anchor_number, anchor_number + 3)
            elif anchor_number > len(self.dict) - 3:
                index = random.randint(anchor_number - 3, anchor_number)
            else:
                index = random.randint(anchor_number - 3, anchor_number + 3)

            # This is random enough right
            # avoid picking wrong word thats already been picked, doesnt work
            if (self.dict[index] == previous_random_choice_data):
                if index < len(self.dict)/2:
                    index += random.randint(1, 7)
                elif index > len(self.dict)/2:
                    index -= random.randint(1, 7)
                else:
                    if random.randint(1, 2) == 1:
                        index += random.randint(1, 5)
                    else:
                        index -= random.randint(1, 5)

            # append first, ask questions later
            sentence.append(self.dict[index])

            # Could attempt to edit a single message, instead of sending a shit ton of new ones
            #await channel.send(sentence) # debug line
            await channel.send(self.format_sentence(sentence))

            # check string at the end of sentence to whatever should be in that position in final
            if sentence[len(sentence) - 1] != final[len(sentence) - 1]:
                previous_random_choice_data = sentence.pop(len(sentence) - 1)
                current_attempt_count += 1

            if current_attempt_count >= 6:
                #await channel.send("Invoking current index skip")
                current_attempt_count = 0
                sentence.append(final[len(sentence)])

            # manually adding punctuation
            if len(sentence) == 6:
                sentence.append(",")
            elif len(sentence) == 11:
                sentence.append(":")



async def setup(bot):
    await bot.add_cog(monkeys_and_typewriters(bot))
