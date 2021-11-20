import pyautogui as pg
import discord
import subprocess
import time
from discord.ext import commands

client = commands.Bot(command_prefix="d!")
screenWidth, screenHeight = pg.size()
pg.PAUSE = 0.5
with open('token.txt') as tk:
        tk421 = tk.readline()

@client.event
async def on_ready():
	print("Powered Up")

# @client.command()
# async def testmapcommand(ctx):
#         role = discord.utils.get(ctx.guild.roles, id = 749325604930977813)
#         if role in ctx.author.roles:
#                 """pg.moveTo(screenWidth/2, screenHeight/2,      duration = 1)
#                 await ctx.send("Moved Mouse!")"""
#                 r"""subprocess.call(['java', '-jar', r'C:\Users\noi01\Documents\mcaselector-1.12.3.jar'])"""
#                 pg.hotkey('win')
#                 pg.typewrite('mcaselector-1.13.3.jar', 0.03)
#                 time.sleep(0.5)
#                 pg.press('enter')
#                 await ctx.send(r"Opened C:\Users\noi01\Documents\mcaselector-1.13.3.jar")
#                 pg.keyDown('enter')
#                 time.sleep(1)
#                 pg.keyDown('ctrl')
#                 pg.press('o')
#                 pg.keyUp('ctrl')
#                 await ctx.send("Pressed Ctrl + O")
#                 pg.hotkey('alt','d')
#                 pg.typewrite(r'C:\Users\noi01\Documents\Minecraft Tools\Server migration\world\region',0.03)
#                 await ctx.send("Typed in Address Bar")
#                 pg.hotkey('enter')
#                 pg.PAUSE = 0.4
#                 pg.hotkey('tab')
#                 pg.hotkey('tab')
#                 pg.hotkey('tab')
#                 pg.hotkey('tab')
#                 pg.hotkey('tab')
#                 pg.hotkey('tab')
#                 pg.hotkey('tab')
#                 pg.PAUSE = 0.5
#                 await ctx.send("Tabbed 7 Times")
#                 pg.hotkey('enter')
#                 pg.hotkey('ctrl','shift','k')     
#                 await ctx.send("Selected World Folder and Cleared Cache")
#                 time.sleep(2)
#                 pg.hotkey('win','up')
#                 pg.hotkey('ctrl','g')
#                 pg.write('-482')
#                 pg.hotkey('tab')
#                 pg.write('98')
#                 pg.hotkey('enter')
#                 await ctx.send("Fullscreened and grabbed world coords for screenshot from MCA visualization")
#                 await ctx.send("Say :cheese:!")
#                 time.sleep(3)
#                 im = pg.screenshot('MCA.png', region=(16,54, 1850, 969))
#                 await ctx.send(":camera: Screenshot taken")
#         else:
#                 await ctx.send("You don't have permissions for this command!")
        
@client.command()
async def hello(ctx):
	await ctx.send("Hi")

@client.command()
async def map(ctx):
        role = discord.utils.get(ctx.guild.roles, id = 749325604930977813)
        if role in ctx.author.roles:
                """pg.moveTo(screenWidth/2, screenHeight/2, duration = 1)
                await ctx.send("Moved Mouse!")"""
                r"""subprocess.call(['java', '-jar', r'C:\Users\noi01\Documents\mcaselector-1.12.3.jar'])"""
                pg.hotkey('win')
                pg.typewrite('mcaselector', 0.1)
                pg.press('enter')
                time.sleep(1)
                pg.keyDown('ctrl')
                pg.press('o')
                pg.keyUp('ctrl')
                pg.hotkey('alt','d')
                pg.typewrite(r'C:\Users\derex\Documents\Server migration\ul_world_new',0.03)
                pg.hotkey('enter')
                pg.PAUSE = 0.4
                x, y = pg.locateCenterOnScreen('selectfolder.png')
                pg.click(x, y)
                pg.PAUSE = 0.5
                pg.hotkey('ctrl','shift','k')     
                time.sleep(2)
                pg.hotkey('win','up')
                pg.hotkey('ctrl','g')
                pg.write('-127')
                pg.hotkey('tab')
                pg.write('84')
                pg.hotkey('tab')
                pg.hotkey('enter')
                pg.scroll(-2)
                pg.hotkey('enter')
                pg.hotkey('ctrl','t')
                pg.hotkey('ctrl','r')
                time.sleep(3)
                im = pg.screenshot('MCA.png', region=(16,54, 1850, 969))
                pg.hotkey('alt','f4')
                time.sleep(1)
        else:
                await ctx.send("You don't have permissions for this command!")
        mcafile = discord.File("mca.png")
        ulworldfile = discord.File("ul_world.png")
        embed=discord.Embed(title="The Community", color=0xffae00)
     #   embed.set_image(url="attachment://ul_world.png")
        """embed.set_thumbnail(url="https://i.imgur.com/Hga1pAM.png")
        embed.set_image(url="http://dl.dropboxusercontent.com/s/2ezj4vckv2dzgak/ul_world.png?dl=0")"""
        mcamap=discord.Embed(title="MCA Map", color=0xffae00)
        mcamap.set_image(url="attachment://mca.png")
        """mcamap.set_image(url="http://dl.dropboxusercontent.com/s/mlzx10v8da0i0lk/mcamap.png?dl=0")"""
        await ctx.message.delete()
     #   await ctx.send(file = ulworldfile, embed=embed)
        await ctx.send(file = mcafile, embed = mcamap)

"""@client.event
async def on_message(message):
    if "hi" in message.content:
        channel = message.channel
        if channel.id == 726210665919807588 or 766382972390866944:
                if not message.author.bot:
                        await channel.send('hi')"""

client.run(tk421)
