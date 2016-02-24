__author__ = 'yi-linghwong'

###############
# methods for tweet preprocessing, includes:
# remove URL, RT, mention, special characters, stopwords, remove all of the above ('cleanup') plus single characters
# label tweets ('LRT', 'HRT', 'ART')
###############

import re
import os
import sys
import itertools
from sklearn.feature_extraction import text

lines = open('../../TwitterML/stopwords/stopwords.csv', 'r').readlines()

my_stopwords=[]
for line in lines:
    my_stopwords.append(line.replace("\n", ""))

stop_words = text.ENGLISH_STOP_WORDS.union(my_stopwords)


class TweetProcessing():

    def get_element_number_per_line(self):

        lines = open(path_to_raw_fb_data_file,'r').readlines()

        for line in lines[:1]:
            spline = line.replace('\n','').split(',')

        length = len(spline)

        return length


    def remove_url_mention_hashtag(self):

        lines = open(path_to_raw_fb_data_file,'r').readlines()

        posts = []
        for line in lines:

            spline = line.replace('\n','').split(',')
            posts.append(spline)

        post_list = []

        length = self.get_element_number_per_line()

        print ("Removing url, mentions and hashtags...")

        for p in posts:

            if (len(p)) == length:

                p1 = p[-1]

                #remove URLs
                p2 = re.sub(r'(?:https?\://)\S+', '', p1)

                #remove mentions
                p3 = re.sub(r'(?:\@)\S+', '', p2)

                #remove hashtags (just the symbol, not the key word)

                p4 = re.sub(r"#","", p3).strip()

                p5 = p4.lower()

                p[-1] = ' '+p5+' '

                post_list.append(p)

            else:
                print ("error")
                print (p)

        print (len(post_list))

        return post_list


    def remove_punctuations(self):

        # Replace punctuation with white space, not nil! So that words won't join together when punctuation is removed

        posts = self.remove_url_mention_hashtag()

        post_list = []

        print ("Removing punctuations ...")

        for p in posts:

            #remove special characters
            p1 = re.sub("[^A-Za-z0-9]+",' ', p[-1])
            p[-1] = p1

            post_list.append(p)

        print (len(post_list))

        return post_list


    def expand_contractions(self):

        contractions_dict = {
            ' isn\'t ': ' is not ',
            ' isn’t ': ' is not ',
            ' isnt ': ' is not ',
            ' isn ': ' is not ',
            ' aren\'t ': ' are not ',
            ' aren’t ': ' are not ',
            ' arent ': ' are not ',
            ' aren ': ' are not ',
            ' wasn\'t ': ' was not ',
            ' wasn’t ': ' was not ',
            ' wasnt ': ' was not ',
            ' wasn ': ' was not ',
            ' weren\'t ': ' were not ',
            ' weren’t ': ' were not ',
            ' werent ': ' were not ',
            ' weren ': ' were not ',
            ' haven\'t ': ' have not ',
            ' haven’t ': ' have not ',
            ' havent ': ' have not ',
            ' haven ': ' have not ',
            ' hasn\'t ': ' has not ',
            ' hasn’t ': ' has not ',
            ' hasnt ': ' has not ',
            ' hasn ': ' has not ',
            ' hadn\'t ': ' had not ',
            ' hadn’t ': ' had not ',
            ' hadnt ': ' had not ',
            ' hadn ': ' had not ',
            ' won\'t ': ' will not ',
            ' won’t ': ' will not ',
            ' wouldn\'t ': ' would not ',
            ' wouldn’t ': ' would not ',
            ' wouldnt ': ' would not ',
            ' wouldn ': ' would not ',
            ' didn\'t ': ' did not ',
            ' didn’t ': ' did not ',
            ' didnt ': ' did not ',
            ' didn ': ' did not ',
            ' don\'t ': ' do not ',
            ' don’t ': ' do not ',
            ' dont ': ' do not ',
            ' don ': ' do not ',
            ' doesn\'t ': ' does not ',
            ' doesn’t ': ' does not ',
            ' doesnt ': ' does not ',
            ' doesn ': ' does not ',
            ' can\'t ': ' can not ',
            ' can’t ': ' can not ',
            ' cant ': ' can not ',
            ' couldn\'t ': ' could not ',
            ' couldn’t ': ' could not ',
            ' couldnt ': ' could not ',
            ' couldn ': ' could not ',
            ' shouldn\'t ': ' should not ',
            ' shouldn’t ': ' should not ',
            ' shouldnt ': ' should not ',
            ' shouldn ': ' should not ',
            ' mightn\'t ': ' might not ',
            ' mightn’t ': ' might not ',
            ' mightnt ': ' might not ',
            ' mightn ': ' might not ',
            ' mustn\'t ': ' must not ',
            ' mustn’t ': ' must not ',
            ' mustnt ': ' must not ',
            ' mustn ': ' must not ',
            ' shan\'t ': ' shall not ',
            ' shan’t ': ' shall not ',
            ' shant ': ' shall not ',
            ' shan ': ' shall not ',
        }

        posts = self.remove_punctuations()
        post_list = []

        contractions_re = re.compile('(%s)' % '|'.join(contractions_dict.keys()), re.IGNORECASE)

        def replace(match):

            return contractions_dict[match.group(0).lower()]

        print ("Expanding contractions ...")

        for p in posts:

            p1 = contractions_re.sub(replace, p[-1])
            p[-1] = p1
            post_list.append(p)

        print (len(post_list))

        return post_list


    def remove_stopwords(self):

        posts = self.expand_contractions()

        post_list=[]

        print ("Removing stopwords ...")

        for p in posts:
            no_stop=[] #important

            for w in p[-1].split():
                #remove single characters and stop words
                if (len(w.lower())>=2) and (w.lower() not in stop_words):
                    no_stop.append(w.lower())


                    #join the list of words together into a string
                    p[-1] = " ".join(no_stop)

            post_list.append(p)

        print (len(post_list))

        return post_list


    def remove_duplicate(self):

        posts = self.remove_stopwords()

        post_list = []
        temp = []

        print ("Removing duplicates...")

        for p in posts:
            if p[-1] not in temp:
                temp.append(p[-1])
                post_list.append(p)

        print (len(post_list))

        return post_list


    def write_to_file(self):

        posts = self.remove_duplicate()
        length = self.get_element_number_per_line()

        print ("Number of element per line is "+str(length))

        f = open(path_to_store_processed_fb_data_file,'w')

        print ("Writing to file ...")

        for p in posts:
            if (len(p)) == length:

                f.write(','.join(p)+'\n')

            else:
                print ("error")
                print (p)

        f.close()

        return


###############
# variables
###############

path_to_raw_fb_data_file = '../fb_data/posts/raw_fb_posts_20160223.csv'
#path_to_raw_fb_data_file = 'test.csv'
path_to_store_processed_fb_data_file = '../fb_data/posts/preprocessed_fb_posts_20160223.csv'

if __name__ == "__main__":

    tp = TweetProcessing()

    tp.write_to_file()



