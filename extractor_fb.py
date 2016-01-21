__author__ = 'yi-linghwong'


import facebook
import json
import urllib
import langdetect
import os
import sys
import time


if os.path.isfile('../../keys/facebook_api_keys.txt'):
    access_token = open('../../keys/facebook_api_keys.txt','r').readline()

else:
    print ("Path not found")
    sys.exit(1)

user_list = ['barackobama']


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


    def create_post_list(self, user, posts, post_list):

        ##############
        # creates a list of post information we want from the dict returned through API
        ##############

        #################
        # check if 'message' and 'shares' exist as keys, sometimes they don't (e.g. when page publishes a 'story' such as updating their profile pic)
        #################

        temp_list = []

        for m in range(len(posts['data'])):

            message = 'message'
            shares = 'shares'

            if message in posts['data'][m] and shares in posts['data'][m]:
                print (posts['data'][m]['id'])
                post_list.append([user, posts['data'][m]['created_time'], posts['data'][m]['id'], str(posts['data'][m]['likes']['summary']['total_count']), str(posts['data'][m]['shares']['count']), str(posts['data'][m]['comments']['summary']['total_count']), posts['data'][m]['type'], posts['data'][m]['message'].replace('\n', ' ').replace('\r', '').replace(',', ' ')])
                temp_list.append([user, posts['data'][m]['created_time'], posts['data'][m]['id'], str(posts['data'][m]['likes']['summary']['total_count']), str(posts['data'][m]['shares']['count']), str(posts['data'][m]['comments']['summary']['total_count']), posts['data'][m]['type'], posts['data'][m]['message'].replace('\n', ' ').replace('\r', '').replace(',', ' ')])

            elif message in posts['data'][m] and shares not in posts['data'][m]:
                print ("No shares for "+str(posts['data'][m]['id']))
                post_list.append([user, posts['data'][m]['created_time'], posts['data'][m]['id'], str(posts['data'][m]['likes']['summary']['total_count']), str(0), str(posts['data'][m]['comments']['summary']['total_count']), posts['data'][m]['type'], posts['data'][m]['message'].replace('\n', ' ').replace('\r', '').replace(',', ' ')])
                temp_list.append([user, posts['data'][m]['created_time'], posts['data'][m]['id'], str(posts['data'][m]['likes']['summary']['total_count']), str(0), str(posts['data'][m]['comments']['summary']['total_count']), posts['data'][m]['type'], posts['data'][m]['message'].replace('\n', ' ').replace('\r', '').replace(',', ' ')])


        ##################
        # write to file each time this function is called, so that we don't lose data if error occurs
        ##################


        f = open('test.csv', 'a')

        for tl in temp_list:
            f.write(', '.join(tl)+'\n')

        f.close()

        return post_list

    def create_comment_list(self, id, comments, comment_list):

    ##############
    # creates a list of comment information we want from the dict returned through API
    ##############

        temp_list = []

        for n in range(len(comments['data'])):

            if comments['data'][n]['message'] != '':
                #print (comments['data'][n]['id'])
                comment_list.append([id, comments['data'][n]['created_time'], comments['data'][n]['id'], str(comments['data'][n]['like_count']), comments['data'][n]['message'].replace('\n', ' ').replace('\r', '').replace(',', ' ')])
                temp_list.append([id, comments['data'][n]['created_time'], comments['data'][n]['id'], str(comments['data'][n]['like_count']), comments['data'][n]['message'].replace('\n', ' ').replace('\r', '').replace(',', ' ')])

        ##################
        # write to file each time this function is called, so that we don't lose data if error occurs
        ##################


        f = open('test1.csv', 'a')

        for tl in temp_list:
            f.write(', '.join(tl)+'\n')

        f.close()

        return comment_list


    def get_page_posts(self,graph):

        post_limit = 2
        page_limit = 6
        post_list = []
        retries = 5
        sleep_time = 50

        for user in user_list:


            posts = graph.get_connections(id=user, connection_name='posts', limit=post_limit, fields='shares, message, id, type, created_time, likes.summary(true), comments.summary(true)') #posts is a dict (with other dicts inside)

            #################
            # 'data' is the dictionary that contains the post messages, which are all in one list: data = {[message 1, message 2, ...]}
            #################

            print ("Collecting page 1 for "+user)

            post_list = self.create_post_list(user, posts, post_list)


            ################
            # the next section gets the posts for the first 'next' URL (which is retrieved with the get_connections method), and run only once
            ################


            if 'next' in posts['paging']:

                for r in range (retries):

                    print ("Collecting page 2 for "+user)

                    print ("Attempt "+str(r))

                    try:

                        url = posts['paging']['next']
                        next_url = urllib.request.urlopen(url)
                        readable_page = next_url.read()
                        next_page = json.loads(readable_page.decode())

                        post_list = self.create_post_list(user, next_page, post_list)

                        break

                    except urllib.error.HTTPError as e:
                        print ("HTTPError caught, retrying...", e.read())
                        time.sleep(sleep_time)

                    except:
                        print ("An error occurred.")
                        time.sleep(10)


            ###############
            # the next section gets the posts for the second 'next' URL onwards (which are retrieved with the urllib!)
            ###############


                for l in range(page_limit-2):

                    # check if there is a next page
                    if 'paging' in next_page:

                        print ("Collecting page "+str(l+3)+" for "+user)

            ###############
            # Try and except to catch HTTPError (Internal server error), set a maximum number of retries
            ###############

                        for r in range (retries):

                            print ("Attempt "+str(r))

                            try:

                                url = next_page['paging']['next']
                                next_url = urllib.request.urlopen(url)
                                readable_page = next_url.read()
                                next_page = json.loads(readable_page.decode())

                                post_list = self.create_post_list(user, next_page, post_list)

                                break

                            except urllib.error.HTTPError as e:
                                print ("HTTPError caught, retrying...", e.read())
                                time.sleep(sleep_time)

                            except:
                                print ("An error occurred.")
                                time.sleep(10)

                    else:
                        print ("No more next page")
                        break



        return post_list


    def get_comments(self,graph,id_list):

        comment_list = []

        for id in id_list:

            ###########
            # get comment count for the post with this id
            ###########

            print ("Getting comments for "+str(id))

            comment_obj = graph.get_object(id = id, fields = 'comments.summary(true)')
            comment_count = comment_obj['comments']['summary']['total_count']

            print ('Comment count is '+str(comment_count))

            if comment_count <= 100:
                comments_limit = comment_count
                #page_limit = 1

            else:
                comments_limit = 100
                #page_limit = int(comment_count/100)+1

            comments = graph.get_connections(id = id, connection_name='comments', limit = comments_limit, fields = 'message, id, created_time, like_count')

            ##############
            # 'data' is the dictionary that contains the post messages, which are all in one list: data = {[message 1, message 2, ...]}
            ##############

            print ('1st page with length '+str(comments_limit))


            comment_list = self.create_comment_list(id, comments, comment_list)


            ##############
            # check if there is a next comment page by checking for the key 'next' in the 'comments' dictionary obtained from get_connections method
            ##############

            if 'next' in comments['paging']:

                url = comments['paging']['next']
                next_url = urllib.request.urlopen(url)
                readable_page = next_url.read()
                next_page = json.loads(readable_page.decode())

                print ('2nd page with length '+str(len(next_page['data'])))

                comment_list = self.create_comment_list(id, next_page, comment_list)

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

                    comment_list = self.create_comment_list(id,next_page,comment_list)


        return comment_list


    def get_post_by_id(self,id):

        post = graph.get_object(id=id, fields='shares, message, id, type, created_time, likes.summary(true), comments.summary(true)')

        print ([post['created_time'], post['id'], str(post['likes']['summary']['total_count']), str(0), str(post['comments']['summary']['total_count']), post['type'], post['message'].replace('\n', ' ').replace('\r', '').replace(',', ' ')])


    def get_comment_by_id(self,id):

        comment = graph.get_object(id=id, fields = 'message, id, created_time, comments, comment_count')

        print (comment)


    def remove_duplicates(self,target_list):

        #########
        #remove duplicates by post/comment id
        #########

        list_clean = []
        temp = []
        for tl in target_list:
            if tl[2] not in temp:
                list_clean.append(tl)
                temp.append(tl[2])

        return list_clean


    def create_id_list(self):

        id_list = []

        # lines is a list of strings ['nasa, 2016-01-16, ID, message', 'nasa, 2016-01-01, ID, message', ...]
        lines = open('output/fb_posts_20160121.csv', 'r').readlines()

        for line in lines:

            spline=line.replace("\n","").split(', ')
            # spline = ['nasa', '2016-01-16', 'ID', 'message']

            id_list.append(spline[2])

        return id_list


    def write_to_file(self,list):

        f = open('test.csv', 'w')

        for l in list:
            f.write(', '.join(l)+'\n')
        f.close()


################
# connect to Facebook Graph API
################

ext = Extractor_fb()
graph = ext.connectToApi(access_token)

################
# get posts for pages
################

#posts = ext.get_page_posts(graph)


###############
# get comments for collected posts based on their id's
###############

ids = ext.create_id_list()
comments = ext.get_comments(graph,ids)


###############
# remove duplicates
###############

#clean_list = ext.remove_duplicates(posts)


###############
# get single post or comment
###############

#single_post = ext.get_post_by_id('54912575666_10153187460825667')

#single_comment = ext.get_comment_by_id('10153794959836772_10153794962046772')


#############
# write to CSV file
#############

#write_file = ext.write_to_file(posts)

