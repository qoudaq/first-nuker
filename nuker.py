import discord
from discord.ext import commands

WEHBOOK = 'wehbook url'

client = commands.Bot(command_prefix=',', intents=discord.Intents.all())

@client.event
async def onready():
    print("bot is online")

# - - - - CHANNEL/CATEGORY DELETER/ADDER - - - - #
@client.command()
async def deletechan(ctx, channel: discord.TextChannel):
    """Deletes a specified channel."""
    await channel.delete()
    await ctx.send(f"{channel.name} **has been deleted.**")

@client.command()
async def deletecat(ctx, category: discord.CategoryChannel):
    """Deletes a specified channel."""
    await category.delete()
    await ctx.send(f"{category.name} **has been deleted.**")

# adder for category:

@client.command()
async def addcategory(ctx, category_name: str):
    """adds a specified channel."""
    guild = ctx.guild
    await guild.create_category(category_name)
    await ctx.send(f"{category_name} **has been created.**")

@client.command()
async def delcategory(ctx, channel_name: str):
    """adds a specified channel."""
    guild = ctx.guild
    await guild.delete_channel(channel_name)
    await ctx.send(f"{channel_name} **has been created.**")


# - - - - mass ban - - - - #
@client.command()
async def massban(ctx):
  """BANS NIGGAS"""
  for member in ctx.guild.members:
    try: 
      await member.ban() 
    except: 
      print("member cannot be banned")

#unban

@client.command()
async def massunban(ctx):
  """UNBANS NIGGAS"""
  for member in ctx.guild.members:
    try: 
      await member.unban() 
    except:
       print('member cant be unbanned.')

# - - - - spam messages - - - - #







# - - - - run bot - - - - #
client.run('bot token')