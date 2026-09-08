# Discord bot that uses two API that gives Breaking Bad and Better Call Saul quotes
# Breaking Bad Quotes: https://breakingbadquotes.xyz/
# Better Call Saul Quotes: https://bcsquotes.shadowdev.xyz/
import os
import discord
from dotenv import load_dotenv

# Quotes requests
import requests

# Header's request
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.3"
}

def BreakingBadQuote():
    # API
    url = "https://api.breakingbadquotes.xyz/v1/quotes"
    # more quotes = https://api.breakingbadquotes.xyz/v1/quotes/5

    try:
        # API Request
        response = requests.get(url, headers=headers)
        # Response Status Code
        if response.status_code == 200:
            json_data = response.json()
            data = json_data
            return str(data[0]['quote']+'^'+data[0]['author'])
        else:
            # Error
            print("Error. Status code:", response.status_code)

    except requests.exceptions.RequestException as e:
        # Error
        print("Error:", str(e))

def BetterCallSaulQuote():
    # API
    url = "https://bcsquotes.shadowdev.xyz/api/quotes"
    # more quotes = https://bcsquotes.shadowdev.xyz/api/quotes/5

    try:
        # API Request
        response = requests.get(url, headers=headers)
        # Response Status Code
        if response.status_code == 200:
            json_data = response.json()
            data = json_data
            return str(data[0]['quote']+'^'+data[0]['author'])
        else:
            # Error
            print("Error. Status code:", response.status_code)

    except requests.exceptions.RequestException as e:
        # Error
        print("Error:", str(e))

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Bot {client.user} [READY]')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$BBquote'):
        BBq = BreakingBadQuote()
        BBquote = BBq.split('^')
        embed=discord.Embed(title=BBquote[1], description="'"+BBquote[0]+"'", color=discord.Color.green())
        await message.channel.send(embed=embed)
    if message.content.startswith('$BCSquote'):
        BCSq = BetterCallSaulQuote()
        BCSquote = BCSq.split('^')
        embed=discord.Embed(title=BCSquote[1], description="'"+BCSquote[0]+"'", color=discord.Color.yellow())
        await message.channel.send(embed=embed)
    if message.content.startswith('$help'):
        help_msg = 'Here are the commands you can use:\n👨🏻‍🦲$BBquote - Get a random Breaking Bad quote\n💼$BCSquote - Get a random Better Call Saul quote'
        embed=discord.Embed(title="Help", description=help_msg, color=discord.Color.blue())
        await message.channel.send(embed=embed)
    
client.run(TOKEN)
