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
from sklearn.neural_network import MLPClassifier

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


###Anonymiser for Winners and Losers
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
A['RankA'] = pd.to_numeric(A['RankA'])
A['RankB'] = pd.to_numeric(A['RankB'])
A = pd.get_dummies(A, prefix_sep='_', drop_first = True)

features_train, features_test, labels_train, labels_test = train_test_split(A, B, test_size=0.30, random_state=50)

### MACHINE LEARNING
print('Training starting...')


### ADABOOST CLASSIFIER
#t0 = time()
#parameters = {'n_estimators':[10,20,30], 'learning_rate':[0.2,0.4,0.8]}
#ada = AdaBoostClassifier()
#clf = GridSearchCV(ada, parameters, cv=5)
#clf.fit(features_train,labels_train)
#t1 = time()
#print("Training time Adaboost : " + str(t1 - t0) + " seconds")
#pred = clf.predict(features_test)
#pred = pd.DataFrame(pred)
#print(accuracy_score(labels_test, pred))
#matrix = confusion_matrix(labels_test, pred)
#print(matrix)

### RANDOM FOREST CLASSIFIER
t2 = time()
clf2 = RandomForestClassifier(n_estimators = 30,min_samples_split = 3, max_depth = 25)
clf2.fit(features_train,labels_train)
pred2 = clf2.predict(features_test)
print(accuracy_score(labels_test, pred2))
t3 = time()
print("Training time Random Forest : " + str(t3 - t2) + " seconds")
matrix2 = confusion_matrix(labels_test, pred2)
print(matrix2)

### NEURAL NETWORK
#t4 = time()
#neural = MLPClassifier(activation='relu', tol=1e-8, alpha=1e-05, hidden_layer_sizes=(100,100,100),learning_rate='constant', max_iter = 5000)
#neural.fit(features_train,labels_train)
#predNeural = neural.predict(features_test)
#print(accuracy_score(labels_test, predNeural))
#t5 = time()
#print("Training time Neural Network : " + str(t5 - t4) + " seconds")
#matrix2 = confusion_matrix(labels_test, predNeural)
#print(matrix2)


### RESULTS ANALYSIS
final_table = features_test[['B365A','B365B','RankA','RankB']]
final_table['Results'] = labels_test
final_table['Predictions'] = pred2
right = (final_table['Predictions'] == final_table['Results'])
predicted_A = final_table['Predictions'] == 'A'
predicted_B = final_table['Predictions'] == 'B'
final_table['earning'] = -1
final_table.loc[predicted_A & right, 'earning'] = final_table.loc[predicted_A & right,'B365A'] - 1
final_table.loc[predicted_B & right, 'earning'] = final_table.loc[predicted_B & right,'B365B'] - 1
print("Betting 1$ on each game and following the AI, your return would have been : " + str(final_table['earning'].sum()) + " $")

### BASIC STRATEGY
lowerA = final_table['B365A'] < final_table['B365B']
lowerB = final_table['B365B'] < final_table['B365A']
resA = final_table['Results'] == 'A'
resB = final_table['Results'] == 'B'
final_table['basic_strat'] = -1
final_table.loc[resA & lowerA, 'basic_strat'] = final_table.loc[resA & lowerA,'B365A'] - 1
final_table.loc[resB & lowerB, 'basic_strat'] = final_table.loc[resB & lowerB,'B365B'] - 1
print("Betting 1$ on each game on lowest odd, your return would have been : " + str(final_table['basic_strat'].sum()) + " $")


### OUTSIDERS PREDICTED
bool_1 = final_table['Predictions'] == 'A'
bool_2 = final_table['B365A'] > final_table['B365B']
bool_3 = final_table['Predictions'] == 'B'
bool_4 = final_table['B365B'] > final_table['B365A']
Out_pred = final_table[(bool_1 & bool_2)  | (bool_3 & bool_4)]
right_out = (Out_pred['Predictions'] == Out_pred['Results'])
print("When betting on the outsider, the AI was right in " + str(100.0 * (len(Out_pred[right_out]) / float(len(Out_pred)))) + "% of cases")




