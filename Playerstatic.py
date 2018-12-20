# -*- coding: utf-8 -*-

import requests
import pandas as pd

user_agent ='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36'
headers={'User-Agent':user_agent}
url='https://china.nba.com/static/data/league/playerstats_All_All_All_0_All_false_2018_2_All_Team_points_All_perGame.json'

r=requests.get(url,headers=headers).json()
num=int(len(r['payload']['players']))-1

print 'number:',num

p1_cols=[]
p2_cols=[]
p3_cols=[]
p4_cols=[]

for x in r['payload']['players'][0]['playerProfile']:
    p1_cols.append(x)
for x in r['payload']['players'][0]['teamProfile']:
    p2_cols.append(x)
for x in r['payload']['players'][0]['statAverage']:
    p3_cols.append(x)
for x in r['payload']['players'][0]['statTotal']:
    p4_cols.append(x)

p1 = pd.DataFrame(columns=p1_cols)
p2 = pd.DataFrame(columns=p2_cols)
p3 = pd.DataFrame(columns=p3_cols)
p4 = pd.DataFrame(columns=p4_cols)

for z in range(num):
    player = pd.DataFrame([r['payload']['players'][z]['playerProfile']])
    team = pd.DataFrame([r['payload']['players'][z]['teamProfile']])
    statAverage = pd.DataFrame([r['payload']['players'][z]['statAverage']])
    statTotal = pd.DataFrame([r['payload']['players'][z]['statTotal']])
    p1 = p1.append(player, ignore_index=True)
    p2 = p2.append(team, ignore_index=True)
    p3 = p3.append(statAverage, ignore_index=True)
    p4 = p4.append(statTotal, ignore_index=True)

p6 = pd.merge(p1, p2, left_index=True, right_index=True)
p7 = pd.merge(p3, p4, left_index=True, right_index=True)
p5 = pd.merge(p6, p7, left_index=True, right_index=True)

print p6
print p7
print p5

p5.to_csv('nba_player_static.csv', index=False, encoding="utf-8")