import os
from dotenv import load_dotenv

import discord
from discord import app_commands
from discord.ext import commands

from dat.strings import *
from dat.improc import process
from dat.embeds import *
from dbsetup import mongo_setup

intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True

client = commands.Bot(command_prefix=".", intents=intents)
load_dotenv()

db, coll = None, None

DEF_EMOJI = '\N{WHITE HEAVY CHECK MARK}' #default
def get_emoji(id):
    result = coll.find_one({"_id": id})    
    
    if result and result.get("emoji"):         
        return result["emoji"]
    else: 
        return DEF_EMOJI
    
def get_mongo():
    return db, coll

################
# Setup Events #
################
@client.event
async def on_ready():
    global db, coll
    print(f'{client.user} has logged in!')
    
    try:
        await client.change_presence(status=discord.Status.online, activity=discord.Game("Screenshots!"))
        synced = await client.tree.sync()
        print(f"Synced Commands: {synced}")
        db, coll = mongo_setup(os.getenv('MONGO_PASS'))
    except Exception as e:
        print(e)
        
##################
# Reaction Event #
##################
@client.event
async def on_raw_reaction_add(payload):
    from dat.assign import assign
    if payload.emoji.name == get_emoji(payload.guild_id):
        channel = await client.fetch_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        guild = await client.fetch_guild(payload.guild_id)
        author = await guild.fetch_member(message.author.id)
        member = await guild.fetch_member(payload.user_id)
        
        # Only if the reactor has role edit permissions (i.e. an officer)
    
        assigned_roles = []
        if int(member.id) == int(os.getenv('DEV_USER_ID')):    
            async with channel.typing():         
                clears = await process(message.attachments, channel)            
                assigned_roles, num_assign = await assign(coll, clears, guild, channel, author)        
            
                if assigned_roles:
                    assigned_roles = ['**' + item + '**' for item in assigned_roles]    
                    assigned_roles = ', '.join(assigned_roles)        
                    await channel.send(embed=assigned_embed(assigned_roles, num_assign, author))
                
            '''else:
                error = ERROR_NO_NEW_ROLES + '**' + author.name + '**'
                await channel.send(embed=error_embed(error))'''
            
            # Debugging for now!    
            # Result.png is from improc.py
            '''try:    
                with open('./temp/result.png', 'rb') as f:
                    image = discord.File(f)
                    await channel.send(file=image)
                    f.close()
                    os.remove('./temp/result.png')
            except Exception as e:
                print(e)'''
 
###################
# CMND DECORATORS #
###################            
@client.tree.command(name="emoji", description=CMND_EMOJI_DESC)
@app_commands.describe(emoji=CMND_EMOJI_TIP)
async def emoji(interaction: discord.Interaction, emoji: str):
    if interaction.user.guild_permissions.administrator:    
        server_id = interaction.guild.id
        data = {"_id": server_id, "emoji": emoji}
        coll.update_one({"_id": server_id}, {"$set": data}, upsert=True)
        
        emoji = get_emoji(server_id)
        
        await interaction.response.send_message(f'Emoji changed to {emoji}!', ephemeral=True)
    else:
        await interaction.response.send_message(CMND_PERM_DENIED, ephemeral=True)
    
@client.tree.command(name="link", description=CMND_LINK_DESC)
@app_commands.describe(bot=CMND_LINK_BOT_TIP, role=CMND_LINK_ROLE_TIP)
async def link(interaction: discord.Interaction, bot: str, role: str):
    if interaction.user.guild_permissions.administrator:
        role = role
        if ord(role[0]) == 60:
            role_id = int(role[3:-1])
            role = discord.utils.get(interaction.guild.roles, id=role_id)
            role = role.name            
        
        server_id = interaction.guild.id
        data = {"_id": server_id, f'{bot}': role}
        coll.update_one({"_id": server_id}, {"$set": data}, upsert=True)
        
        await interaction.response.send_message(f'**{bot}** succesfully linked to {role} role!', ephemeral=True)        
    else:
        await interaction.response.send_message(CMND_PERM_DENIED, ephemeral=True)
        
@client.tree.command(name="help", description=CMND_HELP_DESC)
@app_commands.describe(command=CMND_HELP_TIP)
@app_commands.choices(command=[
    discord.app_commands.Choice(name="Emoji Command", value=1),
    discord.app_commands.Choice(name="Link Command", value=2),
    discord.app_commands.Choice(name="Image Information", value=3),
])                
async def help(interaction: discord.Interaction, command: discord.app_commands.Choice[int]):
    await interaction.response.send_message(embed=help_embed(command.value), ephemeral=True)
    
@client.tree.command(name="serverinfo", description=CMND_INFO_DESC)
async def serverinfo(interaction: discord.Interaction):
    server_id = interaction.guild_id
    data = coll.find_one({"_id": server_id})
    
    emoji = None
    links = []
    if data:
        emoji = data.get("emoji", None)
        exclude = ["emoji", "_id"]        
        for key, value in data.items():
            if key not in exclude:
                links.append(value)
        
    await interaction.response.send_message(embed=serverinfo_embed(emoji, links))
    
@client.tree.command(name="about", description=CMND_ABOUT_DESC)    
async def help(interaction: discord.Interaction):
    await interaction.response.send_message(embed=about_embed())

###############
# BOT STARTUP #
###############  
client.run(os.getenv('DISCORD_TOKEN'))