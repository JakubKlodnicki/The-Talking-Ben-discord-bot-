#######################################
#           The Talking Ben           #
#       Created by Jakub Kłodnicki     #
#               (Jacob)               #
#######################################

# pip install discord
import discord
import random

ben = ["Yes", "No", "Ohohoohho", "eeeeeh"]

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game(name="write $help"))
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$ben'):
        await message.channel.send(random.choice(ben))

    if message.content.startswith('$author'):
        await message.channel.send('My author is giga chad Jacob')

    if message.content.startswith('$help'):
            await message.channel.send('`$ben (question) - Give question to ben`')
            await message.channel.send('`$author - Bot author`') 

client.run('Token here')
