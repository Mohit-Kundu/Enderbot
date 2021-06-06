import discord
import os
import requests
from discord.ext import commands

#dont change a thing
client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
  print('{0.user} logged in...'.format(client))

@client.command()
async def mineserver(ctx, arg):
  response = requests.get('http://api.minehut.com/server/' + arg +
  '?byName=true')
  json_data = response.json()

  #print(json_data)

  server_name = json_data['server']['name']
  online = str(json_data['server']['online'])
  playerCount = str(json_data['server']['playerCount'])
  maxPlayers = str(json_data['server']['maxPlayers'])
  serverPlan = json_data['server']['server_plan']
  platform = json_data['server']['platform']

  server_embed = discord.Embed(
    title = server_name + " Server Info:",
    color = discord.Color.dark_green()
  )

  server_embed.set_thumbnail(url = 'https://art.pixilart.com/d27785b85783e97.png')

  server_embed.add_field(name = 'Online: ', value = online, inline = False)
  server_embed.add_field(name = 'Players Online: ', value = playerCount, inline = True)
  server_embed.add_field(name = 'Max Occupancy: ', value = maxPlayers, inline = True)
  server_embed.add_field(name = 'Server Plan: ', value = serverPlan, inline = False)
  server_embed.add_field(name = 'Platform:' , value = platform , inline = True)

  await ctx.send(embed = server_embed)

#Saving a location
@client.command()
async def minelocation(ctx, name, x, y):
  pin_name = name;
  coordinates = {'X':x, 'Y':y}

  pin_embed = discord.Embed(
    title = pin_name + " coordinates:",
    color = discord.Color.gold()
  )
  pin_embed.set_thumbnail(url = 'https://apprecs.org/gp/images/app-icons/300/4b/com.elderapps.mctorch.jpg')

  pin_embed.add_field(name = "x: ", value = coordinates['X'], inline = True)
  pin_embed.add_field(name = "y: ", value = coordinates['Y'], inline =  True)
  )

  await ctx.author.send(embed = pin_embed)

client.run(os.getenv('TOKEN'))