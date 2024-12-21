import discord
import fortune
import yearsfortune
import lily
import jobshuffle
from discord import guild
from discord.abc import GuildChannel
from discord.flags import Intents
from datetime import datetime
import pytz
import os
import remind as reminder
from server import server_thread

import TOKEN
#DISCORD_TOKEN = TOKEN.DISCORD_TOKEN

DISCORD_TOKEN = os.environ['DISCORD_TOKEN']

# Create an instance of Intents
intents = discord.Intents.default()
# Set the guilds flag
intents.guilds = True
intents.members = True
intents.message_content = True
client = discord.Client(intents=intents)

step = 0

@client.event
async def on_ready():
  print('ログインしました')

@client.event
async def on_message(message):

  global step

  if message.author.bot:  # botの発言を無視する
    return

  channel = client.get_channel(message.channel.id)  # 送信元のチャンネルを取得
  if type(channel) != discord.TextChannel:
    return

  mode = 0

  if message.content.find("今日の運勢") != -1:
    step = 0
    mode = 1

  elif message.content.find("今日のリリィ") != -1:
    step = 0
    mode = 2

  elif (message.content.find("持ってない") != -1) or (message.content.find("持ってねー") != -1) or (message.content.find("持ってません") != -1):
    mode = 3

  elif message.content.find("今日のポジション") != -1:
    step = 0
    mode = 4

  elif message.content.find("今年の運勢") != -1:
    mode = 5

  # 該当しなかった
  if mode == 0:
    step = 0
    return

  guild = client.get_guild(message.guild.id)
  if type(guild) != discord.Guild:
    return

  member = guild.get_member(message.author.id)
  if type(member) != discord.Member:
    return

  g_name = message.author.global_name
  if g_name == None:
    g_name = message.author.name

  # いつもの
  if mode == 1:
    await channel.send(fortune.get_fortune(g_name, datetime.now(pytz.timezone("Asia/Tokyo"))), silent=True)

  elif mode == 2:

    msgs = lily.get_lily(g_name)
    step = 1

    for msg in msgs:
      await channel.send(msg, silent=True)

  # 文句言われた
  elif mode == 3:
    if step == 1:
      start = datetime.now(pytz.timezone("Asia/Tokyo")).replace(hour=0, minute=0, second=0)
      end = datetime.now(pytz.timezone("Asia/Tokyo")).replace(hour=23, minute=59, second=59)
      async for histmsg in channel.history(limit=None, after=start, before=end):

        except_name = []

        # botの発言を集める
        if histmsg.author.bot:
          for item in lily.items:
            if item["name"] in histmsg.content:
              # 今日botが出した名前は除外する
              except_name.append(item["name"])

        flag = True
        while(flag):
          random_name = lily.random_lily()
          if random_name in except_name:
            flag = True
          else:
            flag = False

        msg = f"しょうがないなぁ...\n{g_name}さんの今日のリリィは {random_name["name"]} だよ"

      await channel.send(msg, silent=True)
    else:
      print("ignore mode 3")

  elif mode == 4:
    await channel.send(jobshuffle.get_shuffled(message.guild.members), silent=True)
  elif mode == 5:
    today = datetime.now(pytz.timezone("Asia/Tokyo"))
    if today.month == 1 and 1 <= today.day <= 7:
      await channel.send(yearsfortune.get_fortune(g_name), silent=True)
    else:
      await channel.send("それは期間限定なんだよねぇ", silent=True)

server_thread()
client.run(DISCORD_TOKEN)
