__author__ = 'yi-linghwong'

import os
import sys

class FeatureConstruction():

    def liwc_psychometric_features(self):

        lines = open(path_to_liwc_result_file,'r').readlines()

        print ()
        print ("Constructing psychometric features...")

        print (len(lines))

        for line in lines[:1]:
            spline = line.replace('\n','').split('\t')
            length = len(spline)

            for index,s in enumerate(spline):

                if s == 'Analytic':
                    analytic_index = index

                if s == 'Clout':
                    clout_index = index

                if s == 'Authentic':
                    authentic_index = index

                if s == 'Tone':
                    tone_index = index

                if s == 'posemo':
                    posemo_index = index

                if s == 'negemo':
                    negemo_index = index

                if s == 'anx':
                    anx_index = index

                if s == 'anger':
                    anger_index = index

                if s == 'sad':
                    sad_index = index

                if s == 'insight':
                    insight_index = index

                if s == 'cause':
                    cause_index = index

                if s == 'discrep':
                    discrep_index = index

                if s == 'tentat':
                    tentat_index = index

                if s == 'certain':
                    certain_index = index

                if s == 'differ':
                    differ_index = index

                if s == 'see':
                    see_index = index

                if s == 'hear':
                    hear_index = index

                if s == 'feel':
                    feel_index = index

                if s == 'affiliation':
                    affiliation_index = index

                if s == 'achieve':
                    achieve_index = index

                if s == 'power':
                    power_index = index

                if s == 'reward':
                    reward_index = index

                if s == 'risk':
                    risk_index = index

                if s == 'swear':
                    swear_index = index

                if s == 'netspeak':
                    netspeak_index = index

                if s == 'assent':
                    assent_index = index

                if s == 'nonflu':
                    nonflu_index = index

                if s == 'filler':
                    filler_index = index

        print ("Number of element per line is "+str(length))

        post_features = []

        for line in lines[1:]:
            spline = line.replace('\n','').split('\t')

            features = []

            if len(spline) == length:

                for n in range(28):

                    if n == 0:

                        if float(spline[analytic_index]) > analytic_top:
                            features.append('is_analytic_yes')

                        elif float(spline[analytic_index]) < analytic_bottom:
                            features.append('is_analytic_no')

                    if n == 1:

                        if float(spline[clout_index]) > clout_top:
                            features.append('is_clout_yes')

                        elif float(spline[clout_index]) < clout_bottom:
                            features.append('is_clout_no')

                    if n == 2:

                        if float(spline[authentic_index]) > authentic_top:
                            features.append('is_authentic_yes')

                        elif float(spline[authentic_index]) < authentic_bottom:
                            features.append('is_authentic_no')

                    if n == 3:

                        if float(spline[tone_index]) > tone_top:
                            features.append('is_tone_yes')

                        elif float(spline[tone_index]) < tone_bottom:
                            features.append('is_tone_no')

                    if n == 4:

                        if float(spline[posemo_index]) > 0.0:
                            features.append('posemo_yes')

                    if n == 5:

                        if float(spline[negemo_index]) > 0.0:
                            features.append('negemo_yes')

                    if n == 6:

                        if float(spline[anx_index]) > 0.0:
                            features.append('anx_yes')

                    if n == 7:

                        if float(spline[anger_index]) > 0.0:
                            features.append('anger_yes')

                    if n == 8:

                        if float(spline[sad_index]) > 0.0:
                            features.append('sad_yes')

                    if n == 9:

                        if float(spline[insight_index]) > 0.0:
                            features.append('insight_yes')

                    if n == 10:

                        if float(spline[cause_index]) > 0.0:
                            features.append('cause_yes')

                    if n == 11:

                        if float(spline[discrep_index]) > 0.0:
                            features.append('discrep_yes')

                    if n == 12:

                        if float(spline[tentat_index]) > 0.0:
                            features.append('tentat_yes')

                    if n == 13:

                        if float(spline[certain_index]) > 0.0:
                            features.append('certain_yes')

                    if n == 14:

                        if float(spline[differ_index]) > 0.0:
                            features.append('differ_yes')

                    if n == 15:

                        if float(spline[see_index]) > 0.0:
                            features.append('see_yes')

                    if n == 16:

                        if float(spline[hear_index]) > 0.0:
                            features.append('hear_yes')

                    if n == 17:

                        if float(spline[feel_index]) > 0.0:
                            features.append('feel_yes')

                    if n == 18:

                        if float(spline[affiliation_index]) > 0.0:
                            features.append('affiliation_yes')

                    if n == 19:

                        if float(spline[achieve_index]) > 0.0:
                            features.append('achieve_yes')

                    if n == 20:

                        if float(spline[power_index]) > 0.0:
                            features.append('power_yes')

                    if n == 21:

                        if float(spline[reward_index]) > 0.0:
                            features.append('reward_yes')

                    if n == 22:

                        if float(spline[risk_index]) > 0.0:
                            features.append('risk_yes')

                    if n == 23:

                        if float(spline[swear_index]) > 0.0:
                            features.append('swear_yes')

                    if n == 24:

                        if float(spline[netspeak_index]) > 0.0:
                            features.append('netspeak_yes')

                    if n == 25:

                        if float(spline[assent_index]) > 0.0:
                            features.append('assent_yes')

                    if n == 26:

                        if float(spline[nonflu_index]) > 0.0:
                            features.append('nonflu_yes')

                    if n == 27:

                        if float(spline[filler_index]) > 0.0:
                            features.append('filler_yes')


                if len(features) == 0:
                    print("No feature for this post")
                    print (spline[0])
                    features.append('none')

                post_features.append(features)

            else:
                print ("Length of spline incorrect")
                print (len(spline),line)


        print (len(post_features))

        f = open(path_to_store_psychometric_feature_file,'w')

        for pf in post_features:
            f.write(' '.join(pf)+'\n')

        f.close()


    def liwc_grammar_features(self):

    ################
    # features: sixltr (six letter words), word per sentence, punctuation (exclamation and question mark)
    ################

        lines = open(path_to_liwc_result_file,'r').readlines()

        print ()
        print ("Constructing grammar features...")

        print (len(lines))

        for line in lines[:1]:
            spline = line.replace('\n','').split('\t')
            length = len(spline)

            for index,s in enumerate(spline):

                if s == 'Sixltr':
                    sixltr_index = index

                if s == 'WPS':
                    wps_index = index

                if s == 'Exclam':
                    exclam_index = index

                if s == 'QMark':
                    qmark_index = index

        print ("Number of element per line is "+str(length))

        post_features = []

        for line in lines[1:]:
            spline = line.replace('\n','').split('\t')

            features = []

            if len(spline) == length:

                for n in range(4):

                    if n == 0:

                        if float(spline[sixltr_index]) > sixltr_top:
                            features.append('many_sixltr')

                        elif float(spline[sixltr_index]) < sixltr_bottom:
                            features.append('few_sixltr')

                    if n == 1:

                        if float(spline[wps_index]) > wps_top:
                            features.append('high_wps')

                        elif float(spline[wps_index]) < wps_bottom:
                            features.append('low_wps')

                    if n == 2:

                        if float(spline[exclam_index]) > 0.0:
                            features.append('has_exclam')

                        else:
                            features.append('no_exclam')

                    if n == 3:

                        if float(spline[qmark_index]) > 0.0:
                            features.append('has_qmark')

                        else:
                            features.append('no_qmark')

                if len(features) == 0:
                    print("No feature for this post")
                    print (spline[0])
                    features.append('none')

                post_features.append(features)

            else:
                print ("Length of spline incorrect")
                print (len(spline),line)


        print (len(post_features))

        f = open(path_to_store_grammar_feature_file,'w')

        for pf in post_features:
            f.write(' '.join(pf)+'\n')

        f.close()


    def url_hashtag_type_feature(self):

        lines = open(path_to_labelled_raw_file,'r').readlines()

        print ()
        print ("Constructing social media features...")

        posts = []

        for line in lines:
            spline = line.replace('\n','').split(',')
            posts.append(spline)

        print ("Length of posts is "+str(len(posts)))

        post_features = []
        url_list = []
        hashtag_list = []

        for p in posts:
            features = []

            #append the type (i.e. photo, video, link, etc)

            features.append('type_'+p[2])

            ################
            #replace special character at end of sentence with white space
            #so that hashtags without a space in front of them can be detected too (e.g. This is it.#space)
            ################

            p[0] = p[0].replace(',',' ').replace('.',' ').replace('!',' ').replace('?',' ')

            ################
            # need two different loops and a 'break' after detecting the first symbol
            # so that there will be no repeated features when there are more than one hashtags/urls
            ################

            for word in p[0].split():
                if word.startswith("#"):
                    features.append("has_hashtag")
                    hashtag_list.append(word)
                    break

            for word in p[0].split():
                if word.startswith("http://") or word.startswith("https://"):
                    features.append("has_url")
                    url_list.append(word)
                    break


            if len(features) == 0:
                print("No feature for this post")
                print (p[0])
                features.append('none')


            features = ' '.join(features)

            # append the label to the list
            post_features.append([features,p[1]])

        print ("Length of post features list is "+str(len(post_features)))
        print ("Length of url list is "+str(len(url_list)))
        print ("Length of hashtag list is "+str(len(hashtag_list)))

        f = open(path_to_store_labelled_urlhashtagtype_file,'w')

        for pf in post_features:
            f.write(','.join(pf)+'\n')

        f.close()


    def anew_features(self):

    ##################
    # get anew features (valence, arousal and dominance)
    ##################

        lines = open(path_to_anew_result_file,'r').readlines()

        anew_features = []

        for line in lines:

            spline = line.replace('\n','').split(',')

            features = []

            if len(spline) == 4:

                for n in range(3):

                    if n == 0:

                        if float(spline[1]) > valence_top:
                            features.append('high_valence')

                        elif float(spline[1]) < valence_bottom:
                            features.append('low_valence')

                    if n == 1:

                        if float(spline[2]) > arousal_top:
                            features.append('high_arousal')

                        elif float(spline[2]) < arousal_bottom:
                            features.append('low_arousal')

                    if n == 2:

                        if float(spline[3]) > dominance_top:
                            features.append('high_dominance')

                        elif float(spline[3]) < dominance_bottom:
                            features.append('low_dominance')

                if len(features) == 0:
                    features.append('anew_neutral')

            anew_features.append(features)

        f = open(path_to_store_anew_feature_file,'w')

        for af in anew_features:
            f.write(' '.join(af)+'\n')

        f.close()


    def combine_features(self):

    ################
    # combine psychometrics, grammar and SM (url, hashtags, type) features
    ################

        lines = open(path_to_liwc_result_file,'r').readlines()

        print ()
        print ("Constructing combined features...")

        print (len(lines))

        for line in lines[:1]:
            spline = line.replace('\n','').split('\t')
            length = len(spline)

            for index,s in enumerate(spline):

                if s == 'Analytic':
                    analytic_index = index

                if s == 'Clout':
                    clout_index = index

                if s == 'Authentic':
                    authentic_index = index

                if s == 'Tone':
                    tone_index = index

                if s == 'posemo':
                    posemo_index = index

                if s == 'negemo':
                    negemo_index = index

                if s == 'anx':
                    anx_index = index

                if s == 'anger':
                    anger_index = index

                if s == 'sad':
                    sad_index = index

                if s == 'insight':
                    insight_index = index

                if s == 'cause':
                    cause_index = index

                if s == 'discrep':
                    discrep_index = index

                if s == 'tentat':
                    tentat_index = index

                if s == 'certain':
                    certain_index = index

                if s == 'differ':
                    differ_index = index

                if s == 'see':
                    see_index = index

                if s == 'hear':
                    hear_index = index

                if s == 'feel':
                    feel_index = index

                if s == 'affiliation':
                    affiliation_index = index

                if s == 'achieve':
                    achieve_index = index

                if s == 'power':
                    power_index = index

                if s == 'reward':
                    reward_index = index

                if s == 'risk':
                    risk_index = index

                if s == 'swear':
                    swear_index = index

                if s == 'netspeak':
                    netspeak_index = index

                if s == 'assent':
                    assent_index = index

                if s == 'nonflu':
                    nonflu_index = index

                if s == 'filler':
                    filler_index = index

                if s == 'Sixltr':
                    sixltr_index = index

                if s == 'WPS':
                    wps_index = index

                if s == 'Exclam':
                    exclam_index = index

                if s == 'QMark':
                    qmark_index = index

        print ("Number of element per line is "+str(length))

        post_features = []

        for line in lines[1:]:
            spline = line.replace('\n','').split('\t')

            features = []

            if len(spline) == length:

                for n in range(32):

                    if n == 0:

                        if float(spline[analytic_index]) > analytic_top:
                            features.append('is_analytic_yes')

                        elif float(spline[analytic_index]) < analytic_bottom:
                            features.append('is_analytic_no')

                    if n == 1:

                        if float(spline[clout_index]) > clout_top:
                            features.append('is_clout_yes')

                        elif float(spline[clout_index]) < clout_bottom:
                            features.append('is_clout_no')

                    if n == 2:

                        if float(spline[authentic_index]) > authentic_top:
                            features.append('is_authentic_yes')

                        elif float(spline[authentic_index]) < authentic_bottom:
                            features.append('is_authentic_no')

                    if n == 3:

                        if float(spline[tone_index]) > tone_top:
                            features.append('is_tone_yes')

                        elif float(spline[tone_index]) < tone_bottom:
                            features.append('is_tone_no')

                    if n == 4:

                        if float(spline[posemo_index]) > 0.0:
                            features.append('posemo_yes')

                    if n == 5:

                        if float(spline[negemo_index]) > 0.0:
                            features.append('negemo_yes')

                    if n == 6:

                        if float(spline[anx_index]) > 0.0:
                            features.append('anx_yes')

                    if n == 7:

                        if float(spline[anger_index]) > 0.0:
                            features.append('anger_yes')

                    if n == 8:

                        if float(spline[sad_index]) > 0.0:
                            features.append('sad_yes')

                    if n == 9:

                        if float(spline[insight_index]) > 0.0:
                            features.append('insight_yes')

                    if n == 10:

                        if float(spline[cause_index]) > 0.0:
                            features.append('cause_yes')

                    if n == 11:

                        if float(spline[discrep_index]) > 0.0:
                            features.append('discrep_yes')

                    if n == 12:

                        if float(spline[tentat_index]) > 0.0:
                            features.append('tentat_yes')

                    if n == 13:

                        if float(spline[certain_index]) > 0.0:
                            features.append('certain_yes')

                    if n == 14:

                        if float(spline[differ_index]) > 0.0:
                            features.append('differ_yes')

                    if n == 15:

                        if float(spline[see_index]) > 0.0:
                            features.append('see_yes')

                    if n == 16:

                        if float(spline[hear_index]) > 0.0:
                            features.append('hear_yes')

                    if n == 17:

                        if float(spline[feel_index]) > 0.0:
                            features.append('feel_yes')

                    if n == 18:

                        if float(spline[affiliation_index]) > 0.0:
                            features.append('affiliation_yes')

                    if n == 19:

                        if float(spline[achieve_index]) > 0.0:
                            features.append('achieve_yes')

                    if n == 20:

                        if float(spline[power_index]) > 0.0:
                            features.append('power_yes')

                    if n == 21:

                        if float(spline[reward_index]) > 0.0:
                            features.append('reward_yes')

                    if n == 22:

                        if float(spline[risk_index]) > 0.0:
                            features.append('risk_yes')

                    if n == 23:

                        if float(spline[swear_index]) > 0.0:
                            features.append('swear_yes')

                    if n == 24:

                        if float(spline[netspeak_index]) > 0.0:
                            features.append('netspeak_yes')

                    if n == 25:

                        if float(spline[assent_index]) > 0.0:
                            features.append('assent_yes')

                    if n == 26:

                        if float(spline[nonflu_index]) > 0.0:
                            features.append('nonflu_yes')

                    if n == 27:

                        if float(spline[filler_index]) > 0.0:
                            features.append('filler_yes')

                    if n == 28:

                        if float(spline[sixltr_index]) > sixltr_top:
                            features.append('many_sixltr')

                        elif float(spline[sixltr_index]) < sixltr_bottom:
                            features.append('few_sixltr')

                    if n == 29:

                        if float(spline[wps_index]) > wps_top:
                            features.append('high_wps')

                        elif float(spline[wps_index]) < wps_bottom:
                            features.append('low_wps')

                    if n == 30:

                        if float(spline[exclam_index]) > 0.0:
                            features.append('has_exclam')

                    if n == 31:

                        if float(spline[qmark_index]) > 0.0:
                            features.append('has_qmark')


                if len(features) == 0:
                    print("No feature for this post")
                    print (spline[0])
                    features.append('none')

                features = ' '.join(features)

                post_features.append(features)

            else:
                print ("Length of spline incorrect")
                print (len(spline),line)


        ##############
        # get url hashtag type features
        ##############

        lines = open(path_to_labelled_raw_file,'r').readlines()

        posts = []

        for line in lines:
            spline = line.replace('\n','').split(',')
            posts.append(spline)

        print ("Length of posts is "+str(len(posts)))

        post_features_sm = []
        url_list = []
        hashtag_list = []

        for p in posts:
            features_sm = []

            #append the type (i.e. photo, video, link, etc)

            features_sm.append('type_'+p[2])

            ################
            #replace special character at end of sentence with white space
            #so that hashtags without a space in front of them can be detected too (e.g. This is it.#space)
            ################

            p[0] = p[0].replace(',',' ').replace('.',' ').replace('!',' ').replace('?',' ')

            ################
            # need two different loops and a 'break' after detecting the first symbol
            # so that there will be no repeated features when there are more than one hashtags/urls
            ################

            for word in p[0].split():
                if word.startswith("#"):
                    features_sm.append("has_hashtag")
                    hashtag_list.append(word)
                    break

            for word in p[0].split():
                if word.startswith("http://") or word.startswith("https://"):
                    features_sm.append("has_url")
                    url_list.append(word)
                    break


            features_sm = ' '.join(features_sm)

            post_features_sm.append(features_sm)

        '''
        #################
        # get ANEW features
        #################

        lines = open(path_to_anew_result_file,'r').readlines()

        post_features_anew = []

        for line in lines:

            spline = line.replace('\n','').split(',')

            features_anew = []

            if len(spline) == 4:

                for n in range(2):


                    if n == 0:

                        if float(spline[1]) > valence_top:
                            features_anew.append('high_valence')

                        elif float(spline[1]) < valence_bottom:
                            features_anew.append('low_valence')


                    if n == 0:

                        if float(spline[2]) > arousal_top:
                            features_anew.append('high_arousal')

                        elif float(spline[2]) < arousal_bottom:
                            features_anew.append('low_arousal')


                    if n == 1:

                        if float(spline[3]) > dominance_top:
                            features_anew.append('high_dominance')

                        elif float(spline[3]) < dominance_bottom:
                            features_anew.append('low_dominance')


                if len(features_anew) == 0:
                    features_anew.append('anew_neutral')

                features_anew = ' '.join(features_anew)

            post_features_anew.append(features_anew)

        '''
        print ("Length of liwc feature list is "+str(len(post_features)))
        print ("Length of sm feature list is "+str(len(post_features_sm)))
        #print ("Length of anew features list is "+str(len(post_features_anew)))


        if len(post_features) == len(post_features_sm):

            zipped = zip(post_features,post_features_sm)

        else:
            print ("Length of both lists not equal, exiting...")
            sys.exit()

        combined_features = []

        for z in zipped:
            z = list(z)
            z = ' '.join(z)
            combined_features.append(z)

        print ("Length of combined list is "+str(len(combined_features)))


        f = open(path_to_store_combined_feature_file,'w')

        for cf in combined_features:
            f.write(cf+'\n')

        f.close()

        return combined_features


    def combine_features_all(self):

    ##################
    # combine all features: psychometrics, grammar, SM, words
    ##################

        print ()
        print ("Constructing combine ALL features...")

        language_features = self.combine_features()

        lines = open(path_to_labelled_preprocessed_file,'r').readlines()

        word_features = []

        for line in lines:
            spline = line.replace('\n','').split(',')
            word_features.append(spline[0])

        print ("############################")
        print ("Length of language feature list is "+str(len(language_features)))
        print ("Length of word feature list is "+str(len(word_features)))

        if len(language_features) == len(word_features):
            zipped = zip(language_features,word_features)

        else:
            print ("Length of lists not equal, exiting...")
            sys.exit()

        all_features = []

        for z in zipped:
            z = list(z)
            z = ' '.join(z)
            all_features.append(z)

        print ("Length of combined feature list is "+str(len(all_features)))


        f = open(path_to_store_combined_feature_all_file,'w')

        for af in all_features:
            f.write(af+'\n')

        f.close()


    def join_features_and_target(self):

        lines = open(path_to_labelled_raw_file,'r').readlines()

        label = []

        for line in lines:
            spline = line.replace('\n','').split(',')
            label.append(spline[1])

        print ("Length of label list is "+str(len(label)))

        ##############
        # select one of the features to compare
        ##############

        lines2 = open(path_to_store_psychometric_feature_file,'r').readlines()
        #lines2 = open(path_to_store_grammar_feature_file,'r').readlines()
        #lines2 = open(path_to_store_anew_feature_file,'r').readlines()
        #lines2 = open(path_to_store_combined_feature_file,'r').readlines()
        #lines2 = open(path_to_store_combined_feature_all_file,'r').readlines()

        features = []

        for line in lines2:
            spline = line.replace('\n','')
            features.append(spline)

        print ("Length of feature list is "+str(len(features)))


        if len(label) == len(features):
            zipped_list = zip(features,label)

        else:
            print ("Lists have different lengths, exiting...")
            sys.exit()

        # zip both list together

        feature_and_label = []

        for zl in zipped_list:
            zl = list(zl)
            feature_and_label.append(zl)

        print ("Length of combined list is "+str(len(feature_and_label)))

        ###############
        # select one of the path to store result
        ###############

        f = open(path_to_store_labelled_psychometric_file,'w')
        #f = open(path_to_store_labelled_grammar_file,'w')
        #f = open(path_to_store_labelled_anew_file,'w')
        #f = open(path_to_store_labelled_combined_features_file,'w')
        #f = open(path_to_store_labelled_combined_features_all_file,'w')

        # add header
        header = ['posts','label']

        feature_and_label.insert(0,header)

        for fl in feature_and_label:
            f.write(','.join(fl)+'\n')

        f.close()




###############
# variables
###############

path_to_liwc_result_file = '../output/liwc/with_comments/liwc_fb_nonprofit_withcomment.txt'
path_to_labelled_raw_file = '../output/engrate/others/with_comments/labelled_nonprofit_withcomment_raw.csv'
path_to_labelled_preprocessed_file = '../output/engrate/others/with_comments/labelled_nonprofit_withcomment.csv'

path_to_store_psychometric_feature_file = '../output/features/nonprofit/with_comments/psychometrics.txt'
path_to_store_grammar_feature_file = '../output/features/nonprofit/with_comments/grammar.txt'
path_to_store_combined_feature_file = '../output/features/nonprofit/with_comments/combined.txt'
path_to_store_combined_feature_all_file = '../output/features/nonprofit/with_comments/combined_all.txt' #includes word features

path_to_store_labelled_psychometric_file = '../output/features/nonprofit/with_comments/labelled_psychometrics.csv'
path_to_store_labelled_grammar_file = '../output/features/nonprofit/with_comments/labelled_grammar.csv'
path_to_store_labelled_urlhashtagtype_file = '../output/features/nonprofit/with_comments/labelled_urlhashtagtype.csv'
path_to_store_labelled_combined_features_file = '../output/features/nonprofit/with_comments/labelled_combined.csv'
path_to_store_labelled_combined_features_all_file = '../output/features/nonprofit/with_comments/labelled_combined_all.csv'

# anew

path_to_anew_result_file = '../output/anew/anew_nonprofit.csv'
path_to_store_anew_feature_file = '../output/features/nonprofit/anew.txt'
path_to_store_labelled_anew_file = '../output/features/nonprofit/labelled_anew.csv'


# boundary values

analytic_top = 98.0
analytic_bottom = 74.0
clout_top = 97.0
clout_bottom = 66.0
authentic_top = 43.0
authentic_bottom = 2.8
tone_top = 99.0
tone_bottom = 25.0
sixltr_top = 26.0
sixltr_bottom = 14.0
wps_top = 16.0
wps_bottom = 8.0

#valence_top = 55.0
#valence_bottom = 8.0
#arousal_top = 48.0
#arousal_bottom = 8.0
#dominance_top = 50.0
#dominance_bottom = 8.0



if __name__ == '__main__':

    fc = FeatureConstruction()

    fc.liwc_psychometric_features()
    #fc.liwc_grammar_features()
    #fc.url_hashtag_type_feature()
    #fc.anew_features()
    #fc.combine_features()
    #fc.combine_features_all()

    fc.join_features_and_target()

