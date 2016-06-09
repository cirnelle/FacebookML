#!/usr/local/bin/python3

import os
import sys
import time
import facebook

#################
# Get Facebook API access token
#################


if os.path.isfile('../../../keys/facebook_api_keys.txt'):
    access_token = open('../../../keys/facebook_api_keys.txt','r').readline()

else:
    print ("Path not found")
    sys.exit(1)


################
# Construct user list from txt file
################


lines = open('user_ALL','r').readlines()

user_list = []

for line in lines:
    spline = line.replace('\n', '').split(',')
    user_list.append(spline[0])


graph = facebook.GraphAPI(access_token = access_token)


for ul in user_list:

    try:

        user = graph.get_object(id=ul, fields='likes')

        now = time.strftime("%c")

        f = open("likes/" + ul + ".txt", 'a')

        f.write(str(now) + ',' + str(user['likes']) + '\n')

        f.close()

        time.sleep(1)

    except Exception as e:
        print('Failed: ' + str(e))
        time.sleep(5)

