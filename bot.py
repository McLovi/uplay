import discord
from discord.ext import commands
from discord.ext.commands import Bot
import random
import discord
import time
import asyncio

client = discord.Client()

start_time = {"start_time1": time.time()}

cooldown_time = 3600

@client.event
async def on_ready():
    print('Eingeloggt als')
    print(client.user.name)
    print(client.user.id)
    print('-----------')
    await bot.change_presence(game=discord.Game(name='Type $uplay'))


@client.event
async def on_message(message):
    start_time["start_time1"] = time.time()


async def cooldown():
    await client.wait_until_ready()

    while not client.is_closed:
        await asyncio.sleep(1)

        if time.time() >= start_time["start_time1"] + cooldown_time:
            for server in client.servers:
                await client.send_message(server.default_channel, "Hallo, noch jemand da?")

client.loop.create_task(cooldown())

Client = discord.Client()
bot = commands.Bot(command_prefix="$")
lines = open(r'spotify.txt').read().splitlines()
   
    
@bot.command(pass_context=True)
async def uplay(ctx):
    userName = ctx.message.author.name
    userID = ctx.message.author.id

    if ctx.message.server:
        myline = random.choice(lines)
        split = myline.partition(":")
       
        embed=discord.Embed(title="Spotify Account", color=0xf45eff)
        embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQQ9lEkpFJyS4zJJtyvgqmTR7NoR4-Wg3BaOSmQbDZInmOtxvz6MA")
        embed.add_field(name="Email:", value=split[0], inline=False)
        embed.add_field(name="Password:", value=split[2], inline=False)
        await bot.send_message(ctx.message.author, embed=embed)

        print("{} Typed $uplay".format(userName))
        
      @bot.command(pass_context=True)
async def invite(ctx):
    '''Invite the bot to your server'''
    await ctx.send(
       "Invite me to your server: https://discordapp.com/oauth2/authorize?client_id=384044025298026496&scope=bot&permissions=268905542"
    )
        
        client = discord.Client()

bot.run("NDcyMzU0NjA0ODMxNzM1ODE4.Dj3LlQ.Uq7P7i9IaSZ7fNBocU0-_za1tbM")
