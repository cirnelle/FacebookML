__author__ = 'yi-linghwong'

################
# label tweets by engagement rate (HRT, LRT)
# subroutines: calculate engagement rate, label tweets
################

import time
import sys
import os
import re
import numpy as np
from matplotlib import pyplot as plt


class LabelFbPostsEngRate():

    def get_eng_rate(self):

        lines = open(path_to_preprocessed_fb_post_file,'r').readlines()

        fb_posts = []

        for line in lines:
            spline = line.replace('\n','').split(',')
            fb_posts.append(spline)

        print ("Length of tweet list is "+str(len(fb_posts)))

        for line in lines[:1]:
            spline = line.replace('\n','').split(',')
            length = len(spline)

        print ("Number of element per line is "+str(length))

        engrate_list = []

        print ("Calculating engagement rate...")

        for fp in fb_posts[1:]:

            if len(fp) == length:

                engagement = (0.5*int(fp[4])) + int(fp[5])

                engrate = str((np.divide(int(engagement),int(fp[2])))*100)

                engrate_list.append([fp[0],fp[1],fp[2],fp[3],fp[4],fp[5],fp[6],engrate,fp[7],fp[8]])

            else:
                print ("error")
                print(fp)
                pass

        f = open(path_to_store_engrate_output,'w')

        for el in engrate_list:
            f.write(','.join(el)+'\n')

        f.close()

        return engrate_list


    def label_fb_post(self):

        fb_posts = self.get_eng_rate()

        labelled_fb_posts = []
        high_er = []
        low_er = []

        print ("Labelling tweets ...")

        for fp in fb_posts:

            if float(fp[7]) > 9:

                labelled_fb_posts.append([fp[9],'HER'])
                high_er.append([fp[8],'HER'])

            elif float(fp[7]) < 0.015:

                labelled_fb_posts.append([fp[9],'LER'])
                low_er.append([fp[8],'LER'])

            else:
                pass

        print ("Length of high ER list is "+str(len(high_er)))
        print ("Length of low ER list is "+str(len(low_er)))

        f = open(path_to_store_labelled_fb_post, 'w')

        for lf in labelled_fb_posts:

            f.write(','.join(lf)+str('\n'))

        f.close()

        print ("Length of labelled tweets is "+str(len(labelled_fb_posts)))

        return labelled_fb_posts


    def get_histogram(self):

        lines = open(path_to_store_engrate_output,'r').readlines()

        erlist=[]
        zero_list = []

        for line in lines:
            spline=line.replace("\n", "").split(",")
            #creates a list with key and value. Split splits a string at the comma and stores the result in a list

            #some lines have unexpected line breaks which mess up the output (the last item in the list is the tweet, not the ER)


            #important to convert to float!!

            number=float(spline[7])

            if number > 0:

                erlist.append(number)

            elif number == 0:
                zero_list.append(number)

        print ("Length of list is "+str(len(erlist)))
        print ("Length of zero list is "+str(len(zero_list)))
        print (min(erlist))
        print (max(erlist))


        #plt.hist(erlist,bins=30)


        MIN, MAX = min(erlist), max(erlist)

        plt.hist(erlist, bins = 10 ** np.linspace(np.log10(MIN), np.log10(MAX), 50))
        plt.gca().set_xscale("log")
        #need block=True to keep plot opened
        plt.xlabel("Engagement rate")
        plt.ylabel("Number of posts")
        plt.show(block=True)



################
# variables
################

path_to_preprocessed_fb_post_file = '../fb_data/posts/preprocessed_fb_posts_20160226_follcorr.csv'
#path_to_preprocessed_fb_post_file = 'test.csv'
path_to_store_engrate_output = '../output/engrate/engrate_fb_posts_20160226_follcorr.csv'
path_to_store_labelled_fb_post = '../output/engrate/labelled_fb_posts_20160226_follcorr.csv'


if __name__ == "__main__":


    lf = LabelFbPostsEngRate()
    #lf.get_eng_rate()
    lf.label_fb_post()

    #lf.get_histogram()



'''

lines = open('../followers/user_slope_space.txt','r').readlines()

slope_dict = {}

for line in lines:
    spline = line.replace('\n','').split(',')
    slope_dict[spline[0]] = spline[1]

print ("Length of slope_dict is "+str(len(slope_dict)))



###############
# create tweet list with updated follower count
###############


lines = open('../output/engrate/_old/output_engrate_MASTER.csv','r').readlines()

tweets = []
for line in lines:
    spline = line.replace('\n','').split(',')
    tweets.append(spline)

print ("Length of tweet list is "+str(len(tweets)))

updated_tweets = []

for t in tweets:

    key = t[0]

    if key in slope_dict:

        del t[6]
        updated_tweets.append(t)

print (len(updated_tweets))

f = open('../extracted_data/space_nofollcorr.csv','w')

for ut in updated_tweets:
    f.write(','.join(ut)+'\n')

f.close()

'''

