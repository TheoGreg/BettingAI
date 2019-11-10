#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 15:15:01 2019

@author: theophanegregoir
"""


import pandas as pd
import sklearn as sk
import datetime as dt
import sys
import os
from time import time
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import RandomForestClassifier


### Creation of train and test datasets
xls_file = pd.ExcelFile('/Users/theophanegregoir/Desktop/SportsCoding/Tennis Data/2002.xls')
temp = dt.datetime(1899, 12, 30)    # Note, not 31st Dec but 30th!

### Feature and Label selection
features_selection = ['Date','Tournament','Round','Best of','Surface','Court','Loser','B365L','B365W','WRank','LRank']
labels_selection = ['Winner']
total_selection = features_selection + labels_selection 

###FULL
full = xls_file.parse('2002')[total_selection].dropna(axis=0)
for i in range(2003,2020):
    print(i)
    txt = str(i)
    if (i <= 2012):
        add_file = pd.ExcelFile('/Users/theophanegregoir/Desktop/SportsCoding/Tennis Data/' + str(i) + '.xls')
        add_part = add_file.parse(txt)[total_selection].dropna(axis=0)
    else:
        add_file = pd.ExcelFile('/Users/theophanegregoir/Desktop/SportsCoding/Tennis Data/' + str(i) + '.xlsx')
        add_part = add_file.parse(txt)[total_selection].dropna(axis=0)
    full = pd.concat([full, add_part])
full['Date'] = ((pd.to_datetime(full['Date']) - temp)/dt.timedelta(days=1)) - 37256


###Anonymiser Winners and Losers
s = pd.Series([k for k in range(46018)])
full.set_index(s)
full['Winner_AB'] = 0
full.loc[full.index % 2 == 0,'Winner_AB'] = 'A'
full.loc[full.index % 2 == 1,'Winner_AB'] = 'B'
full['PlayerA'] = 0
full.loc[full.index % 2 == 0,'PlayerA'] = full.iloc[lambda x: x.index % 2 == 0]['Winner']
full.loc[full.index % 2 == 1,'PlayerA'] = full.iloc[lambda x: x.index % 2 == 1]['Loser']
full['PlayerB'] = 0
full.loc[full.index % 2 == 0,'PlayerB'] = full.iloc[lambda x: x.index % 2 == 0]['Loser']
full.loc[full.index % 2 == 1,'PlayerB'] = full.iloc[lambda x: x.index % 2 == 1]['Winner']
full['B365A'] = 0
full.loc[full.index % 2 == 0,'B365A'] = full.iloc[lambda x: x.index % 2 == 0]['B365W']
full.loc[full.index % 2 == 1,'B365A'] = full.iloc[lambda x: x.index % 2 == 1]['B365L']
full['B365B'] = 0
full.loc[full.index % 2 == 0,'B365B'] = full.iloc[lambda x: x.index % 2 == 0]['B365L']
full.loc[full.index % 2 == 1,'B365B'] = full.iloc[lambda x: x.index % 2 == 1]['B365W']
full['RankA'] = 0
full.loc[full.index % 2 == 0,'RankA'] = full.iloc[lambda x: x.index % 2 == 0]['WRank']
full.loc[full.index % 2 == 1,'RankA'] = full.iloc[lambda x: x.index % 2 == 1]['LRank']
full['RankB'] = 0
full.loc[full.index % 2 == 0,'RankB'] = full.iloc[lambda x: x.index % 2 == 0]['LRank']
full.loc[full.index % 2 == 1,'RankB'] = full.iloc[lambda x: x.index % 2 == 1]['WRank']

new_features_selection = ['Date','Tournament','Round','Best of','Surface','Court','PlayerA','PlayerB','B365A','B365B','RankA','RankB']
new_labels_selection = ['Winner_AB']
A = full[new_features_selection]
B = full[new_labels_selection]
A = pd.get_dummies(A, prefix_sep='_', drop_first = True)

features_train, features_test, labels_train, labels_test = train_test_split(A, B, test_size=0.40, random_state=40)

### MACHINE LEARNING
print('Training starting...')

#t0 = time()
#parameters = {'n_estimators':[i for i in range(1,51,10)], 'learning_rate':[(1.0/j) for j in range(1,6)]}
#ada = AdaBoostClassifier()
#clf = GridSearchCV(ada, parameters, cv=5)
#clf.fit(features_train,labels_train)
#t1 = time()
#print("Training time : " + str(t1 - t0) + " seconds")
#pred = clf.predict(features_test)
#pred = pd.DataFrame(pred)
#print(accuracy_score(labels_test, pred))
#matrix = confusion_matrix(labels_test, pred)
#print(matrix)

clf2 = RandomForestClassifier(n_estimators = 20,min_samples_split = 5, max_depth = 20)
clf2.fit(features_train,labels_train)
pred2 = clf2.predict(features_test)
print(accuracy_score(labels_test, pred2))
matrix2 = confusion_matrix(labels_test, pred2)
print(matrix2)


