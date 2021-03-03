import discord
import os
import requests
import json

client = discord.Client()


def get_fortune():
	link = "https://fortuneapi.herokuapp.com/"
	html = requests.get(link).text
	l = list(html)
	for i in range(0, len(l) - 1):
		if (l[i] == '\\' and l[i+1] == 'n'):
			l[i] = ' '
			l[i+1] = ''
	return "".join(l)

def get_quote():
	line = requests.get("https://zenquotes.io/api/random")
	json_data = json.loads(line.text)
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
  	await message.channel.send(f)
	
  elif message.content.startswith('+q'):
    q = get_quote()
    await message.channel.send(q)
	


client.run(os.getenv('TOKEN'))
