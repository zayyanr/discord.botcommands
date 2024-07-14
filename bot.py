import discord
from discord.ext import commands, tasks

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

token = 'your-bot-token-here'
roleId = 'target-role-id-here'

@bot.event
async def on_ready():
    print(f'Bot is online. Logged in as {bot.user}')
  
@bot.command()
async def role(ctx):
    role = discord.utils.get(ctx.guild.roles, id=int(roleId))
    if role is not None:
        await ctx.author.add_roles(role)
    else:
        await print('Role not found.')
      
bot.run(token)
