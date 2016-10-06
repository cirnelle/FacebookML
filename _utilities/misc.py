__author__ = 'yi-linghwong'

import os
import sys

#-------------------------------
# get engrate from excel and then insert into csv (maas data)

# lines1 = open('../output/engrate/maas/engrate_from_excel.csv','r').readlines()
# lines2 = open('../fb_data/posts/maas/raw_maas.csv','r').readlines()
#
# id_dict = {}
#
# for line in lines1:
#     spline = line.rstrip('\n').split(',')
#
#     id_dict[spline[0]] = spline[3]
#
# fb_posts = []
#
# for line in lines2[1:]:
#     spline = line.rstrip('\n').split(',')
#     key = spline[2]
#
#     if key in id_dict:
#         engrate = id_dict[key]
#         spline.insert(6,engrate)
#         fb_posts.append(spline)
#
#     # else:
#     #     print ("key does not exist")
#     #     print (key)
#     #     pass
#
# f = open('../output/engrate/maas/engrate_maas_raw.csv','w')
#
# for t in fb_posts:
#     f.write(','.join(t)+'\n')
#
# f.close()

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

#--------------------------------------

################
# extract only fb posts which I have reallike number (Facebook)
################
#
# import os
# import sys
# import time
#
#
# ##################
# # get the dates for follcount file
# ##################
#
# lines2 = open('/Users/yi-linghwong/GitHub/FacebookML/user_list/likes/NASA.txt','r').readlines()
#
# date_dict = {}
#
# for line in lines2:
#     spline = line.rstrip('\n').split(',')
#
#     if spline == ['']:
#         print("error")
#         break
#
#     d1 = spline[0].replace('\n', '').split(' ')
#
#     if len(d1) == 6:
#         d1.remove(d1[2])
#
#     date_s = d1[1] + ' ' + d1[2] + ' ' + d1[4]
#
#     t1 = time.strptime(date_s, '%b %d %Y')
#     t_epoch = time.mktime(t1)
#     date_dict[t_epoch] = spline[1]
#
# #################
# # get the dates for raw tweet file
# #################
#
# lines1 = open('/Users/yi-linghwong/Documents/PhD/RESEARCH/NASA_data/facebook/data/ORI_fb_posts_reallike.csv', 'r').readlines()
#
# print (len(lines1))
#
# fb_posts = []
#
# for line in lines1:
#     spline = line.rstrip('\n').split(',')
#
#     d1 = spline[4].replace('\n', '').split(' ')
#
#     if len(d1) != 3:
#         print("error")
#         #d1.remove(d1[2])
#
#     d2 = d1[0].replace('\n','').split('/')
#
#     if int(d2[0]) < 10:
#         d2[0]='0'+d2[0]
#
#     if int(d2[1]) < 10:
#         d2[1]='0'+d2[1]
#
#
#     date_s = d2[0] + ' ' + d2[1] + ' ' + d2[2]
#
#     t1 = time.strptime(date_s, '%m %d %y')
#
#     #print (t1)
#
#     t_epoch = time.mktime(t1)
#
#
#     if t_epoch in date_dict:
#
#         if date_dict[t_epoch] != 'nan':
#             #spline[3] = date_dict[t_epoch]
#             spline.append(date_dict[t_epoch])
#             fb_posts.append(spline)
#
#     else:
#         spline.append('n/a')
#         fb_posts.append(spline)
#
# print(len(fb_posts))
#
#
# f = open('/Users/yi-linghwong/Documents/PhD/RESEARCH/NASA_data/facebook/data/ORI_fb_posts_reallike_updated.csv', 'w')
#
# for ut in fb_posts:
#     f.write(','.join(ut) + '\n')
#
# f.close()

#----------------------------------

##########################
# insert REAL Facebook engagement rate from a list into raw NASA posts
##########################

# lines1 = open('../fb_data/posts/nasa/raw_nasa.csv','r').readlines()
# lines2 = open('../output/engrate/nasa/REAL_engrate_list.csv','r').readlines()
#
# posts = []
#
# for line in lines1[1:]:
#     spline = line.rstrip('\n').split(',')
#     posts.append(spline)
#
# print (len(posts))
#
# engrates = []
#
# for line in lines2:
#     spline = line.rstrip('\n')
#     engrates.append(spline)
#
# print (len(engrates))
#
# posts_with_engrate = []
#
# for index1,e in enumerate(engrates):
#
#     for index2, t in enumerate(posts):
#
#         if index2 == index1:
#             t.insert(6,e)
#             posts_with_engrate.append(t)
#
# print (len(posts_with_engrate))
#
# f = open('../output/engrate/nasa/REAL_engrate_nasa_raw.csv','w')
#
# for te in posts_with_engrate:
#     f.write(','.join(te)+'\n')
#
# f.close()

#--------------------------------------------------

################
# extract only posts which I have reallike number
################

# import os
# import sys
# import time
#
#
# ##################
# # get the dates for follcount file
# ##################
#
# lines2 = open('../followers/follcount_interpolated/NASA.csv','r').readlines()
#
# date_dict = {}
#
# for line in lines2:
#     spline = line.rstrip('\n').split(',')
#
#     if spline == ['']:
#         print("error")
#         break
#
#     d1 = spline[0].replace('\n', '').split('-')
#
#     # if len(d1) == 6:
#     #     d1.remove(d1[2])
#
#     if int(d1[1]) < 10:
#         d1[1] = '0'+ d1[1]
#
#     if int(d1[2]) < 10:
#         d1[2] = '0' + d1[2]
#
#
#     date_s = d1[2] + ' ' + d1[1] + ' ' + d1[0]
#
#     t1 = time.strptime(date_s, '%d %m %Y')
#     t_epoch = time.mktime(t1)
#     date_dict[t_epoch] = spline[1]
#
# #################
# # get the dates for raw tweet file
# #################
#
# lines1 = open('../tweets/nasa/raw_nasa.csv', 'r').readlines()
#
# print (len(lines1))
#
# tweets = []
# follcount_list = []
#
# for line in lines1:
#     spline = line.rstrip('\n').split(',')
#
#     d2 = spline[1].replace('\n', '').split(' ')
#
#     if len(d2) != 6:
#         print("error")
#         #d1.remove(d1[2])
#
#     # d2 = d1[2].replace('\n','').split('/')
#     #
#     # if int(d2[0]) < 10:
#     #     d2[0]='0'+d2[0]
#     #
#     # if int(d2[1]) < 10:
#     #     d2[1]='0'+d2[1]
#
#
#     date_s = d2[2] + ' ' + d2[1] + ' ' + d2[5]
#
#     t1 = time.strptime(date_s, '%d %b %Y')
#
#     #print (t1)
#
#     t_epoch = time.mktime(t1)
#
#
#     if t_epoch in date_dict:
#
#         if date_dict[t_epoch] != 'nan':
#             #spline[3] = date_dict[t_epoch]
#             follcount = date_dict[t_epoch]
#             tweets.append([spline[0],spline[1],spline[2],follcount,spline[4],spline[5],spline[6],spline[7],spline[8]])
#
#     else:
#         pass
#
# print(len(tweets))
#
#
# f = open('../tweets/nasa/nasa_realfoll.csv', 'w')
#
# for t in tweets:
#     f.write(','.join(t) + '\n')
#
# f.close()

#------------------------------------

########################
# insert page like count into NASA raw post file
########################

# import sys
# import time
#
# lines1 = open('../fb_data/posts/nasa/raw_nasa.csv','r').readlines()
# lines2 = open('../user_list/likes_interpolated/NASA.csv','r').readlines()
#
# ##################
# # get the dates for follcount file
# ##################
#
# date_dict = {}
#
# for line in lines2:
#     spline = line.rstrip('\n').split(',')
#
#     if spline == ['']:
#         print("error")
#         break
#
#     d1 = spline[0].replace('\n', '').split('-')
#
#     # if len(d1) == 6:
#     #     d1.remove(d1[2])
#
#     if int(d1[1]) < 10:
#         d1[1] = '0'+ d1[1]
#
#     if int(d1[2]) < 10:
#         d1[2] = '0' + d1[2]
#
#
#     date_s = d1[2] + ' ' + d1[1] + ' ' + d1[0]
#
#     t1 = time.strptime(date_s, '%d %m %Y')
#     t_epoch = time.mktime(t1)
#     date_dict[t_epoch] = spline[1]
#
#
# #################
# # get the dates for raw tweet file
# #################
#
#
# posts = []
# likecount_list = []
#
# for line in lines1[1:]:
#     spline = line.rstrip('\n').split(',')
#
#     d2 = spline[1].replace('\n', '').split(' ')
#
#     if len(d2) != 3:
#         print("error")
#         #d1.remove(d1[2])
#
#     d3 = d2[0].replace('\n','').split('/')
#
#     if int(d3[0]) < 10:
#         d3[0]='0'+d3[0]
#
#     if int(d3[1]) < 10:
#         d3[1]='0'+d3[1]
#
#
#     date_s = d3[1] + ' ' + d3[0] + ' ' + d3[2]
#
#     t1 = time.strptime(date_s, '%d %m %y')
#
#     #print (t1)
#
#     t_epoch = time.mktime(t1)
#
#     if t_epoch in date_dict:
#
#         if date_dict[t_epoch] != 'nan':
#             #spline[3] = date_dict[t_epoch]
#             likecount = date_dict[t_epoch]
#             posts.append([spline[0],spline[1],spline[2],likecount,spline[3],spline[4],spline[5],spline[6],spline[7]])
#
#     else:
#         likecount = 'n/a'
#         posts.append(
#             [spline[0], spline[1], spline[2], likecount, spline[3], spline[4], spline[5], spline[6], spline[7]])
#
# print(len(posts))
#
#
# f = open('../fb_data/posts/nasa/raw_nasa_likecount.csv', 'w')
#
# for t in posts:
#     f.write(','.join(t) + '\n')
#
# f.close()

#------------------------------

#####################
# update like count for NASA post (using like slope)
#####################

import sys
import time

lines = open('../fb_data/posts/nasa/raw_nasa_likecount.csv','r').readlines()
print (len(lines))

# get t_max and pagelike_count_max

date_max = '30 7 16'
t_date_max = time.strptime(date_max, '%d %m %y')
t_max = time.mktime(t_date_max)

pagelike_count_max = 16637677

updated_posts = []

for line in lines:
    spline = line.rstrip('\n').split(',')

    if spline[3] == 'n/a':

        d2 = spline[1].replace('\n', '').split(' ')

        if len(d2) != 3:
            print("error")
            #d1.remove(d1[2])

        d3 = d2[0].replace('\n','').split('/')

        if int(d3[0]) < 10:
            d3[0]='0'+d3[0]

        if int(d3[1]) < 10:
            d3[1]='0'+d3[1]


        date_s = d3[1] + ' ' + d3[0] + ' ' + d3[2]
        t1 = time.strptime(date_s, '%d %m %y')
        t_epoch = time.mktime(t1)

        t_delta = t_max - t_epoch

        slope = 0.146734734371

        y_delta = slope * t_delta

        pagelike_count = float(pagelike_count_max) - y_delta
        pagelike_count = int(pagelike_count)

        updated_posts.append([spline[0],spline[1],spline[2],str(pagelike_count),spline[4],spline[5],spline[6],spline[7],spline[8]])

    else:
        updated_posts.append(spline)


print (len(lines))

f = open('../fb_data/posts/nasa/raw_nasa_likecount_interpolated.csv','w')

for up in updated_posts:
    f.write(','.join(up)+'\n')

f.close()


