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
            spline = line.replace('\n','').split(', ')
            fb_posts.append(spline)

        print ("Length of tweet list is "+str(len(fb_posts)))

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

                if like_count <= 0:

                    like_count = pagelike_count[-1]
                    fp[2] = str(like_count)
                    updated_fb_posts.append(fp)

                else:
                    pagelike_count.append(like_count)
                    fp[2] = str(like_count)
                    updated_fb_posts.append(fp)

            else:
                #updated_tweets.append(t)
                pass

        print ("Length of updated tweet list is "+str(len(updated_fb_posts)))

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


################
# variables
################

path_to_raw_facebook_post_file = '../fb_data/posts/raw_fb_posts_20160226.csv'
path_to_slope_file = '../user_list/like_slope.txt'
path_to_store_updated_fb_post_file = '../fb_data/posts/raw_fb_post_20160226_follcorr.csv'



if __name__ == "__main__":


    ################
    # create slope dict
    ################

    lines = open(path_to_slope_file,'r').readlines()

    slope_dict = {}

    for line in lines:
        spline = line.replace('\n','').split(',')
        slope_dict[spline[0]] = spline[1]

    print ("Length of slope_dict is "+str(len(slope_dict)))

    uf = UpdatePagelikeCount()
    uf.update_fb_post_list()