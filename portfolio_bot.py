import discord
import asyncio
import time
from discord.ext import commands
from itertools import cycle
from discord.utils import get

client = discord.Client()

bot_status = ['!help', 'Game of Thrones Season 8', 'in the Tournament of Power', 'in the Timeline', 'with TTY', 'Stamprats', 'with Gaetan']

owner_id = "506338662921797635"
admin_id = "492499319300161536"
kike_id = "506329003225907211"
pow_id = ["536351163105411072"]
chat_filter = ["!CHUNGUS", "!CLEAR", "!TTY", "!SPEAK", "!PRANAV", "!PRINTF", "!AUSTIN", "!ANDREW", "!WAFFLE", "!NANI"]
bypass_list = ["492499319300161536", "506338662921797635", "506329003225907211"]

""" @client.event
async def mem_status(stat):
	if str(stat.discord.status) == "online":
		if () """

@client.event
async def on_member_join(member):
	POW = discord.utils.get(member.server.roles, name='POWs')
	server = member.server
	fmt = 'Welcome {0.mention} to {1.name}!'
	await client.add_roles(member, POW)
	await client.send_message(server, fmt.format(member, server))

@client.event
async def ready():
	await print('Online')

@client.event
async def on_message(message):
#this checks if a command is used and if used by someone not in the bypass list, del
	contents = message.content.split(" ")
	for word in contents:
		if word.upper() in chat_filter:
			if not roles.id in bypass_list:
				try:
					await client.delete_message(message)
					await client.send_message(message.channel, "You need to have your role changed from POW to use commands")
				except discord.errors.NotFound:
					return

	if not pow_id in [role.id for role in message.author.roles]:
		if message.author == client.user:
			return

		if message.content.upper().startswith('!INVITE'):
			await client.send_message(message.author, "https://discord.gg/mC72hrr")

		if message.content.upper().startswith('!HELP'):
			embed = discord.Embed(
				color = discord.Colour.orange()

			)
			embed.set_author(name='Help - The Commands for the 42 Portfolio Project Bot')
			embed.add_field(name='!HELLO', value='Test command, says hello to the user', inline=False)
			embed.add_field(name='!CHUNGUS', value='Posts the big chungus meme', inline=False)
			embed.add_field(name='!TTY', value='Spams a TTS voice saying TTY', inline=False)
			embed.add_field(name='!SPEAK', value='Replacement TTS discord builtin command', inline=False)
			embed.add_field(name='!PRANAV/ANDREW/AUSTIN', value='Summons specified user', inline=False)
			embed.add_field(name='!WAFFLE', value='Funny command about my great friend Maxence', inline=False)
			embed.add_field(name='!NANI', value='Laser eyes Steve Harvey gif', inline=False)
			embed.add_field(name='!CLEAR', value='Deletes all messages in a channel, admin only ;)', inline=False)
			await client.send_message(message.author, embed=embed)

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

		if "171328042763812864" in message.author.id:
			await client.add_reaction(message, emoji=':cuck:525077184424181760')

		if message.content.upper().startswith('!ANDREW'):
			myid = '<@295279188334739457>'
			await client.send_typing(message.channel)
			await client.send_message(message.channel, 'Summoning %s' % myid)

		if message.content.upper().startswith('!AUSTIN'):
			myid = '<@174695136255672322>'
			await client.send_typing(message.channel)
			await client.send_message(message.channel, 'Summoning %s' % myid)

		if message.content.upper().startswith('!PRANAV') or message.content.upper().startswith('!PRINTF'):
			myid = '<@167746680656101377>'
			await client.send_typing(message.channel)
			await client.send_message(message.channel, 'Summoning %s' % myid)

		if message.content.upper().startswith('!WAFFLE'):
			await client.send_typing(message.channel)
			await client.send_message(message.channel, "Maxence Jacques de Dixmude, the waffle himself")

		if message.content.upper().startswith('!NANI'):
			await client.send_typing(message.channel)
			await client.send_message(message.channel, "https://gfycat.com/alarmingcreepyheifer")

#this might need to be deleted due to overlapping with the chat filter
	elif message.content.upper().startswith('!') and pow_id in [role.id for role in message.author.roles]:
		await client.send_typing(message.channel)
		await client.send_message(message.channel, "You don't have permissions to use that comamnd")

	if admin_id in [role.id for role in message.author.roles] or owner_id in [role.id for role in message.author.roles]:
		if message.content.upper().startswith('!CLEAR'):
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
		await asyncio.sleep(1)

client.loop.create_task(swap())
client.run(token)
