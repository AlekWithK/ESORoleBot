import discord
from dat.clear_dat import heiarchy
from dat.strings import *
from dat.embeds import error_embed

# clears = ['vss', 'vrg_tri', etc...]
async def assign(coll, clears, guild, channel, author):    
    num_assign = 0
    try:
        clears_list = []
        result = coll.find_one({"_id": guild.id}, {"emoji": 0})
        
        # Create a dictionary with only clears that the user has that are also present in 
        # the server specific database
        for clear in clears:
            if result.get(clear):
                clears_list.append((clear, result[clear]))
        
        # Assign roles if not already held, and create a list of assigned roles           
        assigned_roles = []
        clears_sorted = sorted(clears_list, key=lambda x: [tup[1] for tup in heiarchy if tup[0] == x[0]] or [float('inf')])[::-1]
        #print(clears_sorted)        
                
        bypass = []
        for clear, role in result.items():
            names = [role.name for role in author.roles]
            if role in names:
                bypass.append(clear[:3])
        
        for clear in clears_sorted:
            role = discord.utils.get(guild.roles, name=clear[1])
            tag = clear[0][:3]
            if role not in author.roles and tag not in bypass:
                await author.add_roles(role)
                assigned_roles.append(clear[1])
                num_assign += 1
                
                if clear[0] != 'vas_felms' and clear[0] != 'vss_ice':
                    bypass.append(tag)
                
        
        return assigned_roles, num_assign
    
    except Exception as e:
        print(e)
        await channel.send(embed=error_embed(f"Error: {e}"))