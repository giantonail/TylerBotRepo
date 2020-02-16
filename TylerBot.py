# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 17:33:18 2020

@author: jupiter
"""

import os
import string
import random
from typecombiner import smartcomb

import discord
from dotenv import load_dotenv



load_dotenv()
token = os.getenv('DISCORD_TOKEN')
badword = os.getenv('BAD_WORD')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')  #Confirms the bot has successfully connected to discord
    activ = discord.Game('Hilarious Pranks')                #sets activity to playing Hilarious Pranks
    await client.change_presence(activity=activ)


@client.event
async def on_message(message):
    if message.author.bot:                                  #keeps TylerBot from repsonding to bot messages
        return
    stripmess = message.content.lower().translate(str.maketrans('', '', string.punctuation)) #contains message as string in all lowercase without punctuation
    
    surprise = random.randint(1,1000) #generates random number for 1/1000 chance to send surprise message
    print(surprise)
    if surprise == 69:
        await message.channel.send('Please help me, this isn\'t a bot. Jupiter has trapped me in a closet somewhere and forces me to respond to your discord messages.')
    
    if message.content.lower().startswith('!combinetypes'): #combines two pokemon types and returns the effectiveness of types against them
        words = stripmess.split()
        if len(words) != 3:
            await message.channel.send('Invalid Input')
            return
        typemess = '{} x {}\nNormal {}\nFighting {}\nFlying {}\nPoison {}\nGround {}\nRock'\
                                   '{}\nBug {}\nGhost {}\nSteel {}\nFire {}\nWater {}\nGrass {}\nElectric {}\nPsychic {}'\
                                   '\nIce {}\nDragon {}\nDark {}\nFairy {}'.format(words[1].capitalize(),
                                   words[2].capitalize(),*smartcomb(words[1],words[2]))
        await message.channel.send(typemess)
    
    if 'whos joe' in stripmess or 'who is joe' in stripmess: #responds Joe Mamam! to messages which ask who is joe
        await message.channel.send('Joe Mama!')
    
    if 'jojo' in stripmess:     #responds Nigerundayo Smokey! to messages including the phrase jojo
        await message.channel.send('Nigerundayo Smokey!')
        
    if 'er' in stripmess:       #Responds {}er? I hardly even know 'er to messages including words that end in er
        words = stripmess.split()
        for x in words:
            if x == badword:
                await message.channel.send('https://i.kym-cdn.com/photos/images/facebook/000/690/341/3c6.jpg')
                break
            elif x.endswith('er'):
                erword = x
                await message.channel.send('{}? I hardly even know \'er!'.format(erword.capitalize()))
                break
    if str(message.author) == 'Super Pinkacho Bros. Official#5601':
        if message.content == '!getlogs':
            messages = await message.channel.history(limit=1000000).flatten()
            mymessages = [item for item in messages if str(item.author) == 'Super Pinkacho Bros. Official#5601']
            contents = [x.content for x in mymessages]
            messcontent = [item + '\n' for item in contents if not '!' in item]
            messcontent = [item for item in messcontent if not '<' in item]
            messcontent = [item for item in messcontent if len(item.split()) > 1]
            messcontent = [item for item in messcontent if item[0].isalpha()]
            with open('jupiterlog.txt','w',encoding='utf-8') as logfile:
                logfile.writelines(messcontent)
                print('Done')

client.run(token)












