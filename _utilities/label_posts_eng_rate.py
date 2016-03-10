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

        print ("Length of post list is "+str(len(fb_posts)))

        for line in lines[:1]:
            spline = line.replace('\n','').split(',')
            length = len(spline)

        print ("Number of element per line is "+str(length))

        engrate_list = []

        print ("Calculating engagement rate...")

        for fp in fb_posts[1:]:

            if len(fp) == length:

                if with_comment == 0:

                    engagement = (0.5*int(fp[4])) + int(fp[5])

                elif with_comment == 1:

                    engagement = (0.5*int(fp[4])) + (0.8*int(fp[6])) + int(fp[5])

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


    def get_eng_rate_raw_posts(self):

        lines = open(path_to_raw_fb_post_file,'r').readlines()

        fb_posts = []

        for line in lines:
            spline = line.replace('\n','').split(',')
            fb_posts.append(spline)

        print ("Length of post list is "+str(len(fb_posts)))

        for line in lines[:1]:
            spline = line.replace('\n','').split(',')
            length = len(spline)

        print ("Number of element per line is "+str(length))

        engrate_list = []

        print ("Calculating engagement rate...")

        for fp in fb_posts[1:]:

            if len(fp) == length:

                if with_comment == 0:

                    engagement = (0.5*int(fp[4])) + int(fp[5])

                elif with_comment == 1:

                    engagement = (0.5*int(fp[4])) + (0.8*int(fp[6])) + int(fp[5])

                engrate = str((np.divide(int(engagement),int(fp[2])))*100)

                engrate_list.append([fp[0],fp[1],fp[2],fp[3],fp[4],fp[5],fp[6],engrate,fp[7],fp[8]])

            else:
                print ("error, length is "+str(len(fp)))
                print(fp)
                pass


        f = open(path_to_store_engrate_output_raw,'w')

        for el in engrate_list:
            f.write(','.join(el)+'\n')

        f.close()

        return engrate_list


    def label_fb_post(self):

        fb_posts = self.get_eng_rate()

        labelled_fb_posts = []
        high_er = []
        low_er = []

        print ("#############################")
        print ("Labelling preprocessed posts ...")

        for fp in fb_posts:

            if float(fp[7]) > her_boundary:

                labelled_fb_posts.append([fp[9],'HER'])
                high_er.append([fp[9],'HER'])

            elif float(fp[7]) < ler_boundary:

                labelled_fb_posts.append([fp[9],'LER'])
                low_er.append([fp[9],'LER'])

            else:
                pass

        print ("Length of high ER list is "+str(len(high_er)))
        print ("Length of low ER list is "+str(len(low_er)))

        f = open(path_to_store_labelled_fb_post, 'w')

        for lf in labelled_fb_posts:

            f.write(','.join(lf)+'\n')

        f.close()

        print ("Length of labelled posts is "+str(len(labelled_fb_posts)))

        return labelled_fb_posts


    def label_fb_post_raw(self):

        fb_posts = self.get_eng_rate_raw_posts()

        labelled_fb_posts = []
        high_er = []
        low_er = []

        print ("#############################")
        print ("Labelling raw posts ...")

        for fp in fb_posts:

            if float(fp[7]) > her_boundary:

                labelled_fb_posts.append([fp[9],'HER',fp[8]])
                high_er.append([fp[8],'HER'])

            elif float(fp[7]) < ler_boundary:

                labelled_fb_posts.append([fp[9],'LER',fp[8]])
                low_er.append([fp[8],'LER'])

            else:
                pass

        print ("Length of high ER list is "+str(len(high_er)))
        print ("Length of low ER list is "+str(len(low_er)))

        f = open(path_to_store_labelled_fb_post_raw, 'w')

        for lf in labelled_fb_posts:

            f.write(','.join(lf)+'\n')

        f.close()

        print ("Length of labelled posts is "+str(len(labelled_fb_posts)))

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

path_to_preprocessed_fb_post_file = '../fb_data/posts/others/preprocessed_fb_posts_nonprofit.csv'
path_to_store_engrate_output = '../output/engrate/others/engrate_nonprofit.csv'
path_to_store_labelled_fb_post = '../output/engrate/others/labelled_nonprofit.csv'

# for LIWC
path_to_raw_fb_post_file = '../fb_data/posts/others/raw_fb_posts_nonprofit.csv'
path_to_store_engrate_output_raw = '../output/engrate/others/engrate_nonprofit_raw.csv'
path_to_store_labelled_fb_post_raw = '../output/engrate/others/labelled_nonprofit_raw.csv'

# engrate parameters
with_comment = 0
her_boundary = 0.35
ler_boundary = 0.00315


if __name__ == "__main__":


    lf = LabelFbPostsEngRate()

    #lf.get_eng_rate()
    lf.label_fb_post()

    #lf.get_eng_rate_raw_posts()
    lf.label_fb_post_raw()

    #lf.get_histogram()




