# -*- coding: utf-8 -*

import requests
import pandas as pd

sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')


user_agent ='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36'
headers={'User-Agent':user_agent}
url='https://china.nba.com/static/data/league/playerlist.json'



r=requests.get(url,headers=headers).json()
num=int(len(r['payload']['players']))-1

print "长度为",num

p1_cols = []
p2_cols = []

for x in r['payload']['players'][0]['playerProfile']:
    p1_cols.append(x)

for y in r['payload']['players'][0]['teamProfile']:
    p2_cols.append(y)

p1 = pd.DataFrame(columns=p1_cols)
p2 = pd.DataFrame(columns=p2_cols)

for z in range(num):
    player = pd.DataFrame([r['payload']['players'][z]['playerProfile']])
    team = pd.DataFrame([r['payload']['players'][z]['teamProfile']])
    p1 = p1.append(player, ignore_index=True)
    p2 = p2.append(team, ignore_index=True)

p3 = pd.merge(p1, p2, left_index=True, right_index=True)
print p3

#p3.to_csv('nba_player.csv', index=False, encoding="utf-8")