import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
from isMember import discordAuthentication
from fortune import Fortune
from datetime import datetime

load_dotenv()
TOKEN = os.getenv("TOKEN")
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix="__", intents=intents)


@bot.event
async def on_ready():
    print('Ready!')
    game = discord.Game("__help Made by 동윤")
    await bot.change_presence(status=discord.Status.online, activity=game)

@bot.command(pass_context=True, name='인증', help='유저 인증을 위한 명령어')
async def authentication(ctx, arg1):
    role = discord.utils.get(ctx.guild.roles, name="User")
    messageAuthor = ctx.message.author
    result = discordAuthentication(arg1)

    if result == "YESYESYES":
        await messageAuthor.add_roles(role)
        embed = discord.Embed(colour=None, color=0x0080ff, title=None, type='rich', url=None, description=None, timestamp=None)
        embed.add_field(name="✔ 인증 결과", value="역할이 부여되었습니다.", inline=True)
        await ctx.send(embed=embed)
    elif result == "NONONO":
        embed = discord.Embed(colour=None, color=0xff0000, title=None, type='rich', url=None, description=None, timestamp=None)
        embed.add_field(name="❌ 인증 결과", value="YUMC 서버 회원이 아닙니다. 회원가입을 하시거나 잠시 후 다시 시도해 주세요.", inline=True)
        await ctx.send(embed=embed)
    else:
        await messageAuthor.add_roles(role)
        embed = discord.Embed(colour=None, color=0x008000, title="🔰 인증 결과", type='rich', url=None, description=None, timestamp=None)
        embed.add_field(name="", value="이미 역할이 부여되었습니다.", inline=True)
        await ctx.send(embed=embed)


@bot.command(pass_context=True, name='운세', help='오늘의 운세(ex. __운세 19990110)')
async def todayFortune(ctx, birth):
    fortuneDataInstance = Fortune()
    fortuneDataInstance = fortuneDataInstance.today_tell(birth)
    embed = discord.Embed(colour=None, color=0x008000, title=str(datetime.today().month)+'월'+str(datetime.today().day)+"일 오늘의 운세", type='rich', url=None, description=None, timestamp=None)
    embed.add_field(name="", value=fortuneDataInstance, inline=True)
    await ctx.send(embed=embed)
        
bot.run(TOKEN)
