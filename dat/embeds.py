import discord
from dat.strings import *

def assigned_embed(assigned_clears, num_assign, author):
    
    desc_str = EMBED_ASSIGNED_DESC_1 + str(num_assign) + EMBED_ASSIGNED_DESC_2 + '**' + str(author.display_name) + '**'
    embed = discord.Embed(title=EMBED_ASSIGNED_TITLE, colour=discord.Colour(0x1b2e4d), description=desc_str)
    #embed.set_author(name="ESO Role Bot", icon_url="https://i.imgur.com/vgIaJue.png")
    
    embed.add_field(name="", value=assigned_clears)
    
    embed.set_footer(text=EMBED_FOOTER_STR, icon_url="https://i.imgur.com/vgIaJue.png")
    
    return embed

def error_embed(error):
    
    embed = discord.Embed(title=EMBED_ERROR_TITLE, colour=discord.Colour(0x1b2e4d))

    embed.add_field(name="", value=error, inline=True)
    embed.add_field(name="", value=EMBED_ERROR_HELP, inline=False)
    
    embed.set_footer(text=EMBED_FOOTER_STR, icon_url="https://i.imgur.com/vgIaJue.png")
    
    return embed

def help_embed(value):
    if value == 1:
        embed = discord.Embed(title=EMBED_HELP_TITLE_EMOJI, colour=discord.Colour(0x1b2e4d))
        
        embed.add_field(name="", value=HELP_EMOJI, inline=False)
        
        embed.set_footer(text=EMBED_FOOTER_STR, icon_url="https://i.imgur.com/vgIaJue.png")
        return embed
    
    if value == 2:
        embed = discord.Embed(title=EMBED_HELP_TITLE_LINK, colour=discord.Colour(0x1b2e4d))
        
        embed.add_field(name="", value=HELP_LINK, inline=True)
        embed.add_field(name="Vet Clears", value=HELP_VET_CLRS, inline=False)
        embed.add_field(name="Partial HMs", value=HELP_PART_HM, inline=False)
        embed.add_field(name="Full HMs", value=HELP_FULL_HM, inline=False)
        embed.add_field(name="Trifectas", value=HELP_TRI, inline=False)
        embed.add_field(name="Extra Achievs", value=HELP_EX, inline=False)        
        embed.add_field(name="", value=HELP_STUCK, inline=False)
        
        embed.set_footer(text=EMBED_FOOTER_STR, icon_url="https://i.imgur.com/vgIaJue.png")
        return embed
    
    if value == 3:
        embed = discord.Embed(title=EMBED_HELP_TITLE_IMG, colour=discord.Colour(0x1b2e4d), url='https://i.imgur.com/M2TMU96.png')
        
        embed.add_field(name="", value=HELP_IMG, inline=False)
        embed.add_field(name="", value=HELP_STUCK, inline=False)
        
        embed.set_footer(text=EMBED_FOOTER_STR, icon_url="https://i.imgur.com/vgIaJue.png")
        return embed
    
def serverinfo_embed(emoji, links):
    embed = discord.Embed(title=EMBED_INFO_TITLE, colour=discord.Colour(0x1b2e4d))
    
    if emoji:
        embed.add_field(name="Server Emoji", value=(EMBED_INFO_EMOJI + emoji), inline=False)
    else:
        embed.add_field(name="Server Emoji", value=EMBED_INFO_NO_EMOJI, inline=False)
        
    if links:
        link_str = ', '.join(links)
        embed.add_field(name="Server Linked Roles", value=(EMBED_INFO_LINKS + link_str + '\n'), inline=False)
    else:
        embed.add_field(name="Server Linked Roles", value=EMBED_INFO_NO_LINKS, inline=False)    
    
    embed.set_footer(text=EMBED_FOOTER_STR, icon_url="https://i.imgur.com/vgIaJue.png")
    return embed 


def about_embed():
    embed = discord.Embed(title=EMBED_ABOUT_TITLE, colour=discord.Colour(0x1b2e4d), url="https://www.esoresorces.com")
    
    embed.add_field(name="", value=ABOUT_INFO, inline=True)    
    
    embed.set_footer(text=EMBED_FOOTER_STR, icon_url="https://i.imgur.com/vgIaJue.png")
    return embed