import discord
import asyncio
import time

from discord.utils import get

client = discord.Client()

token = 'NTIwNzA4OTMzMjQxNzk4Njc2.DvBsqg.ckPls4nvuiPVojYyjCECb5ilPaw'

@client.event
async def on_message(message):
#CANT TALK TO ITSELF
	if message.author == client.user:
		return

#BASIC COMMANDS
	if 'WAFFLE' in message.content.upper() or '!WAFFLE' in message.content.upper():
			await client.send_typing(message.channel)
			await client.send_message(message.channel, "Maxence Jacques de Dixmude, the waffle himself {0.author.mention}".format(message))

	if message.content.upper().startswith('!HELLO'):
		msg = 'Greetings {0.author.mention}'.format(message)
		await client.send_message(message.channel, msg)

#ADMIN COMMANDS THAT ONLY USERS IN ADMIN ROLE CAN USE
bypass_list = [""]

	if '!ANDREW' in message.content.upper():
		myid = '<@295279188334739457>'
		await client.send_message(message.channel, 'Summoning %s' % myid)

	if '!PRANAV' in message.content.upper() or '!PRINTF' in message.content.upper():
		myid = '<@167746680656101377>'
		await client.send_message(message.channel, 'Summoning %s' % myid)

	if '!AUSTIN' in message.content.upper():
		myid = '<@174695136255672322>'
		await client.send_message(message.channel, 'Summoning %s' % myid)

#TTS COMMANDS
	if message.content.upper().startswith('!TTY'):
		await client.send_message(message.channel, "TTY TTY TTY TTY TTY TTY TITTY", tts=True)

	if message.content.upper().startswith('!SPEAK'):
		argv = message.content.split(" ")
		await client.send_message(message.channel, "%s" % (" ".join(argv[1:])),  tts=True)

#EMOJI REACTION/MESSAGE COMMANDS
	if 'GAETAN' in message.content.upper():
		await client.send_typing(message.channel)
		await client.send_emoji(message.channel, ":GayBoi: :ssgaetan: :HailHydra: {0.author.mention}".format(message))
		
	if "439110082106753024" in message.author.id:
		#userid = '<@439110082106753024>'
		await client.send_typing(message.channel)
		await client.send_message(message.channel, ':middle_finger:')

	#if ':GayBoi:' in message.content:
	#	emoji = get(client.get_all_emojis(), name=':GayBoi:')
	#	await client.add_reaction(message, emoji)

client.run(token)