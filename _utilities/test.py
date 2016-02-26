__author__ = 'yi-linghwong'

import facebook
import json
import urllib
import os
import sys
import time


if os.path.isfile('../../../keys/facebook_api_keys.txt'):
    access_token = open('../../../keys/facebook_api_keys.txt', 'r').readline()

else:
    print("Path not found")
    sys.exit(1)

user = 'NASA'
post_limit = 1
post_list = []

graph = facebook.GraphAPI(access_token=access_token)

posts = graph.get_connections(id=user, connection_name='posts', limit=post_limit, fields='shares, message, id, type, created_time, likes.summary(true), comments.summary(true)')

#created_date = posts['data'][0]['created_time'].strftime("%c")

print (posts['data'][0]['created_time'])

created_date = time.strptime(posts['data'][0]['created_time'],'%Y-%m-%dT%H:%M:%S+0000')

t_epoch = time.mktime(created_date)

#Mon Feb  8 17:01:03 2016

print (created_date)
print (t_epoch)

'''

__author__ = 'yi-linghwong'

#############
# Get the slope of the linear equation for a list of user
# y = mx + c, where y is number of follower, x is epoch time
#############

import sys
import os
from matplotlib import *
import matplotlib.pyplot as plt
import pylab
import numpy as np
from scipy.stats import linregress
from scipy.interpolate import interp1d
from decimal import Decimal
import time




lines = open('test.csv','r').readlines()

likecount_list = []
date = []


for line in lines:
    spline = line.replace('\n','').split(',')

    likecount_list.append(float(spline[1]))
    date.append(spline[0])

date_split = []

for d in date:
    d1 = d.replace('\n','').split(' ')

    if len(d1) == 6:
        d1.remove(d1[2])

    date_split.append(d1)


    date_epoch = []

    for ds in date_split:

        date_s = ds[1]+' '+ds[2]+' '+ds[4]

        print (date_s)


        t1 = time.strptime(date_s,'%b %d %Y')
        print (t1)
        t_epoch = time.mktime(t1)

        print (t_epoch)
        date_epoch.append(t_epoch)


'''







