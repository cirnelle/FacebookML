__author__ = 'yi-linghwong'

###############
# class to recalculate feature score by putting more weights on features
# which are validated by more classifiers, before they are normalised
# features which are validated by 3 classifiers are multiplied by 3
# by 2 classifiers by 2
###############


import os
import sys

class RecalculateFeatureScore():

    def get_weighty_features(self):



        pass


################
# variables
################

path_to_nb_feature_score_file = '../output/featimp_normalisation/nb/space.csv'
path_to_sgd_feature_score_file = '../output/featimp_normalisation/sgd/space.csv'
path_to_extratree_feature_score_file = '../output/featimp_normalisation/extratree/space.csv'

if __name__ == '__main__':

    rc = RecalculateFeatureScore()
    rc.get_weighty_features()