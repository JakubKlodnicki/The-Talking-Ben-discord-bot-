#######################################
#           The Talking Ben           #
#       Created by Jakub Kłodnicki     #
#               (Jacob)               #
#######################################

# pip install discord
import discord
import random

ben = ["Yes https://cdn.discordapp.com/attachments/887033566565912636/953998144268562472/yes.mp4", "No https://cdn.discordapp.com/attachments/887033566565912636/953998145317109770/no.mp4", "Ohohoohho https://cdn.discordapp.com/attachments/887033566565912636/953998144901877790/ohohoho.mp4", "Meeeeeh https://cdn.discordapp.com/attachments/887033566565912636/953998145673637929/meeeh.mp4"]

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game(name="write $help"))
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$ben '):
        await message.channel.send(random.choice(ben))

    if message.content.startswith('$author'):
        await message.channel.send('My author is giga chad Jacob')

    if message.content.startswith('$help'):
        await message.channel.send('`$ben (question) - Give question to ben`')
        await message.channel.send('`$author - Bot author`') 

client.run('Token Here')
