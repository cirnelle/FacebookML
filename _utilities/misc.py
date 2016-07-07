__author__ = 'yi-linghwong'

import os
import sys

#-------------------------------
# get engrate from excel and then insert into csv (maas data)

lines1 = open('../output/engrate/maas/engrate_from_excel.csv','r').readlines()
lines2 = open('../fb_data/posts/maas/raw_maas.csv','r').readlines()

id_dict = {}

for line in lines1:
    spline = line.rstrip('\n').split(',')

    id_dict[spline[0]] = spline[3]

fb_posts = []

for line in lines2[1:]:
    spline = line.rstrip('\n').split(',')
    key = spline[2]

    if key in id_dict:
        engrate = id_dict[key]
        spline.insert(6,engrate)
        fb_posts.append(spline)

    # else:
    #     print ("key does not exist")
    #     print (key)
    #     pass

f = open('../output/engrate/maas/engrate_maas_raw.csv','w')

for t in fb_posts:
    f.write(','.join(t)+'\n')

f.close()

#-------------------------------------
# get a certain number of tweets from the LER list

# lines = open('../output/engrate/maas/labelled_maas.csv','r').readlines()
#
# tweets = []
# ler = []
#
# for line in lines:
#     spline = line.rstrip('\n').split(',')
#
#     if spline[1] == 'HER':
#         tweets.append(spline)
#
#     if spline[1] == 'LER':
#         if len(ler) < 279:
#             tweets.append(spline)
#             ler.append(spline)
#
#         else:
#             pass
#
# print (len(tweets))
#
# f = open('../output/engrate/maas/labelled_maas_s.csv','w')
#
# for t in tweets:
#     f.write(','.join(t)+'\n')
#
# f.close()
