__author__ = 'yi-linghwong'

import os
import sys
from langdetect import detect

#lines = open('../fb_data/comments/raw_fb_comments_20160121.csv','r').readlines()
lines = open('../../_big_files/facebook/raw_fb_comments_replies_20160223.csv','r').readlines()

lang_list = []

'''
##############
# get the list of non english languages
##############

for line in lines:

    spline = line.replace('\n','').split(',')

    try:
        lang = detect(spline[-1])
        print (lang,spline[-1])

        if lang not in lang_list:
            lang_list.append(lang)

    except Exception as e:
        print('Failed: ' + str(e))
        print (spline[-1])

print (lang_list)

'''

en_msg = []

lang_list = ['da', 'pt', 'so', 'lt', 'es', 'it', 'hr', 'ca', 'de', 'vi', 'fi', 'no', 'nl', 'af', 'fr', 'sv', 'ar', 'tl', 'ro', 'id', 'sw', 'cs', 'tr', 'th', 'pl', 'cy', 'hi', 'ru', 'et', 'hu', 'sk', 'sl', 'bn', 'sq', 'ja', 'fa', 'ur', 'lv', 'zh-cn', 'el', 'ne', 'bg', 'ko', 'uk', 'ml', 'zh-tw', 'he', 'kn', 'mk', 'te', 'ta', 'mr', 'gu', 'pa']


for line in lines:

    spline = line.replace('\n','').split(',')

    try:
        lang = detect(spline[-1])

        if lang not in lang_list:
            en_msg.append(spline)

    except:
        print ("exception")
        print (spline)
        en_msg.append(spline)

print (len(en_msg))

#f = open('../fb_data/comments/raw_fb_comments_20160121_en.csv','w')
f = open('../../_big_files/facebook/raw_fb_comments_replies_20160223_en.csv','w')

for em in en_msg:
    f.write(','.join(em)+'\n')

f.close()


