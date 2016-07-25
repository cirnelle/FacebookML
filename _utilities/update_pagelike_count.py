__author__ = 'yi-linghwong'


###############
# compute a updated pagelike count (extrapolation based on a linear equation)
# for a list of facebook post
###############


import os
import sys
import time


class UpdatePagelikeCount():


    def update_fb_post_list(self):

        ###############
        # create tweet list with updated follower count
        ###############

        lines = open(path_to_raw_facebook_post_file,'r').readlines()

        fb_posts = []
        for line in lines:
            spline = line.replace('\n','').split(',')
            fb_posts.append(spline)

        print ("Length of post list is "+str(len(fb_posts)))

        unique_user = []
        updated_fb_posts = []
        pagelike_count = []

        for fp in fb_posts[1:]:

            key = fp[0]

            if key in slope_dict:


                if fp[0] not in unique_user:
                    unique_user.append(fp[0])
                    t1 = fp[1]
                    t2 = time.strptime(t1,'%Y-%m-%dT%H:%M:%S+0000')
                    t_max = time.mktime(t2)

                like_count = self.compute_pagelike_count(fp[0],fp[1],t_max,fp[2])

                #if like_count <= 0:
                if like_count <= (0.09 * float(fp[2])):

                    like_count = pagelike_count[-1]
                    fp[2] = str(like_count)
                    updated_fb_posts.append(fp)

                else:
                    pagelike_count.append(like_count)
                    fp[2] = str(like_count)
                    updated_fb_posts.append(fp)

            else:
                #updated_tweets.append(t)
                print (key)
                print ("key not found")
                pass

        print ("Length of updated post list is "+str(len(updated_fb_posts)))

        header = ['user','created_time','page_likes','post_id','like_count','share_count','comment_count','type','message']
        updated_fb_posts.insert(0,header)

        f = open(path_to_store_updated_fb_post_file,'w')

        for ufp in updated_fb_posts:
            f.write(','.join(ufp)+'\n')

        f.close()

        return updated_fb_posts



    def compute_pagelike_count(self,user,date,t_max,pagelike_count_max):

        ###############
        # function to compute pagelike count, taking the tweet date and latest follower count as arguments
        ###############


        t1 = time.strptime(date,'%Y-%m-%dT%H:%M:%S+0000')
        t_epoch = time.mktime(t1)

        t_delta = t_max - t_epoch

        slope = float(slope_dict[user])

        y_delta = slope*t_delta

        pagelike_count = float(pagelike_count_max) - y_delta

        pagelike_count = int(pagelike_count)

        #print ("Updated foll count is "+str(int(foll_count)))

        return pagelike_count


    def update_likecount_with_real_numbers(self):

        lines1 = open(path_to_raw_facebook_post_file, 'r').readlines()

        users = []

        for line in lines1[1:]:
            spline = line.rstrip('\n').split(',')

            if spline[0] not in users:
                users.append(spline[0])

        print (len(users))

        updated_posts = []

        for u in users:

            print(u)

            ##################
            # get the dates for follcount file
            ##################

            lines2 = open(path_to_likecount_files + u + '.txt')

            date_dict = {}

            for line in lines2:
                spline = line.rstrip('\n').split(',')

                if spline == ['']:
                    print("error")
                    break

                d1 = spline[0].replace('\n', '').split(' ')

                if len(d1) == 6:
                    d1.remove(d1[2])

                date_s = d1[1] + ' ' + d1[2] + ' ' + d1[4]

                t1 = time.strptime(date_s, '%b %d %Y')
                t_epoch = time.mktime(t1)
                date_dict[t_epoch] = spline[1]


            #################
            # get the dates for raw tweet file
            #################

            user_posts = []

            for line in lines1[2:]:
                spline = line.rstrip('\n').split(',')

                if spline[0] == u:

                    d1 = spline[1].replace('\n', '').split('T')

                    date_s = d1[0]

                    t1 = time.strptime(date_s, '%Y-%m-%d')
                    t_epoch = time.mktime(t1)


                    if t_epoch in date_dict:

                        if date_dict[t_epoch] != 'nan':

                            spline[2] = date_dict[t_epoch]
                            user_posts.append(spline)

                            updated_posts.append(spline)

            print(len(user_posts))

        print(" ")

        print(len(updated_posts))

        f = open(path_to_store_reallike_fb_post_file, 'w')

        for up in updated_posts:
            f.write(','.join(up) + '\n')

        f.close()


################
# variables
################

path_to_raw_facebook_post_file = '../fb_data/posts/others/old/raw_fb_posts_politics.csv'
path_to_slope_file = '../user_list/slope/user_slope_politics.txt'
path_to_store_updated_fb_post_file = '../fb_data/posts/likecorr/others/raw_fb_posts_politics_likecorr.csv'

path_to_likecount_files = '../user_list/likes/'
path_to_store_reallike_fb_post_file = '../fb_data/posts/reallike/raw_fb_posts_nonprofit_reallike.csv'


if __name__ == "__main__":


    ################
    # create slope dict and update like count
    ################

    lines = open(path_to_slope_file,'r').readlines()

    slope_dict = {}

    for line in lines:
        spline = line.replace('\n','').split(',')
        slope_dict[spline[0]] = spline[1]

    print (slope_dict)

    print ("Length of slope_dict is "+str(len(slope_dict)))

    uf = UpdatePagelikeCount()
    uf.update_fb_post_list()


    #################
    # update like count with real data mined daily
    #################

    # uf = UpdatePagelikeCount()
    # uf.update_likecount_with_real_numbers()