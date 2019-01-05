import discord
import asyncio
import time
from discord.ext import commands
from itertools import cycle
from discord.utils import get

client = discord.Client()
bot = commands.Bot(command_prefix = '!')

token = 'NTIwNzA4OTMzMjQxNzk4Njc2.DvBsqg.ckPls4nvuiPVojYyjCECb5ilPaw'
bot_status = ['Game of Thrones Season 8', 'in the Tournament of Power', 'in the Timeline', 'with TTY', 'Stamprats', 'with Gaetan']

@client.event
async def on_member_join(member):
    server = member.server
    fmt = 'Welcome {0.mention} to {1.name}!'
    await client.send_message(server, fmt.format(member, server))

@client.event
async def ready():
	print('Online')

@client.event
async def on_message(message):
	if message.author == client.user:
		return
	
	if message.content.upper().startswith('!HELLO'):
		msg = 'Greetings {0.author.mention}'.format(message)
		await client.send_message(message.channel, msg)

	if 'GAETAN' in message.content.upper():
		await client.add_reaction(message, emoji=':GayBoi:481992855376887808')
		await client.add_reaction(message, emoji=':ssgaetan:508911822544306183')
		await client.add_reaction(message, emoji=':HailHydra:512376322052456458')

	if message.content.upper().startswith('!CHUNGUS'):
		await client.send_typing(message.channel)
		await client.send_message(message.channel, "https://i.imgur.com/rW8WqUA.jpg")

	if message.content.upper().startswith('!TTY'):
		await client.send_typing(message.channel)
		await client.send_message(message.channel, "TTY TTY TTY TTY TTY TTY TTYTTY", tts=True)

	if message.content.upper().startswith('!SPEAK'):
		argv = message.content.split(" ")
		await client.send_typing(message.channel)
		await client.send_message(message.channel, "%s" % (" ".join(argv[1:])),  tts=True)

	if "439110082106753024" in message.author.id:
		await client.add_reaction(message, emoji='🖕')

	if '!ANDREW' in message.content.upper():
		myid = '<@295279188334739457>'
		await client.send_typing(message.channel)
		await client.send_message(message.channel, 'Summoning %s' % myid)

	if '!AUSTIN' in message.content.upper():
		myid = '<@174695136255672322>'
		await client.send_typing(message.channel)
		await client.send_message(message.channel, 'Summoning %s' % myid)

	if '!PRANAV' in message.content.upper() or '!PRINTF' in message.content.upper():
		myid = '<@167746680656101377>'
		await client.send_typing(message.channel)
		await client.send_message(message.channel, 'Summoning %s' % myid)

	if '!WAFFLE' in message.content.upper():
		await client.send_typing(message.channel)
		await client.send_message(message.channel, "Maxence Jacques de Dixmude, the waffle himself")

	if '!NANI' in message.content.upper():
		await client.send_typing(message.channel)
		await client.send_message(message.channel, "https://gfycat.com/alarmingcreepyheifer")

	if "492499319300161536" in [role.id for role in message.author.roles] or "506338662921797635" in [role.id for role in message.author.roles]:
		if '!CLEAR' in message.content.upper():
			tmp = await client.send_message(message.channel, 'Clearing messages...')
			async for msg in client.logs_from(message.channel):
				await client.delete_message(msg)

@client.event
async def swap():
	await client.wait_until_ready()
	msgs = cycle(bot_status)

	while not client.is_closed:
		current_status = next(msgs)
		await client.change_presence(game=discord.Game(name=current_status))	
		await asyncio.sleep(30)

client.loop.create_task(swap())
client.run(token)
