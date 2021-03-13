import discord
from discord.ext import commands
from discord.ext import tasks
import string
import random
import asyncio

client = commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
    print('Bot is ready')

@client.event
async def on_ready():
    print('Bot is ready')
    #setting `playing ` status
    await client.change_presence(activity=discord.Game(name=".commands " f"| watching {len(client.guilds)} servers"))



#commands
@client.command()
async def commands(ctx):
        await ctx.send("This command is for help! All the commands that this bot can do will be listed here.\n \n **commands** - Gives the command list.\n **botlink** - Gives the bot link! \n **bananalink** - Gives the link to the discord.\n **rltournaments** - Gives the time for rocket league tournaments! \n **mainlink** - Gives the link to the main discord!")


@client.command()
async def bananalink(ctx):
        await ctx.send("**https://bit.ly/2NejhAy**")

@client.command()
async def mainlink(ctx):
    await ctx.send("**https://bit.ly/2OKjID0**")

@client.command()
async def rltournaments(ctx):
    await ctx.send("**9 AM PST**\n**3 PM PST**\n**6 PM PST**\n**9 PM PST**")

@client.command()
async def botlink(ctx):
    await ctx.send("**https://bit.ly/3cquVRl**")





client.run('ODE5NzUyMTU3ODMzMDY4NTk2.YErLsA.wZW2H8L1A1VL2mpgo8TbN43x1pQ')
