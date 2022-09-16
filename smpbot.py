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
                time.sleep(1)

                #lower section
                pg.hotkey('ctrl','g')
                pg.write('-127')
                pg.hotkey('tab')
                pg.write('750')
                pg.hotkey('tab')
                pg.hotkey('enter')
                pg.scroll(-2)
                pg.hotkey('enter')
                time.sleep(3)
                im2 = pg.screenshot('MCA2.png', region=(16,54, 1850, 969))
                time.sleep(1)

                #upper section
                pg.hotkey('ctrl','g')
                pg.write('-127')
                pg.hotkey('tab')
                pg.write('-500')
                pg.hotkey('tab')
                pg.hotkey('enter')
                pg.scroll(-2)
                pg.hotkey('enter')
                time.sleep(3)
                im3 = pg.screenshot('MCA3.png', region=(16,54, 1850, 969))
                pg.hotkey('alt','f4')
                time.sleep(1)
        else:
                await ctx.send("You don't have permissions for this command!")
                
        mcafile = discord.File("mca.png")
        ulworldfile = discord.File("ul_world.png")
        embed=discord.Embed(title="The Community", color=0xffae00)
        mcamap=discord.Embed(title="MCA Map", color=0xffae00)
        mcamap.set_image(url="attachment://mca.png")
        await ctx.message.delete()
        await ctx.send(file = mcafile, embed = mcamap)
        
        mcafile = discord.File("mca2.png")
        embed=discord.Embed(title="Upper Section", color=0xffae00)
        mcamap=discord.Embed(title="Northern Section", color=0xffae00)
        mcamap.set_image(url="attachment://mca1.png")
        await ctx.send(file = mcafile, embed = mcamap)

        mcafile = discord.File("mca3.png")
        embed=discord.Embed(title="Upper Section", color=0xffae00)
        mcamap=discord.Embed(title="Lower Section", color=0xffae00)
        mcamap.set_image(url="attachment://mca2.png")
        await ctx.send(file = mcafile, embed = mcamap)

client.run(tk421)
