__author__ = 'yi-linghwong'

import sys
import os
import operator
import pandas as pd
from sklearn import cross_validation
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
#from sklearn.naive_bayes import BernoulliNB
from sklearn.pipeline import Pipeline
from sklearn.grid_search import GridSearchCV
from sklearn.cross_validation import train_test_split
from sklearn.cross_validation import StratifiedShuffleSplit
from sklearn.cross_validation import StratifiedKFold
from sklearn.cross_validation import cross_val_score
#from sklearn.feature_selection import RFE
from sklearn.feature_selection import RFECV
#from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import SelectPercentile
from sklearn.feature_selection import chi2, f_classif
from sklearn import metrics
import numpy as np
import scipy as sp
from sklearn.feature_extraction import text
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from dense_transformer import DenseTransformer


dataset = pd.read_csv('../output/features/labelled_urlhashtagtype.csv', header=0, names=['posts', 'class'])

X = dataset['posts']
y = dataset['class']


docs_train, docs_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

print ("Number of data point is "+str(len(y)))

lines = open('../../TwitterML/stopwords/stopwords.csv', 'r').readlines()

my_stopwords=[]
for line in lines:
    my_stopwords.append(line.replace("\n", ""))

stopwords = text.ENGLISH_STOP_WORDS.union(my_stopwords)


# Get list of features
count_vect = CountVectorizer(stop_words=stopwords, min_df=3, max_df=0.90, ngram_range=(1,1))
X_CV = count_vect.fit_transform(docs_train)

# print number of unique words (n_features)
print ("Shape of train data is "+str(X_CV.shape))

# tfidf transformation###

tfidf_transformer = TfidfTransformer(use_idf = True)
X_tfidf = tfidf_transformer.fit_transform(X_CV)

X_dense = X_tfidf.toarray()

feature_names = count_vect.get_feature_names()
print (feature_names)

pca = PCA(n_components=4)
X_new = pca.fit_transform(X_dense)

print (X_new.shape) #shape = (n_samples, n_components)

components = pca.components_

print (pca.explained_variance_ratio_)
print (components)


pca = PCA()

n_features = X_CV.shape[1]
n_components = []

print (n_features)

for n in range(1,11):

    components = int(n_features * (n/10))
    n_components.append(components)

clf = MultinomialNB()

#pca = PCA()
#pipe = Pipeline(steps=[('pca', pca), ('clf', clf)])

###############################################################################
# Plot the PCA spectrum
pca.fit(X_dense)
print ("#############")
print (pca.explained_variance_ratio_)

#plt.figure(1, figsize=(4, 3))
plt.clf()
plt.axes([.2, .2, .7, .7])
plt.plot(pca.explained_variance_, linewidth=2)
plt.axis('tight')
plt.xlabel('n_components')
plt.ylabel('explained_variance_')

'''

n_components = [3,5,7]
alpha = [0.4, 0.5]

#Parameters of pipelines can be set using ‘__’ separated parameter names:

pipeline = Pipeline([
     ('vect', TfidfVectorizer(stop_words=stopwords, min_df=3, max_df=0.90)),
     ('to_dense', DenseTransformer()),
#     ('pca', PCA())
     ('clf', MultinomialNB())
])


parameters = {
    'vect__ngram_range': [(1,1),(1,2), (1,3)],
    'vect__use_idf': (True, False),
    'clf__alpha': (0.4, 0.5)
}


cv = StratifiedShuffleSplit(y_train, n_iter=5, test_size=0.2, random_state=42)
grid_search = GridSearchCV(pipeline, param_grid=parameters, cv=cv, n_jobs=-1)
clf_gs = grid_search.fit(docs_train, y_train)


plt.axvline(clf_gs.best_estimator_.named_steps['pca'].n_components,
            linestyle=':', label='n_components chosen')
plt.legend(prop=dict(size=12))
plt.show()



pca_scores, fa_scores = [], []
for n in n_components:
    pca.n_components = n
    pca_scores.append(np.mean(cross_val_score(pca, X_dense)))

print (pca_scores)

'''