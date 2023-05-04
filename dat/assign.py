import discord
from dat.clear_dat import value_dict
from dat.strings import *
from dat.embeds import error_embed

# clears = ['vss', 'vrg_tri', etc...]
async def assign(coll, clears, guild, channel, author):    
    num_assign = 0
    
    try:
        clears_dict = {}
        result = coll.find_one({"_id": guild.id}, {"emoji": 0})
        
        # Create a dictionary with only clears that the user has that are also present in 
        # the server specific database. This automatically updates any lower order clear to 
        # the higher order version due to the order of something im not sure honestly
        for clear in clears:
            if result.get(clear):
                clears_dict.update({clear[:3] : ((result[clear]), value_dict[clear])})
                
        assigned_roles = []  
        for tag, info in clears_dict.items():
            role = discord.utils.get(guild.roles, name=info[0])
            if role not in author.roles:
                await author.add_roles(role)
                assigned_roles.append(info[0])
                num_assign += 1           
        
        return assigned_roles, num_assign
    
    except Exception as e:
        print(e)
        await channel.send(embed=error_embed(f"Error: {e}"))