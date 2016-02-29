__author__ = 'yi-linghwong'

####################
# get the boundary value for demarcating between 1 and 0
# for LIWC categories
####################


import os
import sys
from matplotlib import pyplot as plt
import numpy as np


class GetLIWCBoundaryValues():

    def create_category_lists(self):


        lines = open(path_to_liwc_result_file,'r').readlines()

        analytic = []
        clout = []
        authentic = []
        tone = []

        for line in lines[:1]:
            spline = line.replace('\n','').split('\t')
            length = len(spline)

            for index,s in enumerate(spline):

                if s == 'Analytic':
                    analytic_index = index

                if s == 'Clout':
                    clout_index = index

                if s == 'Authentic':
                    authentic_index = index

                if s == 'Tone':
                    tone_index = index


        print ("Number of element per line is "+str(length))

        for line in lines[2:]:
            spline = line.replace('\n','').split('\t')

            if len(spline) == length:
                analytic.append(float(spline[analytic_index]))
                clout.append(float(spline[clout_index]))
                authentic.append(float(spline[authentic_index]))
                tone.append(float(spline[tone_index]))

            else:
                pass

        return analytic,clout,authentic,tone



    def get_boundary_values(self):

        lists = self.create_category_lists()
        percentage = 0.25

        print (len(lists))

        for index,l in enumerate(lists):

            # sort the list in descending order

            sorted_list = sorted(l, reverse=True)

            # get the index for top 25%

            percentile = int(percentage*len(sorted_list))

            list_percentile = sorted_list[:percentile]

            if index == 0:

                print ("Analytic top boundary value is "+str(list_percentile[-1]))

            if index == 1:

                print ("Clout top boundary value is "+str(list_percentile[-1]))

            if index == 2:

                print ("Authentic top boundary value is "+str(list_percentile[-1]))

            if index == 3:

                print ("Tone top boundary value is "+str(list_percentile[-1]))


        ##############
        # get bottom boundary values
        ##############

        print ("############################")


        for index,l in enumerate(lists):

            # sort the list in ascending order

            sorted_list = sorted(l)

            # get the index for top 25%

            percentile = int(percentage*len(sorted_list))

            list_percentile = sorted_list[:percentile]

            if index == 0:

                print ("Analytic bottom boundary value is "+str(list_percentile[-1]))

            if index == 1:

                print ("Clout bottom boundary value is "+str(list_percentile[-1]))

            if index == 2:

                print ("Authentic bottom boundary value is "+str(list_percentile[-1]))

            if index == 3:

                print ("Tone bottom boundary value is "+str(list_percentile[-1]))


    def plot_histogram(self):


        lists = self.create_category_lists()

        for index,l in enumerate(lists):

            plt.hist(l,bins=30)

            if index == 0:

                plt.xlabel("Analytic score")
                plt.ylabel("Number of posts")
                plt.show(block=True)

            if index == 1:

                plt.xlabel("Clout score")
                plt.ylabel("Number of posts")
                plt.show(block=True)

            if index == 2:

                plt.xlabel("Authentic score")
                plt.ylabel("Number of posts")
                plt.show(block=True)

            if index == 3:

                plt.xlabel("Tone score")
                plt.ylabel("Number of posts")
                plt.show(block=True)


##############
# variables
##############

path_to_liwc_result_file = '../output/liwc/liwc_raw_fb_posts_20160226.txt'


if __name__ == '__main__':

    
    gb = GetLIWCBoundaryValues()

    #gb.create_category_lists()
    gb.get_boundary_values()
    #gb.plot_histogram()
