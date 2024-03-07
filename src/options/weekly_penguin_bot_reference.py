import discord
import random
from discord.ext import commands
from bs4 import BeautifulSoup
import requests

class scrape_unsplash_penguins(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.url = "https://unsplash.com/s/photos/penguin?license=free"

# ------------------ backend ------------------ 

# Currently the process is to send the links
# Better idea may be to download the images to a specific folder on the bot.
    def parse_img_src_links(self):
        response = requests.get(self.url)
        content = response.content

#        blacklisted_words = ["adServer", "scorecard", "profile", "avatars"]
        whitelist = ["media.istockphoto.com", "images.unsplash.com"]

        soup = BeautifulSoup(content, 'html.parser')
        result_links = soup.find_all('img', src=True)

        # find all links with whitelisted domains
        image_links = [img_tag['src'] for img_tag in result_links if any(domain in img_tag['src'] for domain in whitelist)]

        # exclude profile pictures
        image_links = [link for link in image_links if 'profile' not in link]

        return image_links

# -----------------------------------------

# ------------------ API ------------------  

    async def send_penguin_img(self, interaction: discord.Interaction):
        peng_img_links_arr = self.parse_img_src_links()

        if len(peng_img_links_arr) == 0:
            await interaction.response.send_message("No penguins images loaded in bot")

        chosen_img_link = random.choice(peng_img_links_arr)

        await interaction.response.send_message(chosen_img_link)

# -----------------------------------------  

async def setup(bot):
    await bot.add_cog(scrape_unsplash_penguins(bot))
