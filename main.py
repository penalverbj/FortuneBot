import discord
import os 
import requests
import json

client = discord.Client()

def get_fortune():
	fortune = requests.get("https://zenquotes.io/api/random")
	json_data = json.loads(fortune.text)
	quote = json_data[0]['q'] + " -" + json_data[0]['a']
	return quote

@client.event
async def on_ready():
	print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
	if message.author == client.user:
		return
	
	if message.content.startswith('+f'):
		f = get_fortune()
		await message.channel.send(f);	

client.run(os.getenv('TOKEN'));