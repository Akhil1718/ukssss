import discord
from discord.ext import commands
import asyncio
import time
 
bot=commands.Bot(command_prefix='*')
start=time.time()
 
@bot.event
async def on_ready():
    print('Logged in as:')
    print(bot.user.name)
    print(bot.user.id)
    print('--------------------')

   
@bot.command(pass_context=True)
async def Q1():
       
        embed=discord.Embed(title="<:emoji_52:671050824331296799>**__|I-»  ℙ𝔼𝔸𝕂 么 TRIVIA  «-I| __**", description="**Its Trivia Game Time Be Ready Guys**", color=0xFF4000)
        embed.add_field(name="**__ALL ℙ𝔼𝔸𝕂 么 TRIVIA ᴍᴇᴍʙᴇʀs__**", value="Q1. is coming on your 📳 screen", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/612849803352604673/666201723341373462/barrr.gif")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/672055096372232218/672730075799748628/PicsArt_01-31-02.38.59.gif")
        embed.set_footer(text=f"|I-» Created By AKHIL «-I|",\
        icon_url="https://i.imgur.com/ULCkgoz.jpg")
        await bot.say('@everyone',embed=embed)
        
        await msg.add_reaction("<:right:569161677862338560>")

    
        
     
        
        
@bot.command(pass_context=True)
async def Q2():
       
        embed=discord.Embed(title="<:emoji_52:671050824331296799>**__|I-»  ℙ𝔼𝔸𝕂 么 TRIVIA «-I| __**", description="**Its Trivia Game Time Be Ready Guys**", color=0xFF4000)
        embed.add_field(name="**__ALL ℙ𝔼𝔸𝕂 么 TRIVIA ᴍᴇᴍʙᴇʀs__**", value="Q2. is coming on your 📳 screen", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/612849803352604673/666201723341373462/barrr.gif")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/672055096372232218/672730075799748628/PicsArt_01-31-02.38.59.gif")
        embed.set_footer(text=f"|I-» Created By AKHIL «-I|",\
        icon_url="https://i.imgur.com/ULCkgoz.jpg")
        await bot.say('@everyone',embed=embed)

@bot.command(pass_context=True)
async def Q3():
       
        embed=discord.Embed(title="<:emoji_52:671050824331296799>**__|I-»  ℙ𝔼𝔸𝕂 么 TRIVIA  «-I|__**", description="**Its Trivia Game Time Be Ready Guys**", color=0xFF4000)
        embed.add_field(name="**__ALL ℙ𝔼𝔸𝕂 么 TRIVIA ᴍᴇᴍʙᴇʀs__**", value="Q3. is coming on your 📳 screen", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/612849803352604673/666201723341373462/barrr.gif")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/672055096372232218/672730075799748628/PicsArt_01-31-02.38.59.gif")
        embed.set_footer(text=f"|I-» Created By AKHIL «-I|",\
        icon_url="https://i.imgur.com/ULCkgoz.jpg")
        await bot.say('@everyone',embed=embed)

@bot.command(pass_context=True)
async def Q4():
       
        embed=discord.Embed(title="<:emoji_52:671050824331296799>**__|I-»  ℙ𝔼𝔸𝕂 么 TRIVIA  «-I|__**", description="**Its Trivia Game Time Be Ready Guys**", color=0xFF4000)
        embed.add_field(name="**__ALL ℙ𝔼𝔸𝕂 么 TRIVIA ᴍᴇᴍʙᴇʀs__**", value="Q4. is coming on your 📳 screen", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/612849803352604673/666201723341373462/barrr.gif")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/672055096372232218/672730075799748628/PicsArt_01-31-02.38.59.gif")
        embed.set_footer(text=f"|I-» Created By AKHIL «-I|",\
        icon_url="https://i.imgur.com/ULCkgoz.jpg")
        await bot.say('@everyone',embed=embed)

@bot.command(pass_context=True)
async def Q5():
       
        embed=discord.Embed(title="<:emoji_52:671050824331296799>**__|I-»  ℙ𝔼𝔸𝕂 么 TRIVIA  «-I|__**", description="**Its Trivia Game Time Be Ready Guys**", color=0xFF4000)
        embed.add_field(name="**__ALL ℙ𝔼𝔸𝕂 么 TRIVIA ᴍᴇᴍʙᴇʀs__**", value="Q5. is coming on your 📳 screen", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/612849803352604673/666201723341373462/barrr.gif")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/672055096372232218/672730075799748628/PicsArt_01-31-02.38.59.gif")
        embed.set_footer(text=f"|I-» Created By AKHIL «-I|",\
        icon_url="https://i.imgur.com/ULCkgoz.jpg")
        await bot.say('@everyone',embed=embed)

@bot.command(pass_context=True)
async def Q6():
       
        embed=discord.Embed(title="<:emoji_52:671050824331296799>**__|I-»  ℙ𝔼𝔸𝕂 么 TRIVIA**", description="**Its Trivia Game Time Be Ready Guys**", color=0xFF4000)
        embed.add_field(name="**__ALL ℙ𝔼𝔸𝕂 么 TRIVIA ᴍᴇᴍʙᴇʀs__**", value="Q6. is coming on your 📳 screen", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/612849803352604673/666201723341373462/barrr.gif")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/672055096372232218/672730075799748628/PicsArt_01-31-02.38.59.gif")
        embed.set_footer(text=f"|I-» Created By AKHIL «-I|",\
        icon_url="https://i.imgur.com/ULCkgoz.jpg")
        await bot.say('@everyone',embed=embed)

@bot.command(pass_context=True)
async def Q7():
       
        embed=discord.Embed(title="<:emoji_52:671050824331296799>**ℙ𝔼𝔸𝕂 么 TRIVIA**", description="**Its Trivia Game Time Be Ready Guys**", color=0xFF4000)
        embed.add_field(name="**__ALL ℙ𝔼𝔸𝕂 么 TRIVIA ᴍᴇᴍʙᴇʀs__**", value="Q7. is coming on your 📳 screen", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/612849803352604673/666201723341373462/barrr.gif")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/672055096372232218/672730075799748628/PicsArt_01-31-02.38.59.gif")
        embed.set_footer(text=f"|I-» Created By AKHIL «-I|",\
        icon_url="https://i.imgur.com/ULCkgoz.jpg")
        await bot.say('@everyone',embed=embed)

@bot.command(pass_context=True)
async def Q8():
       
        embed=discord.Embed(title="<:emoji_52:671050824331296799>**ℙ𝔼𝔸𝕂 么 TRIVIA**", description="**Its Trivia Game Time Be Ready Guys**", color=0xFF4000)
        embed.add_field(name="**__ALL ℙ𝔼𝔸𝕂 么 TRIVIA ᴍᴇᴍʙᴇʀs__**", value="Q8. is coming on your 📳 screen", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/612849803352604673/666201723341373462/barrr.gif")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/672055096372232218/672730075799748628/PicsArt_01-31-02.38.59.gif")
        embed.set_footer(text=f"|I-» Created By AKHIL «-I|",\
        icon_url="https://i.imgur.com/ULCkgoz.jpg")
        await bot.say('@everyone',embed=embed)

@bot.command(pass_context=True)
async def Q9():
       
        embed=discord.Embed(title="<:emoji_52:671050824331296799>**ℙ𝔼𝔸𝕂 么 TRIVIA**", description="**Its Trivia Game Time Be Ready Guys**", color=0xFF4000)
        embed.add_field(name="**__ALL ℙ𝔼𝔸𝕂 么 TRIVIA ᴍᴇᴍʙᴇʀs__**", value="Q9. is coming on your 📳 screen", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/612849803352604673/666201723341373462/barrr.gif")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/672055096372232218/672730075799748628/PicsArt_01-31-02.38.59.gif")
        embed.set_footer(text=f"|I-» Created By AKHIL «-I|",\
        icon_url="https://i.imgur.com/ULCkgoz.jpg")
        await bot.say('@everyone',embed=embed)

@bot.command(pass_context=True)
async def Q10():
       
        embed=discord.Embed(title="<:emoji_52:671050824331296799>**ℙ𝔼𝔸𝕂 么 TRIVIA**", description="**Its Trivia Game Time Be Ready Guys**", color=0xFF4000)
        embed.add_field(name="**ℙ𝔼𝔸𝕂 么 TRIVIA**", value="Q10. is coming on your 📳 screen", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/612849803352604673/666201723341373462/barrr.gif")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/672055096372232218/672730075799748628/PicsArt_01-31-02.38.59.gif")
        embed.set_footer(text=f"|I-» Created By AKHIL «-I|",\
        icon_url="https://i.imgur.com/ULCkgoz.jpg")
        await bot.say('@everyone',embed=embed)

@bot.command(pass_context=True)
async def loco():
       
        embed=discord.Embed(title="<:emoji_52:671050824331296799>**ℙ𝔼𝔸𝕂 么 TRIVIA**", description="**READY TO WIN LOCO GUYS**<:emoji_55:672787686230065152> ", color=0xFF4000)
        embed.add_field(name="**ℙ𝔼𝔸𝕂 么 TRIVIA**", value="**`LOCO STARTS WITHIN 5 MINUTES`**", inline=False)
        
        embed.set_image(url="https://cdn.discordapp.com/attachments/557437899294113797/626114339102916619/13-26-52-nitro_1-5.gif")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/645318717357686804/672789935530573863/gif_12-29-07.29.28.gif")
        embed.set_footer(text=f"|I-» Created By AKHIL «-I|",\
        icon_url="https://i.imgur.com/ULCkgoz.jpg")
        await bot.say('@everyone',embed=embed)

@bot.command(pass_context=True)
async def jeetoh():
        
        embed=discord.Embed(title="<:emoji_52:671050824331296799>**ℙ𝔼𝔸𝕂 么 TRIVIA**", description="**READY TO WIN JEETOH GUYS** <:emoji_54:672797311939903558>", color=0xFF4000)
        embed.add_field(name="**ℙ𝔼𝔸𝕂 么 TRIVIA**", value="**`JEETOH STARTS WITHIN 5 MINUTES`**", inline=False)
        
        embed.set_image(url="https://cdn.discordapp.com/attachments/557437899294113797/626114339102916619/13-26-52-nitro_1-5.gif")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/645318717357686804/672796068131635200/giphy_7.gif")
        embed.set_footer(text=f"|I-» Created By AKHIL «-I|",\
        icon_url="https://i.imgur.com/ULCkgoz.jpg")
        await bot.say('@everyone',embed=embed)


bot.run('Njg1NDkwOTA3NzA4OTE1NzM1.XmJfmg.DuIgU1U4CsP6UWKL9261WNQt21s')
