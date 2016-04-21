__author__ = 'yi-linghwong'

import os
import sys

path_to_labelled_raw_file = '../output/engrate/others/labelled_nonprofit_raw.csv'
path_to_store_single_liwc_input_file = '../output/liwc/single_input/nonprofit.txt'

lines = open(path_to_labelled_raw_file,'r').readlines()

posts = []

for line in lines:

    spline = line.replace('\n','').split(',')
    posts.append(spline[0])


f = open(path_to_store_single_liwc_input_file,'w')

f.write(' '.join(posts))

f.close()


