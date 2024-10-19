import discord
import fortune
import lily
from discord import guild
from discord.abc import GuildChannel
from discord.flags import Intents
from datetime import datetime
import os
import random
from server import server_thread

DISCORD_TOKEN = os.environ['DISCORD_TOKEN']

# Create an instance of Intents
intents = discord.Intents.default()
# Set the guilds flag
intents.guilds = True
intents.members = True
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
  print('ログインしました')

@client.event
async def on_message(message):

  if message.author.bot:  # botの発言を無視する
    return

  channel = client.get_channel(message.channel.id)  # 送信元のチャンネルを取得
  if type(channel) != discord.TextChannel:
    return

  mode = 0

  if message.content.find("今日の運勢") != -1:
    mode = 1

  elif message.content.find("今日のリリィ") != -1:
    mode = 2

  elif (message.content.find("持ってない") != -1) or (message.content.find("持ってねー") != -1) or (message.content.find("持ってません") != -1):
    mode = 3

  elif message.content.find("今日のポジション") != -1:
    mode = 4

  # 該当しなかった
  if mode == 0:
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
    await channel.send(fortune.get_fortune(g_name), silent=True)

  elif mode == 2:
    await channel.send(lily.get_lily(g_name), silent=True)

  # 文句言われた
  elif mode == 3:
    start = datetime.now().replace(hour=0, minute=0, second=0)
    end = datetime.now().replace(hour=23, minute=59, second=59)

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

  elif mode == 4:

    AZs = []
    TZs = []
    BZs = []

    # 全加入者の一覧を総当たり
    for m in message.guild.members:
      rolenames = []
      # 正規メンバーだけを対象とする
      for role in m.roles:
        # その人の全ロールを配列にする
        rolenames.append(role.name)
        # メンバーである
        if rolenames.count("メンバー") > 0:
          # かつポジション
          if rolenames.count("AZ") > 0:
            AZs.append(m.global_name)
          elif rolenames.count("TZ") > 0:
            TZs.append(m.global_name)
          elif rolenames.count("BZ") > 0:
            BZs.append(m.global_name)

    # シャッフルする
    role_limits = {'AZ':4, 'TZ':3, 'BZ':2}
    initial_roles = [(mem, 'AZ') for mem in AZs] + [(mem, 'TZ') for mem in TZs] + [(mem, 'BZ') for mem in BZs]

    new_roles = shuffle_roles(initial_roles, role_limits)

    msg = '今日のポジションは...これでどうかな！？\n'

    for mem, new_role in new_roles:
      msg += f"{mem}: {new_role}\n"

    await channel.send(msg, silent=True)

def shuffle_roles(initial_roles, role_limits):
  # 新しいリスト
  shuffled_roles = []

  # 各役割がシャッフル後に就ける役割
  candidates = {'AZ': ['TZ', 'BZ'], 'TZ': ['AZ', 'BZ'], 'BZ': ['AZ', 'TZ']}

  # 各役割の人数カウント
  role_count = {'AZ': 0, 'TZ': 0, 'BZ': 0}

  for mem, role in initial_roles:
    # 人数を超えないように割り当てる
    available_roles = [r for r in candidates[role] if role_count[r] < role_limits[r]]
    new_role = random.choice(available_roles)

    # 新しい役割を追加してカウントを更新
    shuffled_roles.append((mem, new_role))
    role_count[new_role] += 1

  return shuffled_roles

server_thread()
client.run(DISCORD_TOKEN)
