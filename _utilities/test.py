__author__ = 'yi-linghwong'

import facebook
import sys
import os

if os.path.isfile('../../../keys/facebook_api_keys.txt'):
    access_token = open('../../../keys/facebook_api_keys.txt', 'r').readline()

else:
    print("Path not found")
    sys.exit(1)

graph = facebook.GraphAPI(access_token=access_token)

posts = graph.get_connections(id='LEGO', connection_name='posts', limit=5,
                                              fields='shares, message, id, type, created_time, likes.summary(true), comments.summary(true)')

for r in range(5):

    print (posts['data'][r]['id'])




