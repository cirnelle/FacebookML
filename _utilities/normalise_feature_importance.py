__author__ = 'yi-linghwong'

import sys
import os
import numpy as np
from scipy.stats import linregress

class NormaliseFeatureImportance():

    def create_her_ler_list(self):

    #################
    # create two separate lists of all her and ler features from all fields
    #################

        lines1 = open(path_to_space_feature_score_file,'r').readlines()
        lines2 = open(path_to_politics_feature_score_file,'r').readlines()
        lines3 = open(path_to_business_feature_score_file,'r').readlines()
        lines4 = open(path_to_nonprofit_feature_score_file,'r').readlines()

        lines = lines1+lines2+lines3+lines4
        print (len(lines))

        her = []
        ler = []

        for line in lines:
            spline = line.replace('\n','').split(',')

            if spline[0] == 'HER':
                her.append(float(spline[2]))

            elif spline[0] == 'LER':
                ler.append(float(spline[2]))

            else:
                print ("error")

        return her,ler


    def get_normalisation_slope(self,featimp_list):

    #################
    # calculate the normalisation factor
    #################

        x = [min(featimp_list),max(featimp_list)]
        y = [0,1]

        #her_diff = max(her) - min(her)
        #ler_diff = max(ler) - min(ler)
        #gradient_her = 1/her_diff
        #print (gradient_her)

        #################
        # linregress method returns (slope, interception, etc)
        # first item in the list returned is the slope of the linear line
        # second item in the list is the interception, c
        #################

        slope = linregress(x, y)

        # gradient of slope

        m = slope[0]

        # intercept

        c = slope[1]

        return m,c

    def compare_science_and_others_her(self):

    #################
    # compare features in science if they exist in other fields
    # if so normalise and add to list, otherwise append 0
    #################

        her = self.create_her_ler_list()[0]

        print ("Length of science HER list is "+str(len(her)))

        # get gradient
        m = self.get_normalisation_slope(her)[0]

        # get intercept
        c = self.get_normalisation_slope(her)[1]

        ##############
        # create normalised space HER feat imp file
        ##############

        lines = open(path_to_space_feature_score_file,'r').readlines()

        space_her = []
        space_her_features = []

        for line in lines:
            spline = line.replace('\n','').split(',')

            if spline[0] == 'HER':

                space_her_features.append(spline[1])

                featimp_ori = float(spline[2])
                featimp_norm = round(((m * (featimp_ori)) + c),4)
                space_her.append('HER,'+spline[1]+','+str(featimp_norm))

        f = open(path_to_store_normalised_space_feature_file,'w')

        for sh in space_her:
            f.write(sh+'\n')

        f.close()

        ##############
        # create normalised politics HER feat imp file
        ##############

        lines = open(path_to_politics_feature_score_file,'r').readlines()

        politics_her = []

        for line in lines:
            spline = line.replace('\n','').split(',')

            if spline[1] in space_her_features:

                if spline[0] == 'HER':
                    featimp_ori = float(spline[2])
                    featimp_norm = round(((m * (featimp_ori)) + c),4)
                    politics_her.append(['HER',spline[1],featimp_norm])

                # if the feature is not a HER feature then append '0' as its feat importance
                elif spline[0] == 'LER':
                    politics_her.append(['HER',spline[1],0])


                else:
                    print ("error")

            # for HER features of politics which are not in space's HER list, just normalise and append as is
            else:

                if spline[0] == 'HER':
                    featimp_ori = float(spline[2])
                    featimp_norm = round(((m * (featimp_ori)) + c),4)
                    politics_her.append(['HER',spline[1],featimp_norm])

        politics_her.sort(key=lambda x: x[2], reverse=True)

        politics_her_sorted = []

        for ph in politics_her:
            ph[2] = str(ph[2])
            politics_her_sorted.append(ph)

        f = open(path_to_store_normalised_politics_feature_file,'w')

        for ph in politics_her_sorted:
            f.write(','.join(ph)+'\n')

        f.close()

        ##############
        # create normalised business HER feat imp file
        ##############

        lines = open(path_to_business_feature_score_file,'r').readlines()

        business_her = []

        for line in lines:
            spline = line.replace('\n','').split(',')

            if spline[1] in space_her_features:

                if spline[0] == 'HER':
                    featimp_ori = float(spline[2])
                    featimp_norm = round(((m * (featimp_ori)) + c),4)
                    business_her.append(['HER',spline[1],featimp_norm])

                # if the feature is not a HER feature then append '0' as its feat importance
                elif spline[0] == 'LER':
                    business_her.append(['HER',spline[1],0])


                else:
                    print ("error")

            # for HER features of politics which are not in space's HER list, just normalise and append as is
            else:

                if spline[0] == 'HER':
                    featimp_ori = float(spline[2])
                    featimp_norm = round(((m * (featimp_ori)) + c),4)
                    business_her.append(['HER',spline[1],featimp_norm])

        business_her.sort(key=lambda x: x[2], reverse=True)

        business_her_sorted = []

        for bh in business_her:
            bh[2] = str(bh[2])
            business_her_sorted.append(bh)

        f = open(path_to_store_normalised_business_feature_file,'w')

        for bh in business_her_sorted:
            f.write(','.join(bh)+'\n')

        f.close()

        ##############
        # create normalised nonprofit HER feat imp file
        ##############

        lines = open(path_to_nonprofit_feature_score_file,'r').readlines()

        nonprofit_her = []

        for line in lines:
            spline = line.replace('\n','').split(',')

            if spline[1] in space_her_features:

                if spline[0] == 'HER':
                    featimp_ori = float(spline[2])
                    featimp_norm = round(((m * (featimp_ori)) + c),4)
                    nonprofit_her.append(['HER',spline[1],featimp_norm])

                # if the feature is not a HER feature then append '0' as its feat importance
                elif spline[0] == 'LER':
                    nonprofit_her.append(['HER',spline[1],0])


                else:
                    print ("error")

            # for HER features of politics which are not in space's HER list, just normalise and append as is
            else:

                if spline[0] == 'HER':
                    featimp_ori = float(spline[2])
                    featimp_norm = round(((m * (featimp_ori)) + c),4)
                    nonprofit_her.append(['HER',spline[1],featimp_norm])

        nonprofit_her.sort(key=lambda x: x[2], reverse=True)

        nonprofit_her_sorted = []

        for nh in nonprofit_her:
            nh[2] = str(nh[2])
            nonprofit_her_sorted.append(nh)

        f = open(path_to_store_normalised_nonprofit_feature_file,'w')

        for nh in nonprofit_her_sorted:
            f.write(','.join(nh)+'\n')

        f.close()





################
# variables
################

path_to_space_feature_score_file = '../output/featimp_normalisation/nb/space.csv'
path_to_politics_feature_score_file = '../output/featimp_normalisation/nb/politics.csv'
path_to_business_feature_score_file = '../output/featimp_normalisation/nb/business.csv'
path_to_nonprofit_feature_score_file = '../output/featimp_normalisation/nb/nonprofit.csv'

path_to_store_normalised_space_feature_file = '../output/featimp_normalisation/nb/normalised_space.csv'
path_to_store_normalised_politics_feature_file = '../output/featimp_normalisation/nb/normalised_politics.csv'
path_to_store_normalised_business_feature_file = '../output/featimp_normalisation/nb/normalised_business.csv'
path_to_store_normalised_nonprofit_feature_file = '../output/featimp_normalisation/nb/normalised_nonprofit.csv'


if __name__ == '__main__':

    nf = NormaliseFeatureImportance()

    #nf.create_her_ler_list()
    #nf.get_normalisation_slope()
    nf.compare_science_and_others_her()

