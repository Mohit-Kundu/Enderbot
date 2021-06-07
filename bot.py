import discord
import os
import requests
from discord.ext import commands
    
class Enderbot(commands.Bot):
    
    def __init__(self, command_prefix, self_bot):
        commands.Bot.__init__(self, command_prefix=command_prefix, self_bot=self_bot)
        self.add_commands() 
    
    async def on_ready(self):
        print('Enderbot is online...')
    
    #add_commands is used to pass self to user defined commands
    def add_commands(self):

        #Lets user know if server is online and also returns server info
        @self.command(name = "ping", pass_context = True)
        async def ping(ctx, arg):
          response = requests.get('http://api.minehut.com/server/' + arg + '?byName=true')

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
          server_embed.add_field(name = 'Platform:' , value = platform , inline = False)

          await ctx.send(embed = server_embed)
    
        #Saving a location
        @self.command(name = 'pin', pass_context = True)
        async def pin(ctx, name, x, y):
          loc_name = name;
          coordinates = {'X':x, 'Y':y}

          loc_embed = discord.Embed(
            title = loc_name + " coordinates:",
            color = discord.Color.gold()
          )
          loc_embed.set_thumbnail(url = 'https://apprecs.org/gp/images/app-icons/300/4b/com.elderapps.mctorch.jpg')

          loc_embed.add_field(name = "x: ", value = coordinates['X'], inline = True)
          loc_embed.add_field(name = "y: ", value = coordinates['Y'], inline =  True)

          await ctx.author.send(embed = loc_embed)

if __name__ == '__main__':
  bot = Enderbot(command_prefix="?", self_bot=False)
  bot.run(os.getenv("TOKEN"))
