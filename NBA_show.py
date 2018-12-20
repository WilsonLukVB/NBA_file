# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pylab as plt

player =pd.read_csv("nba_player.csv")
playerstatic =pd.read_csv("nba_player_static.csv")

player.head()
player.tail()

player['country'].value_counts()
player['position'].value_counts()

#print player['country'].value_counts()
print player['position'].value_counts()

# NorthAmerica = {'巴哈马','美国','加拿大','海地','多米尼加共和国','波多黎各'}
# SouthAmerica = {'哥伦比亚','委内瑞拉','圭亚那','苏里南','厄瓜多尔','秘鲁','巴西','玻利维亚','智利','巴拉圭','乌拉圭','阿根廷'}
# Europe = {'法国','西班牙','德国','瑞典','黑山', '波兰','捷克共和国', '斯洛文尼亚乌克兰', '奥地利', '希腊' ,'芬兰', '英国', '俄罗斯', '波斯尼亚和黑塞哥维那', '塞尔维亚', '克罗地亚','波斯尼亚' ,'意大利','瑞士', '立陶宛', '比利时', '拉脱维亚' }
# Africa = {'喀麦隆','南苏丹','突尼斯','刚果民主共和国', '苏丹', '刚果','塞内加尔','加纳','马里', '埃及'}
# Oceania = {'澳洲','新西兰'}
# Asia = {'土耳其', '中国', '以色列', '格鲁吉亚'}

# asiaPlayer = player[player['country'].isin(Asia)]
# northAmericaPlayer = player[player['country'].isin(NorthAmerica)]
# southAmericaPlayer = player[player['country'].isin(SouthAmerica)]
# europePlayer = player[player['country'].isin(Europe)]
# oceaniaPlayer = player[player['country'].isin(Oceania)]
# africaPlayer = player[player['country'].isin(Africa)]

# north = len(northAmericaPlayer)
# south = len(southAmericaPlayer)
# europe = len(europePlayer)
# africa = len(africaPlayer)
# asia = len(asiaPlayer)
# oceania = len(oceaniaPlayer)

# d=[north,south,europe,africa,asia,oceania]
# i=['north','south','europe','africa','asia','oceania']
# n=[0,1,2,3,4,5]


# contient = pd.Series(data=d,index=i)

# print '北美洲球员人数:',north
# print '南美洲球员人数:',south
# print '欧洲球员人数:',europe
# print '非洲球员人数:',africa
# print '亚洲球员人数:',asia
# print '大洋洲洲球员人数:',oceania

# contient.sort_index(ascending=True)
# contient.plot(kind='bar',alpha=0.5)
# plt.xlabel("contient")
# plt.ylabel("theNumofPlayer")
# plt.title("The number of players on all continents ")

# for a,b in zip(n,d):
#     plt.text(a-0.1,b+0.5,'%.0f' %b)

#plt.show()

df = player
df =df[True^df['draftYear'].isin([00])]
df = df['draftYear'].value_counts()
df.index.name='Year'
df = df.sort_index(ascending=True)

print df

df.plot(kind = 'bar', alpha = 0.5)
plt.xlabel('years')
plt.ylabel('count')
plt.title('2017-2018 NBA season players')
plt.show()