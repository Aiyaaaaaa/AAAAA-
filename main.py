#import Discord package
import discord
import os
from discord.ext import commands
from keep_alive import keep_alive
#Client (my bot)

client = discord.Client()

client = commands.Bot(command_prefix=',')

@client.command(name='version')
async def version(context):

# DO STUFF.....

@client.event
async def on_ready():
    print("Bot Is Ready And Online!")

@client.event    
async def react(message): 
    if message.content == "Meeting":
        await message.add_reaction("👍")

@bot.command()
async def info(ctx):
    await ctx.send("Hello, thanks for testing out our bot. ~ techNOlogics")

@bot.command(pass_context=True)
async def meet(ctx,time):
    if ctx.message.author.name == "techNOlogics":
        await ctx.channel.purge(limit=1)
        await ctx.send("**Meeting at " + time + " today!** React if you read.")

 ##THIS ONE HOLDS UP THE WHOLE SCRIPT
async def on_message(message):
    await react(message)

# Run the client on the server
keep_alive()
client.run(os.getenv("TOKEN"))