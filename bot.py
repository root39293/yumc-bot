import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
from isMember import discordAuthentication

load_dotenv()
TOKEN = os.getenv("TOKEN")
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix="__", intents=intents)


@bot.command()
async def 인증(ctx, arg1):
    role = discord.utils.get(ctx.guild.roles, name="User")
    messageAuthor = ctx.message.author
    result = discordAuthentication(arg1)

    if result == "YESYESYES":
        await messageAuthor.add_roles(role)
        await ctx.send("User role has been assigned.")
    elif result == "NONONO":
        await ctx.send("You are not User")
    else:
        await ctx.send("You are already User. User role has been assigned")
        await messageAuthor.add_roles(role)


bot.run(TOKEN)
