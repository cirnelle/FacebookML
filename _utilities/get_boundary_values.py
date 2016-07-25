__author__ = 'yi-linghwong'

####################
# get the boundary value for demarcating between 1 and 0
# for LIWC categories
####################


import os
import sys
from matplotlib import pyplot as plt
import numpy as np
from statsmodels.robust.scale import mad
import statistics



class GetBoundaryValues():

    def create_category_lists_summary_dimensions(self):

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

        for line in lines[1:]:
            spline = line.replace('\n','').split('\t')

            if len(spline) == length:
                analytic.append(float(spline[analytic_index]))
                clout.append(float(spline[clout_index]))
                authentic.append(float(spline[authentic_index]))
                tone.append(float(spline[tone_index]))

            else:
                pass

        return analytic,clout,authentic,tone



    def get_boundary_values_summary_dimensions(self):

        lists = self.create_category_lists_summary_dimensions()
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


    def create_category_lists_grammar(self):

    ################
    # features: sixltr (six letter words), word per sentence, punctuation (exclamation and question mark)
    ################

        lines = open(path_to_liwc_result_file,'r').readlines()

        sixltr = []
        wps = []
        exclam = []
        qmark = []

        for line in lines[:1]:
            spline = line.replace('\n','').split('\t')
            length = len(spline)

            for index,s in enumerate(spline):

                if s == 'Sixltr':
                    sixltr_index = index

                if s == 'WPS':
                    wps_index = index

                if s == 'Exclam':
                    exclam_index = index

                if s == 'QMark':
                    qmark_index = index


        print ("Number of element per line is "+str(length))

        for line in lines[1:]:
            spline = line.replace('\n','').split('\t')

            if len(spline) == length:
                sixltr.append(float(spline[sixltr_index]))
                wps.append(float(spline[wps_index]))
                exclam.append(float(spline[exclam_index]))
                qmark.append(float(spline[qmark_index]))

            else:
                pass

        return sixltr,wps,exclam,qmark


    def get_boundary_value_grammar(self):

    ################
    # features: sixltr (six letter words), word per sentence, punctuation (exclamation and question mark)
    ################

        lists = self.create_category_lists_grammar()
        percentage = 0.25

        print (len(lists))

        for index,l in enumerate(lists):

            # sort the list in descending order

            sorted_list = sorted(l, reverse=True)

            # get the index for top 25%

            percentile = int(percentage*len(sorted_list))

            list_percentile = sorted_list[:percentile]

            if index == 0:

                print ("Sixltr top boundary value is "+str(list_percentile[-1]))

            if index == 1:

                print ("WPS top boundary value is "+str(list_percentile[-1]))

            if index == 2:

                print ("Exclam top boundary value is "+str(list_percentile[-1]))

            if index == 3:

                print ("QMark top boundary value is "+str(list_percentile[-1]))


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

                print ("Sixltr bottom boundary value is "+str(list_percentile[-1]))

            if index == 1:

                print ("WPS bottom boundary value is "+str(list_percentile[-1]))

            if index == 2:

                print ("Exclam bottom boundary value is "+str(list_percentile[-1]))

            if index == 3:

                print ("QMark bottom boundary value is "+str(list_percentile[-1]))


    def plot_histogram(self):


        lists = self.create_category_lists_summary_dimensions()

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

        lists = self.create_category_lists_grammar()

        for index,l in enumerate(lists):

            plt.hist(l,bins=30)

            if index == 0:

                plt.xlabel("Sixltr score")
                plt.ylabel("Number of posts")
                plt.show(block=True)

            if index == 1:

                plt.xlabel("WPS score")
                plt.ylabel("Number of posts")
                plt.show(block=True)

            if index == 2:

                plt.xlabel("Exclam score")
                plt.ylabel("Number of posts")
                plt.show(block=True)

            if index == 3:

                plt.xlabel("QMark score")
                plt.ylabel("Number of posts")
                plt.show(block=True)


    def create_category_lists_anew(self):

    ################
    # features: valence, arousal and dominance
    ################

        lines = open(path_to_anew_result_file,'r').readlines()

        valence = []
        arousal = []
        dominance = []

        for line in lines[:1]:
            spline = line.replace('\n','').split(',')
            length = len(spline)

        for line in lines:
            spline = line.replace('\n','').split(',')

            if len(spline) == length:
                valence.append(float(spline[1]))
                arousal.append(float(spline[2]))
                dominance.append(float(spline[3]))

            else:
                pass

        return valence,arousal,dominance


    def get_boundary_value_anew(self):

    ################
    # features: valence, arousal and dominance
    ################

        lists = self.create_category_lists_anew()
        percentage = 0.15

        print (len(lists))

        for index,l in enumerate(lists):

            # sort the list in descending order

            sorted_list = sorted(l, reverse=True)

            # get the index for top 25%

            percentile = int(percentage*len(sorted_list))

            list_percentile = sorted_list[:percentile]

            if index == 0:

                print ("Valence top boundary value is "+str(list_percentile[-1]))

            if index == 1:

                print ("Arousal top boundary value is "+str(list_percentile[-1]))

            if index == 2:

                print ("Dominance top boundary value is "+str(list_percentile[-1]))


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

                print ("Valence bottom boundary value is "+str(list_percentile[-1]))

            if index == 1:

                print ("Arousal bottom boundary value is "+str(list_percentile[-1]))

            if index == 2:

                print ("Dominance bottom boundary value is "+str(list_percentile[-1]))


    def plot_histogram_anew(self):

        val = self.create_category_lists_anew()[0]
        arou = self.create_category_lists_anew()[1]
        dom = self.create_category_lists_anew()[2]

        print ()
        print ("Max value for valence is "+str(max(val)))
        print ("Max value for arousal is "+str(max(arou)))
        print ("Max value for dominance is "+str(max(dom)))
        print ()

        ###############
        # Valence: get median absolute deviation to remove outliers
        ###############

        val_mad = mad(val)
        val_median = np.median(val)
        val_top_thresh = round((val_median + (5 * val_mad)),2) # 5 is just an arbitrary number we choose

        print ("MAD for valence is "+str(val_mad))
        print ("Median for valence is "+str(val_median))
        print ("Top threshold for valence is "+str(val_top_thresh))

        val_outliers = []
        valence = []

        for v in val:

            if v <= val_top_thresh:
                valence.append(v)

            else:
                val_outliers.append(v)

        print ("Number of valence outliers is "+str(len(val_outliers)))

        plt.hist(valence,bins=30)
        plt.xlabel("Valence score")
        plt.ylabel("Number of posts")
        plt.show()

        ###############
        # Arousal: get median absolute deviation to remove outliers
        ###############

        arou_mad = mad(arou)
        arou_median = np.median(arou)
        arou_top_thresh = round((arou_median + (5 * arou_mad)),2) # 5 is just an arbitrary number we choose

        print ()
        print ("MAD for arousal is "+str(arou_mad))
        print ("Median for arousal is "+str(arou_median))
        print ("Top threshold for arousal is "+str(arou_top_thresh))

        arou_outliers = []
        arousal = []

        for a in arou:

            if a <= arou_top_thresh:
                arousal.append(a)

            else:
                arou_outliers.append(a)

        print ("Number of arousal outliers is "+str(len(arou_outliers)))

        plt.hist(arousal,bins=30)
        plt.xlabel("Arousal score")
        plt.ylabel("Number of posts")
        plt.show()

        ###############
        # Dominance: get median absolute deviation to remove outliers
        ###############

        dom_mad = mad(dom)
        dom_median = np.median(dom)
        dom_top_thresh = round((dom_median + (5 * dom_mad)),2) # 5 is just an arbitrary number we choose

        print ()
        print ("MAD for dominance is "+str(dom_mad))
        print ("Median for dominance is "+str(dom_median))
        print ("Top threshold for dominance is "+str(dom_top_thresh))

        dom_outliers = []
        dominance = []

        for d in dom:

            if d <= dom_top_thresh:
                dominance.append(d)

            else:
                dom_outliers.append(d)

        print ("Number of dominance outliers is "+str(len(dom_outliers)))

        plt.hist(dominance,bins=30)
        plt.xlabel("Dominance score")
        plt.ylabel("Number of posts")
        plt.show()



##############
# variables
##############

path_to_liwc_result_file = '../output/liwc/likecorr/liwc_politics_likecorr.txt'
path_to_anew_result_file = '../output/anew/anew_nonprofit.csv'


if __name__ == '__main__':

    
    gb = GetBoundaryValues()

    #############
    # get boundary values for liwc
    #############

    #gb.create_category_lists_summary_dimensions()
    gb.get_boundary_values_summary_dimensions()

    #gb.create_category_lists_grammar()
    gb.get_boundary_value_grammar()

    #gb.plot_histogram()

    ##############
    # get boundary values for anew
    ##############

    #gb.create_category_lists_anew()
    #gb.get_boundary_value_anew()

    #gb.plot_histogram_anew()
