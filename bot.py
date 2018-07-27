import discord
from discord.ext import commands
from discord.ext.commands import Bot
import random

Client = discord.Client()
bot = commands.Bot(command_prefix="<")
lines = open(r'spotify.txt').read().splitlines()

@bot.event
async def on_ready():
    print('The bot is online!')
    await bot.change_presence(game=discord.Game(name='Type <uplay'))
   
    
@bot.command(pass_context=True)
async def spotify(ctx):
    userName = ctx.message.author.name
    userID = ctx.message.author.id

    if ctx.message.server:
        myline = random.choice(lines)
        split = myline.partition(":")
       
        embed=discord.Embed(title="Uplay Account", color=0xf45eff)
        embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQQ9lEkpFJyS4zJJtyvgqmTR7NoR4-Wg3BaOSmQbDZInmOtxvz6MA.png")
        embed.add_field(name="Email:", value=split[0], inline=False)
        embed.add_field(name="Password:", value=split[2], inline=False)
        await bot.send_message(ctx.message.author, embed=embed)

        print("{} Typed <spotify".format(userName))

        client = discord.Client()

bot.run("NDcyMzQyOTIzMzU5NDIwNDE2.Djx_Mg.mxPJVnByXsr69854PnIW0ZBf2_o")
