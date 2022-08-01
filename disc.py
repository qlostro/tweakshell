
from threading import Thread
import threading
import discord
import asyncio

from requests import delete
from feedbacks import add_feedback, rfeedbacks
import time 


client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    msg = message.content
    
    if message.author == client.user:
        return
    msg = message.content
    if msg.startswith != '!feedback' or '!old':
        def delete():
            time.sleep(2)
            message.delete()
        thr1 = threading.Thread(target=delete).start()
    if message.content.startswith('!old'):
         
        feedbac = rfeedbacks
        oldstuff = rfeedbacks()
        await message.delete()
        await message.channel.send(f'**All older feedbacks:**\n{oldstuff}', delete_after = 50)
    
    elif message.content.startswith('!feedback'):
        await message.delete()
        await message.channel.send('**To add feedback enter:** "*!addfeedback* FEEDBACK"', delete_after = 5)

    elif message.content.startswith('!addfeedback'):
        feedbac = str(msg.split("!addfeedback",1)[1])
        await message.delete()
        await message.channel.send('**Thank you for leaving feedback**\n ▀██▀─▄███▄─▀██─██▀██▀▀█\n─██─███─███─██─██─██▄█\n─██─▀██▄██▀─▀█▄█▀─██▀█\n▄██▄▄█▀▀▀─────▀──▄██▄▄█', delete_after = 5)
        userid = str(message.author.name)
        add_feedback(userid, 'DISCORD', feedbac)
    else:
        await message.delete()

client.run('MTAwMzIzMjQwMzM2OTc3MTA5OA.GoJRYJ.fUlm_HMg1lz4pOGA7QmeUWoZBO7n8lJwerrfbU')