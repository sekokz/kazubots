import random


def get_shuffled(members):

    AZs = []
    TZs = []
    BZs = []

    # 全加入者の一覧を総当たり
    for m in members:
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

    return msg

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