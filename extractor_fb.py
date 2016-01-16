__author__ = 'yi-linghwong'


import facebook
import json
import urllib
import langdetect
import os
import sys


if os.path.isfile('../../keys/facebook_api_keys.txt'):
    access_token = open('../../keys/facebook_api_keys.txt','r').readline()

else:
    print ("Path not found")
    sys.exit(1)

user_list = ['nasa', 'spacex']


class Extractor_fb():


    def printer(self,messagew,case):
        #
        # 1: info
        # 2: error
        # 3: warning


        if case == 1:
            print ("Info  ==> ",messagew)

        elif case == 2:
            print ("Error  ==> ",messagew)

        elif case == 3:
            print ("Warning  ==> ",messagew)


    def connectToApi(self,token):

        self.printer("connecting to Facebook Graph API",1)

        graph = facebook.GraphAPI(access_token = access_token)

        return graph

    def get_page_posts(self,graph):

        post_limit = 2
        page_limit = 2
        post_list = []
        id_list = []


        for user in user_list:

            posts = graph.get_connections(id=user, connection_name='posts', limit=post_limit, fields='shares, message, id, type, created_time, likes.summary(true)') #posts is a dict (with other dicts inside)


            #################
            # 'data' is the dictionary that contains the post messages, which are all in one list: data = {[message 1, message 2, ...]}
            #################

            for k in range(len(posts['data'])):

            #################
            # check if 'message' exists as a key, sometimes it doesn't (e.g. when page publishes a 'story' such as updating their profile pic)
            #################

                key = 'message'

                if key in posts['data'][k]:
                    post_list.append([user, posts['data'][k]['created_time'], posts['data'][k]['id'], str(posts['data'][k]['likes']['summary']['total_count']), str(posts['data'][k]['shares']['count']), posts['data'][k]['type'], posts['data'][k]['message'].replace('\n', ' ').replace(',', ' ')])
                    id_list.append(posts['data'][k]['id'])


            for l in range(page_limit-1):

                url = posts['paging']['next']
                next_url = urllib.request.urlopen(url)
                readable_page = next_url.read()
                next_page = json.loads(readable_page.decode())

                for m in range(len(next_page['data'])):

                    key = 'message'

                    if key in next_page['data'][m]:
                        post_list.append([user, next_page['data'][m]['created_time'], next_page['data'][m]['id'], str(next_page['data'][m]['likes']['summary']['total_count']), str(next_page['data'][m]['shares']['count']), next_page['data'][m]['type'], next_page['data'][m]['message'].replace('\n', ' ').replace(',', ' ')])
                        id_list.append(next_page['data'][m]['id'])

        return post_list, id_list


    def get_comments(self,graph,id_list):

        comment_list = []

        for id in id_list:

            ###########
            # get comment count for the post with this id
            ###########

            comment_obj = graph.get_object(id = id, fields = 'comments.summary(true)')
            comment_count = comment_obj['comments']['summary']['total_count']

            print ('Comment count is '+str(comment_count))

            if comment_count <= 100:
                comments_limit = comment_count
                #page_limit = 1

            else:
                comments_limit = 100
                #page_limit = int(comment_count/100)+1

            comments = graph.get_connections(id = id, connection_name='comments', limit = comments_limit, fields = 'message, id, created_time')

            ##############
            # 'data' is the dictionary that contains the post messages, which are all in one list: data = {[message 1, message 2, ...]}
            ##############

            print ('This is the first page with length '+str(comments_limit))

            for k in range(len(comments['data'])):

                if comments['data'][k]['message'] != '':

                    comment_list.append([id, comments['data'][k]['created_time'], comments['data'][k]['id'], comments['data'][k]['message'].replace('\n', ' ').replace(',', ' ')])


            ##############
            # check if there is a next comment page by checking for the key 'next' in the 'comments' dictionary obtained from get_connections method
            ##############

            if 'next' in comments['paging']:

                url = comments['paging']['next']
                next_url = urllib.request.urlopen(url)
                readable_page = next_url.read()
                next_page = json.loads(readable_page.decode())

                print ('This is the next page with length '+str(len(next_page['data'])))

                for m in range(len(next_page['data'])):

                    if next_page['data'][m]['message'] != '':

                        comment_list.append([id, next_page['data'][m]['created_time'], next_page['data'][m]['id'], next_page['data'][m]['message'].replace('\n', ' ').replace(',', ' ')])

            ##############
            # check if there is a next comment page by checking for the key 'next' in the 'next_page' dictionary obtained from URL
            # Important! While loop has to be under the if statement above
            ##############

                while 'next' in next_page['paging']:

                    url = next_page['paging']['next']
                    next_url = urllib.request.urlopen(url)
                    readable_page = next_url.read()
                    next_page = json.loads(readable_page.decode())

                    print (len(next_page['data']))

                    for n in range(len(next_page['data'])):

                        if next_page['data'][n]['message'] != '':

                            comment_list.append([id, next_page['data'][n]['created_time'], next_page['data'][n]['id'], next_page['data'][n]['message'].replace('\n', ' ').replace(',', ' ')])


        #########
        #remove duplicates by comment id
        #########

        comment_list_clean = []
        temp = []
        for cl in comment_list:
            if cl[2] not in temp:
                comment_list_clean.append(cl)
                temp.append(cl[2])

        return comment_list_clean


    def write_to_file(self,list):

        f = open('test.csv', 'w')

        for l in list:
            f.write(', '.join(l)+'\n')
        f.close()


ext = Extractor_fb()
graph = ext.connectToApi(access_token)
posts = ext.get_page_posts(graph)[0]
ids = ext.get_page_posts(graph)[1]
comments = ext.get_comments(graph,ids)

write_file = ext.write_to_file(comments)

