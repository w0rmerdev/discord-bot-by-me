#bot.py

import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

# prints the server name and server id
@client.event
async def on_ready():
  guild = discord.utils.get(client.guilds, name=GUILD)

  print(
    f'{client.user} is connected to the following guild:\n'
    f'{guild.name}(id: {guild.id}))'
  )

  #members = '\n - '.join([member.name for member in guild.members])
  #print(f'Guild Members:\n - {members}')

# sends a message in the server to welcome new members
@client.event
async def on_member_join(member):
  guild = discord.utils.get(client.guilds, name=GUILD)
  await member.create_dm()
  await member.dm_channel.send(
    f'Hi @{member.name}, welcome to {guild.id}!'
  )

'''
# says that the bot has connected to x server
class CustomClient(discord.Client):
  async def on_ready(self):
    print(f'{self.user} has connected to Discord!')

client = CustomClient()
'''

client.run(TOKEN)
