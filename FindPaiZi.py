import requests

def get_paizi(uid, headers, CheckBigLevel):
    result = requests.get(
        f'https://api.live.bilibili.com/xlive/web-ucenter/user/MedalWall?target_id={uid}',
        headers=headers,
    )
    data_json = result.json()
    first_line = '粉丝牌：\n'
    medal_wall = str()
    num = len(data_json['data']['list'])
    BigLevel = []
    for i in range(num):
        medal_wall = (
            medal_wall
            + data_json['data']['list'][i]['medal_info']['medal_name']
            + str(data_json['data']['list'][i]['medal_info']['level'])
            + '级'
            + '\t{}\n'.format(data_json['data']['list'][i]['target_name'])
        )
        if data_json['data']['list'][i]['medal_info']['level'] >= 21:
            BigLevel.append(data_json['data']['list'][i]['target_name'])

    if CheckBigLevel:
        return '舰长：' + ','.join(map(str, BigLevel))
    else:
        return first_line + medal_wall[:-1]

Cookie = input("输入Cookie: ")
CheckBigLevelTorF = input("是否仅查询舰长?(yes/no): ")
if CheckBigLevelTorF.lower() == 'yes':
    CheckBigLevel = True
else:
    CheckBigLevel = False

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36 ',
    "Cookie": Cookie,
}

while True:
    uid = input("输入待查询UID:")
    print(get_paizi(uid, headers, CheckBigLevel))
    user_input = input("是否结束操作?(yes/no): ")
    if user_input.lower() == 'yes':
        break
