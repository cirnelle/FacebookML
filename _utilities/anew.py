__author__ = 'yi-linghwong'

import os
import sys

class Anew():

    def create_anew_word_list(self):

    ###############
    # create a list of list with anew vocab and their val, aro and dom scores
    ###############

        lines = open(path_to_anew_dictionary_file,'r').readlines()

        anew_list = []

        for line in lines[1:]:

            spline = line.replace('\n','').split('\t')

            if (len(spline)) == 8:

                if spline[0].endswith('y'):

                    word = spline[0][:-1]+'ies'
                    anew_list.append([spline[0],spline[2],spline[4],spline[6]])
                    anew_list.append([word,spline[2],spline[4],spline[6]])

                elif (spline[0].endswith('s')) == False:

                    # add 's' to end of each word to account for plural and tenses
                    # some words will not make sense (e.g. 'ables'), but they also will not be detected in the posts so doesn't matter
                    word = spline[0]+'s'
                    anew_list.append([spline[0],spline[2],spline[4],spline[6]])
                    anew_list.append([word,spline[2],spline[4],spline[6]])

                else:

                    # for word already ending with 's', do nothing: don't add any variations

                    word = spline[0]
                    anew_list.append([word,spline[2],spline[4],spline[6]])


            else:
                print (spline)

        print (len(anew_list))

        return anew_list


    def create_fb_post_list(self):

        lines = open(path_to_preprocessed_labelled_fb_posts,'r').readlines()

        print (len(lines))

        posts = []

        for line in lines:

            spline = line.replace('\n','').split(',')

            # add blank space to front and end of line for each tweet, in case the ngram is the first or last word in the sentence
            # e.g. ngram = ' the end ', and the tweet is 'that is the end', if we don't add space the ngram won't be detected

            post = ' ' + spline[0] + ' '

            posts.append(post)

        print ("Length of facebook post list is "+str(len(posts)))

        return posts


    def calculate_anew_score(self):

        anew_list = self.create_anew_word_list()
        post_list = self.create_fb_post_list()

        post_score = []

        print ("Calculating anew score ...")

        for pl in post_list:

            string = pl

            valence = 0
            arousal = 0
            dominance = 0

            for al in anew_list:

                # add space to front and back of anew word so that whole word can be detected (otherwise it will detect 'duct' within 'abduction')
                substring = ' '+al[0]+' '

                if substring in string:

                    count = string.count(substring)

                    valence += (count * float(al[1]))
                    arousal += (count * float(al[2]))
                    dominance += (count * float(al[3]))

            post_score.append([pl,str(round(valence,2)),str(round(arousal,2)),str(round(dominance,2))])

        f = open(path_to_store_anew_score_file,'w')

        for ps in post_score:

            f.write(','.join(ps)+'\n')

        f.close()



#############
# variables
#############

path_to_anew_dictionary_file = '../../data_files/ANEW/ANEW2010All_variations.txt'
path_to_preprocessed_labelled_fb_posts = '../output/engrate/others/labelled_nonprofit.csv'
path_to_store_anew_score_file = '../output/anew/anew_nonprofit.csv'



if __name__ == '__main__':

    an = Anew()

    #an.create_anew_word_list()
    #an.create_fb_post_list()
    an.calculate_anew_score()


