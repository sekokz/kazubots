import discord
import random
import lucky
from discord import guild
from discord.abc import GuildChannel
from discord.flags import Intents

fortunes = ["大吉", "吉", "中吉", "小吉", "末吉", "凶", "大凶"]

DISCORD_TOKEN = os.environ['DISCORD_TOKEN']

id_to_name = {
  "kzn_ygr":"カズ",
  "yu01383":"ユウ",
  "kurome0568_14843":"黒江",
  "renge_akatuki":"ミユ(朱月レン)",
  "kirie5819":"キリエ",
  "souichirosimon":"サイモン先輩",
  "kanasu1":"カウナス",
  "may3650":"May",
  ".barukiri":"ばるきり",
  "konoetyun":"近衛"
}

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

  if message.content.find("今日の運勢は") == -1:
    return

  if message.author.bot:  # botの発言を無視する
    return

  channel = client.get_channel(message.channel.id)  # 送信元のチャンネルを取得
  if type(channel) != discord.TextChannel:
    return

  guild = client.get_guild(message.guild.id)
  if type(guild) != discord.Guild:
    return

  member = guild.get_member(message.author.id)
  if type(member) != discord.Member:
    return

  f = randomFortune()
  item = randomItem()
  msg = ""
  if f in fortunes:
    msg = f + "だってさ\n" + f"ラッキーフードは{item}だよ"
  else:
    msg = f + "だってさ\n...おめでとう！激レアだよ！"

  await channel.send(f"{conv_id2name(member.name)}さんの運勢は" + msg, silent=True)


def conv_id2name(id):
  return id_to_name.get(id, id)

def randomFortune():
  custonefortunes = ["大吉", "吉", "中吉", "小吉", "末吉", "凶", "大凶", "狂", "夏吉ゆうこ", "吉村・Thi・梅"]
  probabilities = [0.1, 0.2, 0.2, 0.2, 0.2, 0.2, 0.1, 0.01, 0.01, 0.01]  # 増やした分だけ弄る
  result = random.choices(custonefortunes, probabilities, k=1)[0]
  return result


def randomItem():
  result = random.choices(lucky.items)[0]
  return result


client.run(DISCORD_TOKEN)
