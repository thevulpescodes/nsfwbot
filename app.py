import discord
import os
from dotenv import load_dotenv
import random

pic_ext = ['.jpg', '.png', '.jpeg', '.gif']
answers = [
    "Future Waifu",
    "HOWZIT Approved",
    "Thats your dads favorite picture too",
    "That looks like my sister",
    "My hand is going to cramp senpai",
    "uWu",
    "Dont tell the other bots Im in here",
    "Please sir, may I have another",
    "I can't believe your mom gave you these",
    "If you share more Ill eventually stop talking",
    "HOWZIT requested me to respond",
    "The curator paid me to be here",
    "Are you XP farming?"  
    ]
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_message(message):
    try:
        for ext in pic_ext:
            if message.content.endswith(ext):
                await message.channel.send(random.choice(answers))
            
            elif len(message.attachments) > 0:
                await message.channel.send(random.choice(answers))
                return
    except:
        print("Oof, tits gone wild. Something went wrong")

client.run(TOKEN)

# Made by Vulpes
