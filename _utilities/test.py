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

created_date = posts['data'][0]['created_time'].strftime("%c")


print (created_date)






