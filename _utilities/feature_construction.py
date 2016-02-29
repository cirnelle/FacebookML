__author__ = 'yi-linghwong'

import os
import sys

class FeatureConstruction():

    def liwc_psychometric_features(self):

        lines = open(path_to_liwc_result_file,'r').readlines()

        print (len(lines))

        for line in lines[:1]:
            spline = line.replace('\n','r').split('\t')
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

                if s == 'posemo':
                    posemo_index = index

                if s == 'negemo':
                    negemo_index = index

                if s == 'anx':
                    anx_index = index

                if s == 'anger':
                    anger_index = index

                if s == 'sad':
                    sad_index = index

                if s == 'insight':
                    insight_index = index

                if s == 'cause':
                    cause_index = index

                if s == 'discrep':
                    discrep_index = index

                if s == 'tentat':
                    tentat_index = index

                if s == 'certain':
                    certain_index = index

                if s == 'differ':
                    differ_index = index

                if s == 'see':
                    see_index = index

                if s == 'hear':
                    hear_index = index

                if s == 'feel':
                    feel_index = index

                if s == 'affiliation':
                    affiliation_index = index

                if s == 'achieve':
                    achieve_index = index

                if s == 'power':
                    power_index = index

                if s == 'reward':
                    reward_index = index

                if s == 'risk':
                    risk_index = index

                if s == 'swear':
                    swear_index = index

                if s == 'netspeak':
                    netspeak_index = index

                if s == 'assent':
                    assent_index = index

                if s == 'nonflu':
                    nonflu_index = index

                if s == 'filler':
                    filler_index = index

        print ("Number of element per line is "+str(length))

        post_features = []

        for line in lines[2:]:
            spline = line.replace('\n','r').split('\t')

            features = []

            if len(spline) == length:

                for n in range(28):

                    if n == 0:

                        if float(spline[analytic_index]) > 98.0:
                            features.append('is_analytic_yes')

                        elif float(spline[analytic_index]) < 93.0:
                            features.append('is_analytic_no')

                    if n == 1:

                        if float(spline[clout_index]) > 78.0:
                            features.append('is_clout_yes')

                        elif float(spline[clout_index]) < 50.0:
                            features.append('is_clout_no')

                    if n == 2:

                        if float(spline[authentic_index]) > 72.0:
                            features.append('is_authentic_yes')

                        elif float(spline[clout_index]) < 50.0:
                            features.append('is_authentic_no')

                    if n == 3:

                        if float(spline[tone_index]) > 84.0:
                            features.append('is_tone_yes')

                        elif float(spline[tone_index]) < 25.0:
                            features.append('is_tone_no')

                    if n == 4:

                        if float(spline[posemo_index]) > 0.0:
                            features.append('posemo_yes')

                    if n == 5:

                        if float(spline[negemo_index]) > 0.0:
                            features.append('negemo_yes')

                    if n == 6:

                        if float(spline[anx_index]) > 0.0:
                            features.append('anx_yes')

                    if n == 7:

                        if float(spline[anger_index]) > 0.0:
                            features.append('anger_yes')

                    if n == 8:

                        if float(spline[sad_index]) > 0.0:
                            features.append('sad_yes')

                    if n == 9:

                        if float(spline[insight_index]) > 0.0:
                            features.append('insight_yes')

                    if n == 10:

                        if float(spline[cause_index]) > 0.0:
                            features.append('cause_yes')

                    if n == 11:

                        if float(spline[discrep_index]) > 0.0:
                            features.append('discrep_yes')

                    if n == 12:

                        if float(spline[tentat_index]) > 0.0:
                            features.append('tentat_yes')

                    if n == 13:

                        if float(spline[certain_index]) > 0.0:
                            features.append('certain_yes')

                    if n == 14:

                        if float(spline[differ_index]) > 0.0:
                            features.append('differ_yes')

                    if n == 15:

                        if float(spline[see_index]) > 0.0:
                            features.append('see_yes')

                    if n == 16:

                        if float(spline[hear_index]) > 0.0:
                            features.append('hear_yes')

                    if n == 17:

                        if float(spline[feel_index]) > 0.0:
                            features.append('feel_yes')

                    if n == 18:

                        if float(spline[affiliation_index]) > 0.0:
                            features.append('affiliation_yes')

                    if n == 19:

                        if float(spline[achieve_index]) > 0.0:
                            features.append('achieve_yes')

                    if n == 20:

                        if float(spline[power_index]) > 0.0:
                            features.append('power_yes')

                    if n == 21:

                        if float(spline[reward_index]) > 0.0:
                            features.append('reward_yes')

                    if n == 22:

                        if float(spline[risk_index]) > 0.0:
                            features.append('risk_yes')

                    if n == 23:

                        if float(spline[swear_index]) > 0.0:
                            features.append('swear_yes')

                    if n == 24:

                        if float(spline[netspeak_index]) > 0.0:
                            features.append('netspeak_yes')

                    if n == 25:

                        if float(spline[assent_index]) > 0.0:
                            features.append('assent_yes')

                    if n == 26:

                        if float(spline[nonflu_index]) > 0.0:
                            features.append('nonflu_yes')

                    if n == 27:

                        if float(spline[filler_index]) > 0.0:
                            features.append('filler_yes')


                post_features.append(features)



            else:
                print (len(spline),line)


        print (len(post_features))

        f = open(path_to_store_psychometric_feature_file,'w')

        for pf in post_features:
            f.write(' '.join(pf)+'\n')

        f.close()


###############
# variables
###############

path_to_liwc_result_file = '../output/liwc/liwc_raw_fb_posts_20160226.txt'
#path_to_liwc_result_file = 'test.csv'
path_to_store_psychometric_feature_file = '../output/features/psychometrics.txt'



if __name__ == '__main__':

    fc = FeatureConstruction()
    fc.liwc_psychometric_features()

