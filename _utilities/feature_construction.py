__author__ = 'yi-linghwong'

import os
import sys

class FeatureConstruction():

    def liwc_features(self):

        lines = open(path_to_liwc_result_file,'r').readlines()

        post_features = []

        for line in lines[:1]:
            spline = line.replace('\n','r').split('\t')
            length = len(spline)


        for line in lines[2:]:
            spline = line.replace('\n','r').split('\t')

            if len(spline) == length:



            else:
                print (line)





###############
# variables
###############

path_to_liwc_result_file = '../output/liwc/liwc_raw_fb_posts_20160226.txt'



if __name__ == '__main__':

    fc = FeatureConstruction()

