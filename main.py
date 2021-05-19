import discord
from discord.ext import commands
import asyncio, random, os, requests, sys, threading, datetime, json, aiohttp
from urllib import parse
import re, time
from colorama import Fore
import os 
import time 
import halo

from discord.ext import commands

prefix = (".")


RICHY = discord.Client()
RICHY = commands.Bot(description='RICHY Selfbot', command_prefix=prefix, self_bot=True)





RICHY.remove_command('help')





@RICHY.command()
async def help(ctx):
    await ctx.message.delete()
    embed = discord.Embed(color=0)
    embed.set_author(name='RICHY SELFBOT')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/767242291794280449/841290264845090816/image0.gif')
    embed.set_footer(text='Created by RICHY')
    embed.add_field(name='**TEXT**', value='```THIS COMMAND DISPLAYS TEXT COMMANDS```')
    embed.add_field(name='**NUKE**', value='```THIS COMMAND DISPLAYS NUKE COMMANDS```')
    embed.add_field(name='**UTILITY**', value='```THIS COMMAND SHOWS ALL THE MAJOR COMMANDS IN THE SELFBOT```')
    embed.add_field(name='**FUN**', value='```THIS COMMAND DISPLAYS FUN COMMANDS```')
    embed.add_field(name='**HELP**', value='```THE COMMAND DISPLAYS help commands```')
    embed.add_field(name='**UPTIME**', value='```THIS COMMAND SHOWS RUNNING TIME OF THE SELFBOT```')
    embed.add_field(name='**HELPHACK**', value='```shows hack commands```')
    embed.add_field(name='important info',value='```THIS SELFBOT IS UNDER DEVELOPMENT! so if you face any problem , dm me on instagram <3 instagram id - _jotarokujo_123```')
    await ctx.send(embed=embed) 
    
   
@RICHY.command()
async def helphack(ctx):
    embed = discord.Embed(color=0)
    embed.set_author(name='RICHY SELFBOT')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/767242291794280449/841290264845090816/image0.gif')
    embed.set_footer(text='Created by RICHY')
    embed.add_field(name='.helphack', value='```Shows Help Cmds```')
    embed.add_field(name='.text', value='```Shows Text Cmds```')
    embed.add_field(name='.hack', value='```Shows hack Cmds```')
    embed.add_field(name='.helpnuke', value='```Shows nuke Cmds```')
    embed.add_field(name='.misc', value='```Shows misc Cmds```')
    await ctx.send(embed=embed)

@RICHY.command(pass_context=True)
async def hack(ctx):
    embed = discord.Embed(color=0)
    embed.set_author(name='RICHY SELFBOT | HACK CMDS')
    embed.set_footer(text='Created by RICHY')
    embed.add_field(name='>ip', value='```Displays info on an IP \nParameters- >ip <target> \nEx- >ip 162.159.128.233```')
    embed.add_field(name='>doxuser', value='```Displays info on a user | Only works in a server\nParameters- >doxuser <@target> \nEx- >doxuser @RICHY#9999```')
    embed.add_field(name='>doxtoken', value='```Displays info on a Discord Account \nParameters- >tdox <target-token> \nEx- >tdox mfa.W3Di4FprRZ_AXH_Y5-A9ReoshSu9Dzn_fTXrvBhwc6p3LvkYLJM4jbr338YUMZ7ECnj2zbxnKm-I2ReFh2Zp```')
    embed.add_field(name='>doxserver', value='```Displays info on a Discord Server\nParameters- >doxserver\nEx- >doxserver```')
    embed.add_field(name='>pingweb', value='```Pings the website to check whether its operational or not.\nParameters- >pingweb <website url>\nEx- >pingweb https://discord.com/```')
    embed.add_field(name='>getroles', value='```Sends all roles of a server which you dont have the perm to view | Note - Use a spam channel.\nParameters- >getroles\nEx- >getroles```')
    await ctx.send(embed=embed)
    
@RICHY.command(pass_context=True)
async def misc(ctx):
    embed = discord.Embed(color=0)
    embed.set_author(name='RICHY SELFBOT | MISC CMDS')
    embed.set_footer(text='Created by RICHY')
    embed.add_field(name='>renameserver', value='```Renames the server name\nParameters- >renameserver <name>\nEx- >renameserver RICHY GOD```')
    await ctx.send(embed=embed)
    
@RICHY.command()
async def spam(ctx, amount: int, *, message):
    for _i in range(amount):
        await ctx.send(message)

RICHY.command(aliases=['trash', 'wizz'])
async def trash(ctx):
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
            pass

    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            pass

    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass

    try:
        await ctx.guild.edit(name='RICHY TRASHED THIS SERVER',
          description='RICHY got no chill',
          reason='ripped by RICHY',
          icon=None,
          banner=None)
    except:
        pass

    for _i in range(100):
        await ctx.guild.create_text_channel(name='richy runs you')

    for _i in range(100):
        await ctx.guild.create_role(name='RICHY fucked you', color=(RandomColor()))
  
@RICHY.command(aliases=['whois'])
async def doxuser(ctx, member: discord.Member=None):
    if not member:
        member = ctx.message.author
    roles = [role for role in member.roles]
    embed = discord.Embed(colour=(discord.Colour.default()), timestamp=(ctx.message.created_at), title=f"User Info - {member}")
    embed.set_thumbnail(url=(member.avatar_url))
    embed.set_footer(text='Created By RICHY')
    embed.add_field(name='ID:', value=(member.id))
    embed.add_field(name='Display Name:', value=(member.display_name))
    embed.add_field(name='Created Account On:', value=(member.created_at.strftime('%a, %#d %B %Y, %I:%M %p UTC')))
    embed.add_field(name='Joined Server On:', value=(member.joined_at.strftime('%a, %#d %B %Y, %I:%M %p UTC')))
    embed.add_field(name='Roles:', value=(''.join([role.mention for role in roles])))
    embed.add_field(name='Highest Role:', value=(member.top_role.mention))
    print(member.top_role.mention)
    await ctx.send(embed=embed)

@RICHY.command()
async def uptime(ctx):
    embed = discord.Embed(color=0)
    embed.set_author(name='RICHY SELFBOT')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/767242291794280449/841290264845090816/image0.gif')
    embed.set_footer(text='Created by RICHY')
    embed.add_field(name='UPTIME', value='```coming soon```')
    await ctx.send(embed=embed)
    
    
@RICHY.command()
async def helptext(ctx):
    embed = discord.Embed(color=0)
    embed.set_author(name='RICHY SELFBOT')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/767242291794280449/841290264845090816/image0.gif')
    embed.set_footer(text='Created by RICHY')
    embed.add_field(name='**TEXT**', value='**text commands**')
    embed.add_field(name='**.spam**', value='```Example : .spam 3 richy```')
    embed.add_field(name='**.purge**', value='```deletes the messages```')
    embed.add_field(name='**.embed**', value='```convert the text into embed```')
    embed.add_field(name='**.firstmsg**', value='```jumps to first message```')
    await ctx.send(embed=embed)

@RICHY.command()
async def purge(ctx, amount: int=None):
    if amount is None:
        async for message in ctx.message.channel.history(limit=999).filter(lambda m: m.author == RICHY.user).map(lambda m: m):
            try:
                await message.delete()
            except:
                pass

    else:
        async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == RICHY.user).map(lambda m: m):
            try:
                await message.delete()
            except:
                pass

@RICHY.command(name='first-message',
  aliases=['firstmsg', 'fm', 'firstmessage'])
async def _first_message(ctx, channel: discord.TextChannel=None):
    if channel is None:
        channel = ctx.channel
    first_message = (await channel.history(limit=1, oldest_first=True).flatten())[0]
    embed = discord.Embed(description=(first_message.content))
    embed.add_field(name='First Message',
      value=f"[Click here to Jump]({first_message.jump_url})")
    embed.set_footer(text='Created by RICHY')
    await ctx.send(embed=embed)

@RICHY.command()
async def funhack(ctx, user: discord.Member = None):
    await ctx.message.delete()
    gender = ["Male", "Female", "Trans", "Other", "Retard"]
    age = str(random.randrange(10, 25))
    height = [
        '4\'6\"', '4\'7\"', '4\'8\"', '4\'9\"', '4\'10\"', '4\'11\"', '5\'0\"',
        '5\'1\"', '5\'2\"', '5\'3\"', '5\'4\"', '5\'5\"', '5\'6\"', '5\'7\"',
        '5\'8\"', '5\'9\"', '5\'10\"', '5\'11\"', '6\'0\"', '6\'1\"', '6\'2\"',
        '6\'3\"', '6\'4\"', '6\'5\"', '6\'6\"', '6\'7\"', '6\'8\"', '6\'9\"',
        '6\'10\"', '6\'11\"'
    ]
    weight = str(random.randrange(60, 300))
    hair_color = ["Black", "Brown", "Blonde", "White", "Gray", "Red"]
    skin_color = ["White", "Pale", "Brown", "Black", "Light-Skin"]
    religion = [
        "Christian", "Muslim", "Atheist", "Hindu", "Buddhist", "Jewish"
    ]
    sexuality = [
        "Straight", "Gay", "Homo", "Bi", "Bi-Sexual", "Lesbian", "Pansexual"
    ]
    education = [
        "High School", "College", "Middle School", "Elementary School",
        "Pre School", "Retard never went to school LOL"
    ]
    ethnicity = [
        "White", "African American", "Asian", "Latino", "Latina", "American",
        "Mexican", "Korean", "Chinese", "Arab", "Italian", "Puerto Rican",
        "Non-Hispanic", "Russian", "Canadian", "European", "Indian"
    ]
    occupation = [
        "Retard has no job LOL", "Certified discord retard", "Janitor",
        "Police Officer", "Teacher", "Cashier", "Clerk", "Waiter", "Waitress",
        "Grocery Bagger", "Retailer", "Sales-Person", "Artist", "Singer",
        "Rapper", "Trapper", "Discord Thug", "Gangster", "Discord Packer",
        "Mechanic", "Carpenter", "Electrician", "Lawyer", "Doctor",
        "Programmer", "Software Engineer", "Scientist"
    ]
    salary = [
        "Retard makes no money LOL", "$" + str(random.randrange(0, 1000)),
        '<$50,000', '<$75,000', "$100,000", "$125,000", "$150,000", "$175,000",
        "$200,000+"
    ]
    location = [
        "Retard lives in his mom's basement LOL", "America", "United States",
        "Europe", "Poland", "Mexico", "Russia", "Pakistan", "India",
        "Some random third world country", "Canada", "Alabama", "Alaska",
        "Arizona", "Arkansas", "California", "Colorado", "Connecticut",
        "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois",
        "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine",
        "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi",
        "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire",
        "New Jersey", "New Mexico", "New York", "North Carolina",
        "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania",
        "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas",
        "Utah", "Vermont", "Virginia", "Washington", "West Virginia",
        "Wisconsin", "Wyoming"
    ]
    email = [
        "@gmail.com", "@yahoo.com", "@hotmail.com", "@outlook.com",
        "@protonmail.com", "@disposablemail.com", "@aol.com", "@edu.com",
        "@icloud.com", "@gmx.net", "@yandex.com"
    ]
    dob = f'{random.randrange(1, 13)}/{random.randrange(1, 32)}/{random.randrange(1950, 2021)}'
    name = [
        'James Smith', "Michael Smith", "Robert Smith", "Maria Garcia",
        "David Smith", "Maria Rodriguez", "Mary Smith", "Maria Hernandez",
        "Maria Martinez", "James Johnson", "Catherine Smoaks", "Cindi Emerick",
        "Trudie Peasley", "Josie Dowler", "Jefferey Amon", "Kyung Kernan",
        "Lola Barreiro", "Barabara Nuss", "Lien Barmore", "Donnell Kuhlmann",
        "Geoffrey Torre", "Allan Craft", "Elvira Lucien", "Jeanelle Orem",
        "Shantelle Lige", "Chassidy Reinhardt", "Adam Delange", "Anabel Rini",
        "Delbert Kruse", "Celeste Baumeister", "Jon Flanary", "Danette Uhler",
        "Xochitl Parton", "Derek Hetrick", "Chasity Hedge",
        "Antonia Gonsoulin", "Tod Kinkead", "Chastity Lazar", "Jazmin Aumick",
        "Janet Slusser", "Junita Cagle", "Stepanie Blandford", "Lang Schaff",
        "Kaila Bier", "Ezra Battey", "Bart Maddux", "Shiloh Raulston",
        "Carrie Kimber", "Zack Polite", "Marni Larson", "Justa Spear"
    ]
    phone = f'({random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)})-{random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)}-{random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)}'
    if user is None:
        user = ctx.author
        password = [
            'password', '123', 'mypasswordispassword', user.name + "iscool123",
            user.name + "isdaddy", "daddy" + user.name, "ilovediscord",
            "i<3discord", "furryporn456", "secret", "123456789", "apple49",
            "redskins32", "princess", "dragon", "password1", "1q2w3e4r",
            "ilovefurries"
        ]
        message = await ctx.send(f"`Hacking {user}...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...`"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\n`"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...`"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...\nFinalizing life-span dox details\n`"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"```Successfully hacked {user}\nName: {random.choice(name)}\nGender: {random.choice(gender)}\nAge: {age}\nHeight: {random.choice(height)}\nWeight: {weight}\nHair Color: {random.choice(hair_color)}\nSkin Color: {random.choice(skin_color)}\nDOB: {dob}\nLocation: {random.choice(location)}\nPhone: {phone}\nE-Mail: {user.name + random.choice(email)}\nPasswords: {random.choices(password, k=3)}\nOccupation: {random.choice(occupation)}\nAnnual Salary: {random.choice(salary)}\nEthnicity: {random.choice(ethnicity)}\nReligion: {random.choice(religion)}\nSexuality: {random.choice(sexuality)}\nEducation: {random.choice(education)}```"
        )
    else:
        password = [
            'password', '123', 'mypasswordispassword', user.name + "iscool123",
            user.name + "isdaddy", "daddy" + user.name, "ilovediscord",
            "i<3discord", "furryporn456", "secret", "123456789", "apple49",
            "redskins32", "princess", "dragon", "password1", "1q2w3e4r",
            "ilovefurries"
        ]
        message = await ctx.send(f"`Hacking {user}...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...`"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\n`"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...`"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...\nFinalizing life-span dox details\n`"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"```Successfully hacked {user}\nName: {random.choice(name)}\nGender: {random.choice(gender)}\nAge: {age}\nHeight: {random.choice(height)}\nWeight: {weight}\nHair Color: {random.choice(hair_color)}\nSkin Color: {random.choice(skin_color)}\nDOB: {dob}\nLocation: {random.choice(location)}\nPhone: {phone}\nE-Mail: be {user.name + random.choice(email)}\nPasswords: {random.choices(password, k=3)}\nOccupation: {random.choice(occupation)}\nAnnual Salary: {random.choice(salary)}\nEthnicity: {random.choice(ethnicity)}\nReligion: {random.choice(religion)}\nSexuality: {random.choice(sexuality)}\nEducation: {random.choice(education)}```"
        )


@RICHY.command()
async def selfbotinfo(ctx):
    await ctx.message.delete()
    embed = discord.Embed(color=0)
    embed.set_author(name='RICHY | SELFBOT INFO OP')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/767242291794280449/840712671581175868/image0.gif')
    embed.set_footer(text='DEVILs Eternal | SELFBOTBOT INFO')
    embed.add_field(name='___**SELFBOT  INFO**___', value='```ALL THE INFO ABOUT SELFBOT```')
    embed.add_field(name='___**DEVELOPER**___', value='''**insane X richy <\>xBRV#8366**
    https://dsc.bio/richy''')
    embed.add_field(name='___**DATE OF CREATION**___', value='**Sunday ,9 May**')
    embed.add_field(name='___**discord version**___', value='**discord.py 1.7.2**')
    embed.add_field(name='___**Language**___', value='**PYTHON 3.8.2 version**')
    embed.add_field(name='___**ASSISTANT DEVELOPER**___', value='**R E X🚬†ʲᵉⁿⁿⁱᵉﮩ٨ــﮩ♡ ˢᵖʸ#3106**')
    embed.add_field(name='___**instagram**___', value='''** CONTACT US ON INSTAGRAM! | our insta id  _jotarokujo_123**''')
    await ctx.send(embed=embed)




@RICHY.command()
async def token(ctx, user: discord.Member = None):
    await ctx.message.delete()
    list = [
        "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
        "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "_"
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0',
        '1', '2', '3', '4', '5', '6', '7', '8', '9'
    ]
    token = random.choices(list, k=59)
    print(token)
    if user is None:
        user = ctx.author
        await ctx.send(user.mention + "'s token is " + ''.join(token))
    else:
        await ctx.send(user.mention + "'s token is " + "".join(token))

@RICHY.command(aliases=['dong', 'penis'])
async def dick(ctx, *, user: discord.Member = None):
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    size = random.randint(1, 15)
    dong = ""
    for _i in range(0, size):
        dong += "="
    await ctx.send(f"{user}'s Dick size\n8{dong}D")

@RICHY.command()
async def helpfun(ctx):
    embed = discord.Embed(color=0)
    embed.set_author(name='RICHY SELFBOT')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/767242291794280449/841290264845090816/image0.gif')
    embed.set_footer(text='Created by RICHY')
    embed.add_field(name='___**FUN COMMANDS**___', value='```ALL THE FUN COMMANDS```')
    embed.add_field(name='**.token**', value='```GIVES OUT A TOKEN```')
    embed.add_field(name='**.dick**', value='```PERFORMS A DICK SIZE PREDICTION , lmfao xD```')
    embed.add_field(name='**.funhack**', value='```performs a fake hacking process```')
    embed.add_field(name='**.cum**', value='```gives out human semen xD lmfao```')
    await ctx.send(embed=embed)

@RICHY.command()
async def helpnuke(ctx):
    await ctx.message.delete()
    embed = discord.Embed(color=0)
    embed.set_author(name='RICHY SELFBOT')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/829324594929991692/839843014754041876/image0.gif')
    embed.set_footer(text='Created by RICHY')
    embed.add_field(name='___**NUKE COMMANDS**___', value='```NUKE COMMANDS ARE HERE lol xD```')
    embed.add_field(name='**.massroles**', value='```THIS COMMAND SPAMS ROLES xD```')
    embed.add_field(name='**.masschannel**', value='```THIS COMMAND CREATE TONS OF CHANNELS xD```')
    embed.add_field(name='**.webhookspam**', value='```THIS COMMAND FILLS THE SERVER THIS SPAM lol ```')
    embed.add_field(name='**.masskick**', value='```THIS COMMAND KICK EVERYONE```')
    embed.add_field(name='**.helpnuke**', value='```help command```')
    embed.add_field(name='**.helphack**', value='```shows hack commands```')
    await ctx.send(embed=embed) 

RICHY.command(aliases=["masschannels", "masschannel", "ctc"])
async def masschannels(ctx):
    await ctx.message.delete()
    for _i in range(250):
        try:
            await ctx.guild.create_text_channel(name="RICHY OP")
        except:
            return
          
@RICHY.command(aliases=["delchannel"])
async def delchannels(ctx):
    await ctx.message.delete()
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            return

@RICHY.command(aliases=["kickall", "kickwave"])
async def masskick(ctx):
    await ctx.message.delete()
    users = list(ctx.guild.members)
    for user in users:
        try:
            await user.kick(reason="RICHY")
        except:
            pass
          
@RICHY.command(aliases=["rc"])
async def renamechannels(ctx, *, name):
    await ctx.message.delete()
    for channel in ctx.guild.channels:
        await channel.edit(name=name)
@RICHY.command()
async def embed(ctx, *, description):
    embed = discord.Embed(title='RICHY SELFBOT', description=description)
    embed.set_footer(text='RICHYOP')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/767242291794280449/841290264845090816/image0.gif')
    await ctx.send(embed=embed)

@RICHY.command(aliases=['listening'])
async def listen(ctx, *, listenstatus="I didn't know how to specify a listen status lol"):
    randcolor = random.randint(0x000000, 0xFFFFFF)
    await RICHY.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=listenstatus))
    embed=discord.Embed(title="RICHY SELFBOT - Listen Status", description=f"Status is now : `Listening to {listenstatus}`", color=randcolor)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/829324594929991692/839843014754041876/image0.gif")
    embed.set_footer(text="Created by RichY ")
    await ctx.message.edit(content="",embed=embed)

@RICHY.command(aliases=['watching'])
async def watch(ctx, *, watchstatus ="I didn't know how to specify a watch status lol"):
    randcolor = random.randint(0x000000, 0xFFFFFF)
    await RICHY.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=watchstatus))    
    embed=discord.Embed(title="RichY Selfbot - Watch Status", description=f"Status is now : `Watching {watchstatus}`", color=randcolor)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/829324594929991692/839843014754041876/image0.gif")
    embed.set_footer(text="Created by RichY")
    await ctx.message.edit(content="",embed=embed)

@RICHY.command(aliases=['gaming'])
async def game(ctx, *, gamestatus="I didn't know how to specify a game status lol"):
    randcolor = random.randint(0x000000, 0xFFFFFF)
    await RICHY.change_presence(status=discord.Status.dnd, activity=discord.Game(name=gamestatus))
    embed=discord.Embed(title="RichY Selfbot - Game Status", description=f"Status is now : `Playing {gamestatus}`", color=randcolor)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/829324594929991692/839843014754041876/image0.gif")
    embed.set_footer(text="Created By RichY ")
    await ctx.send(content="",embed=embed)

@RICHY.command(aliases=["stopcopycatuser", "stopcopyuser", "stopcopy"])
async def stopcopycat(ctx):
    await ctx.message.delete()
    if RICHY.user is None:
        await ctx.send("You weren't copying anyone to begin with")
        return
    await ctx.send("Stopped copying " + str(RICHY.copycat))
    RICHY.copycat = None

@RICHY.command(aliases=["copycatuser", "copyuser"])
async def copycat(ctx, user: discord.User):
    await ctx.message.delete()
    RICHY.copycat = user
    await ctx.send("Now copying " + str(RICHY.copycat))

@RICHY.command()
async def pingweb(ctx, website=None):
    await ctx.send(f"Pinging {website} with 32 bytes of data:")
    if website is None:
        pass
    else:
        try:
            r = requests.get(website).status_code
        except Exception as e:
            try:
                print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
            finally:
                e = None
                del e

        if r == 404:
            await ctx.send(f"Website is down, status = ({r})")
        else:
            await ctx.send(f"Website is operational, status = ({r})")
            await ctx.send('Timed out')


@RICHY.command()
async def helputility(ctx):
    embed = discord.Embed(color=0)
    embed.set_author(name='RICHY SELFBOT')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/767242291794280449/841290264845090816/image0.gif')
    embed.set_footer(text='Created by RICHY')
    embed.add_field(name='___**UTILITY COMMANDS**___', value='```major commands```')
    embed.add_field(name='**.stream**', value='Ex: .stream RICHY SELFBOT OP')
    embed.add_field(name='**.game**', value='```Ex: .game richyop```')
    embed.add_field(name='**.watch**', value='```your status changes to watching```')
    embed.add_field(name='**.listen**', value='```changes your status to listening```')
    embed.add_field(name='**.stopactivity**', value='```THIS COMMAND STOPS YOUR STATUS ACTIVITY```')
    embed.add_field(name='**.copycat**', value='```copies the mention user```')
    embed.add_field(name='**.stopcopycat**', value='```stops the copycat program```')
    embed.add_field(name='**.nsfw**', value='```THIS COMMAND OPEN THE LIST OF NSFW COMMANDS```')
    embed.add_field(name='**.pingweb**', value='pings the given website! xD')
    
    await ctx.send(embed=embed)
    
@RICHY.command(aliases=["streaming"])
async def stream(ctx, *, message):
    await ctx.message.delete()
    stream = discord.Streaming(
        name=message,
        url='https://www.twitch.tv/discordtos',
    )
    await RICHY.change_presence(activity=stream)
@RICHY.command(aliases=["stopstreaming", "stopstatus", "stoplistening", "stopplaying", "stopwatching"])
async def stopactivity(ctx):
    await ctx.message.delete()
    await RICHY.change_presence(activity=None, status=discord.Status.dnd)
@RICHY.command()
async def nsfw(ctx):
    embed = discord.Embed(color=0)
    embed.set_author(name='RICHY SELFBOT')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/767242291794280449/841290264845090816/image0.gif')
    embed.set_footer(text='Created by RICHY')
    embed.add_field(name='___**NSFW COMMANDS**___', value='```U ARE GAYYY```')
    embed.add_field(name='**.dick**', value='```ur mom gae```')
    await ctx.send(embed=embed)

@RICHY.command()
async def gay(ctx, user: discord.Member = None):
    await ctx.message.delete()
    endpoint = "https://api.alexflipnote.dev/filter/gay?image="
    if user is None:
        avatar = str(ctx.author.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"RICHY_invert.png"))
        except:
            await ctx.send(endpoint)
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(endpoint) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"RICHY_invert.png"))
        except:
            await ctx.send(endpoint)


print("RICHY SELFBOT v2 op")

RICHY.run(token,bot=False)
