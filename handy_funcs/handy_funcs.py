import discord
from random import randint
from time import sleep
import sys
import os

from botui import ButtonView, next_stage



intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
shut_status = {}
JOKES = [['ach', 'bless you'],['tank', "you're wellcome"],['weekend', 'Weekend do anything we want!'],['Radio', 'Radio not, here I come!'],['Bless', "but I didn't sneeze!"],['shore', 'shore hope you like bad jokes!'],['water', 'Water you asking so many questions for, just open up!'],['candice', 'candice joke get any worse?'],['orange', 'orange you going to let me in?'],['theodore', "theodore wasn't opened so I knocked."],['weirdo', "weirdo you think you're going?"],['fix', "fix the doorbell' I've been knocking forever! "],['disis', 'disis the police, open up!'],['I nitu', 'I nitu use the bathroom, open the door!'],['ice cream', 'ICE CREAM SO YOU CAN HEAR ME!'],['needle', 'needle little help opening the door!'],['ears', "'ears another joke for ya!"],['kanga', "actually, it's kanga-ROO!"],['howel', 'howel you know unless you open the door?'],['CD', 'CD person knocking on the door?'],['adore', 'adore is between us, so open up!'],['a little old lady', "hey, I didn't know you could yodel!"],['annie', 'annie body home?'],['boo', "don't cry, it's just a joke!"],['spell', 'okay, W-H-O!'],['double', 'W!'],['says', 'says me!'],['yurap', "no, you're a poo!"],['dejav', 'knock knock!'],['Billy Bob Joe Penny', 'really? how many billy bob joe penny do you know?'],['hawai','i am fine, how are you?']]

        
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):

    if message.author == client.user:
        return
    if message.content == "$knock_knock" or message.content == "$kk":
        await start_joke(message)
        

    if "$shut_kk" == message.content:
        if message.author.id == 801747239332610088:
            await message.delete()
            shut_status[message.author.id] = True
        
    
    
    if "$PASS1_shut_kk" == message.content:
        if message.author.id == 801747239332610088:
            if shut_status[message.author.id]:
                await message.delete()
                sys.exit()
                shut_status[message.author.id] = False
            
            
      
async def second(data_dict):
    current_stage = "second"
    data_dict["current_stage"]=current_stage
    joke = JOKES[data_dict["rand"]]
    return await data_dict["channel"].send(joke[1])

        
async def first(data_dict):
    current_stage = "first"
    data_dict["current_stage"]=current_stage
    joke = JOKES[data_dict["rand"]]
    data_dict["buttons"][current_stage]=[{
        "callback_func": next_stage,
        "label": '{} who'.format(joke[0]),
        "style": discord.ButtonStyle.blurple}]
    return await data_dict["channel"].send(joke[0], view=ButtonView(data_dict))



async def start_joke(message):
    
    author = message.author
    data_dict = {
        "current_stage": "zero",
        "message": message, 
        "channel": message.channel,
        "author": author,
        "rand":randint(0,len(JOKES)-1),
        "buttons": {"zero":[
                    {"label":"who's there?", 
                    "style":discord.ButtonStyle.primary, 
                    "callback_func":next_stage}]},
        "flow":{"zero":first,
                "first": second,
        }
    }
   
    return await data_dict["channel"].send("Knock Knock!", view=ButtonView(data_dict))

client.run('OTczMTYzODY5MDAwMzEwODM0.Ynjneg.KS_Agalpj6K1UlizFfkvGFyMdwg')
