import discord
import asyncio
import config

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    messageLower = message.content.lower()
    authorid = message.author.id
    if message.author == client.user:
        return
    elif 'left leg next week' in messageLower:
        userFile = open(f'{authorid}.txt', 'w')
        userFile.write('left leg')
        userFile.close()
        await message.channel.send('I got ya')
    elif 'right leg next week' in messageLower:
        userFile = open(f'{authorid}.txt', 'w')
        userFile.write('right leg')
        userFile.close()
        await message.channel.send('I got ya')
    elif 'which leg' in messageLower:
        userFile = open(f'{authorid}.txt', 'r')
        toSend = userFile.readline()
        await message.channel.send(toSend)
    elif 'good bot' in messageLower:
        await message.channel.send('😊')

client.run(config.token)