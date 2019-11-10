#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 00:06:00 2019

@author: theophanegregoir
"""

import pandas as pd
import sklearn as sk
import datetime as dt
import sys
import math
from time import time
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.ensemble import AdaBoostClassifier


### Creation of train and test datasets
xls_file = pd.ExcelFile('/Users/theophanegregoir/Desktop/SportsCoding/Entire_Data_PL.xlsx')
temp = dt.datetime(1899, 12, 30)    # Note, not 31st Dec but 30th!

### Feature and Label selection
features_selection = ['Date','HomeTeam','AwayTeam','IWH','IWD','IWA','WHH','WHD','WHA']
labels_selection = ['FTR']
total_selection = features_selection + labels_selection 

###FULL
full = xls_file.parse('2000-2001')[total_selection].dropna(axis=0)
for i in range(2001,2019):
    txt = str(i) + '-' + str(i + 1)
    add_part = xls_file.parse(txt)[total_selection].dropna(axis=0)
    full = pd.concat([full, add_part])
full['Date'] = ((pd.to_datetime(full['Date']) - temp)/dt.timedelta(days=1)) - 36757
A = full[features_selection]
B = full[labels_selection]
A = pd.get_dummies(A, prefix_sep='_', drop_first = True)

features_train, features_test, labels_train, labels_test = train_test_split(A, B, test_size=0.40, random_state=40)

### MACHINE LEARNING
t0 = time()
parameters = {'n_estimators':[i for i in range(1,51,5)], 'learning_rate':[(1.0/j) for j in range(1,10)]}
ada = AdaBoostClassifier()
clf = GridSearchCV(ada, parameters, cv=5)
clf.fit(features_train,labels_train)
t1 = time()
print("Training time : " + str(t1 - t0) + " seconds")

pred = clf.predict(features_test)
pred = pd.DataFrame(pred)
print(accuracy_score(labels_test, pred))
matrix = confusion_matrix(labels_test, pred)
print(matrix)

### TRAIN DATASET
#train = xls_file.parse('2000-2001')[total_selection].dropna(axis=0)
#features_train = train[features_selection]
#labels_train = train[labels_selection]
#
#for i in range(2001,2011):
#    txt = str(i) + '-' + str(i + 1)
#    add_train = xls_file.parse(txt)[total_selection].dropna(axis=0)
#    add_features_train = add_train[features_selection]
#    add_labels_train = add_train[labels_selection]
#    features_train = pd.concat([features_train, add_features_train])
#    labels_train = pd.concat([labels_train, add_labels_train])
#
#features_train['Date'] = ((pd.to_datetime(features_train['Date']) - temp)/dt.timedelta(days=1)) - 36757
#
#
#### TEST DATASET
#test = xls_file.parse('2011-2012')[total_selection].dropna(axis=0)
#features_test = test[features_selection]
#labels_test = test[labels_selection]
#
#for i in range(2011,2019):
#    txt = str(i) + '-' + str(i + 1)
#    add_test = xls_file.parse(txt)[total_selection].dropna(axis=0)
#    add_features_test = add_test[features_selection]
#    add_labels_test = add_test[labels_selection]
#    features_test = pd.concat([features_test, add_features_test])
#    labels_test = pd.concat([labels_test, add_labels_test])   
#
#features_test['Date'] = ((pd.to_datetime(features_test['Date']) - temp)/dt.timedelta(days=1)) - 36757


### ENCODING CATEGORICAL FEATURE
# Get dummies
#n_train = len(features_train)
#n_test = len(features_test)
#X = pd.concat([features_train, features_test])   
#X = pd.get_dummies(X, prefix_sep='_', drop_first = True)
#features_train = X.iloc[0:n_train]
#features_test = X.iloc[n_train:]


