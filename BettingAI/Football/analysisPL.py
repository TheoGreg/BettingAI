#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 00:06:00 2019

@author: theophanegregoir

Notes for Football Data

All data is in csv format, ready for use within standard spreadsheet applications. Please note that some abbreviations are no longer in use (in particular odds from specific bookmakers no longer used) and refer to data collected in earlier seasons. For a current list of what bookmakers are included in the dataset please visit http://www.football-data.co.uk/matches.php

Key to results data:

Div = League Division
Date = Match Date (dd/mm/yy)
Time = Time of match kick off
HomeTeam = Home Team
AwayTeam = Away Team
FTHG and HG = Full Time Home Team Goals
FTAG and AG = Full Time Away Team Goals
FTR and Res = Full Time Result (H=Home Win, D=Draw, A=Away Win)
HTHG = Half Time Home Team Goals
HTAG = Half Time Away Team Goals
HTR = Half Time Result (H=Home Win, D=Draw, A=Away Win)

Match Statistics (where available)
Attendance = Crowd Attendance
Referee = Match Referee
HS = Home Team Shots
AS = Away Team Shots
HST = Home Team Shots on Target
AST = Away Team Shots on Target
HHW = Home Team Hit Woodwork
AHW = Away Team Hit Woodwork
HC = Home Team Corners
AC = Away Team Corners
HF = Home Team Fouls Committed
AF = Away Team Fouls Committed
HFKC = Home Team Free Kicks Conceded
AFKC = Away Team Free Kicks Conceded
HO = Home Team Offsides
AO = Away Team Offsides
HY = Home Team Yellow Cards
AY = Away Team Yellow Cards
HR = Home Team Red Cards
AR = Away Team Red Cards
HBP = Home Team Bookings Points (10 = yellow, 25 = red)
ABP = Away Team Bookings Points (10 = yellow, 25 = red)

Note that Free Kicks Conceeded includes fouls, offsides and any other offense commmitted and will always be equal to or higher than the number of fouls. Fouls make up the vast majority of Free Kicks Conceded. Free Kicks Conceded are shown when specific data on Fouls are not available (France 2nd, Belgium 1st and Greece 1st divisions).

Note also that English and Scottish yellow cards do not include the initial yellow card when a second is shown to a player converting it into a red, but this is included as a yellow (plus red) for European games.


Key to 1X2 (match) betting odds data:

B365H = Bet365 home win odds
B365D = Bet365 draw odds
B365A = Bet365 away win odds
BSH = Blue Square home win odds
BSD = Blue Square draw odds
BSA = Blue Square away win odds
BWH = Bet&Win home win odds
BWD = Bet&Win draw odds
BWA = Bet&Win away win odds
GBH = Gamebookers home win odds
GBD = Gamebookers draw odds
GBA = Gamebookers away win odds
IWH = Interwetten home win odds
IWD = Interwetten draw odds
IWA = Interwetten away win odds
LBH = Ladbrokes home win odds
LBD = Ladbrokes draw odds
LBA = Ladbrokes away win odds
PSH and PH = Pinnacle home win odds
PSD and PD = Pinnacle draw odds
PSA and PA = Pinnacle away win odds
SOH = Sporting Odds home win odds
SOD = Sporting Odds draw odds
SOA = Sporting Odds away win odds
SBH = Sportingbet home win odds
SBD = Sportingbet draw odds
SBA = Sportingbet away win odds
SJH = Stan James home win odds
SJD = Stan James draw odds
SJA = Stan James away win odds
SYH = Stanleybet home win odds
SYD = Stanleybet draw odds
SYA = Stanleybet away win odds
VCH = VC Bet home win odds
VCD = VC Bet draw odds
VCA = VC Bet away win odds
WHH = William Hill home win odds
WHD = William Hill draw odds
WHA = William Hill away win odds

Bb1X2 = Number of BetBrain bookmakers used to calculate match odds averages and maximums
BbMxH = Betbrain maximum home win odds
BbAvH = Betbrain average home win odds
BbMxD = Betbrain maximum draw odds
BbAvD = Betbrain average draw win odds
BbMxA = Betbrain maximum away win odds
BbAvA = Betbrain average away win odds

MaxH = Market maximum home win odds
MaxD = Market maximum draw win odds
MaxA = Market maximum away win odds
AvgH = Market average home win odds
AvgD = Market average draw win odds
AvgA = Market average away win odds


Key to total goals betting odds:

BbOU = Number of BetBrain bookmakers used to calculate over/under 2.5 goals (total goals) averages and maximums
BbMx>2.5 = Betbrain maximum over 2.5 goals
BbAv>2.5 = Betbrain average over 2.5 goals
BbMx<2.5 = Betbrain maximum under 2.5 goals
BbAv<2.5 = Betbrain average under 2.5 goals

GB>2.5 = Gamebookers over 2.5 goals
GB<2.5 = Gamebookers under 2.5 goals
B365>2.5 = Bet365 over 2.5 goals
B365<2.5 = Bet365 under 2.5 goals
P>2.5 = Pinnacle over 2.5 goals
P<2.5 = Pinnacle under 2.5 goals
Max>2.5 = Market maximum over 2.5 goals
Max<2.5 = Market maximum under 2.5 goals
Avg>2.5 = Market average over 2.5 goals
Avg<2.5 = Market average under 2.5 goals


Key to Asian handicap betting odds:

BbAH = Number of BetBrain bookmakers used to Asian handicap averages and maximums
BbAHh = Betbrain size of handicap (home team)
AHh = Market size of handicap (home team) (since 2019/2020)
BbMxAHH = Betbrain maximum Asian handicap home team odds
BbAvAHH = Betbrain average Asian handicap home team odds
BbMxAHA = Betbrain maximum Asian handicap away team odds
BbAvAHA = Betbrain average Asian handicap away team odds

GBAHH = Gamebookers Asian handicap home team odds
GBAHA = Gamebookers Asian handicap away team odds
GBAH = Gamebookers size of handicap (home team)
LBAHH = Ladbrokes Asian handicap home team odds
LBAHA = Ladbrokes Asian handicap away team odds
LBAH = Ladbrokes size of handicap (home team)
B365AHH = Bet365 Asian handicap home team odds
B365AHA = Bet365 Asian handicap away team odds
B365AH = Bet365 size of handicap (home team)
PAHH = Pinnacle Asian handicap home team odds
PAHA = Pinnacle Asian handicap away team odds
MaxAHH = Market maximum Asian handicap home team odds
MaxAHA = Market maximum Asian handicap away team odds	
AvgAHH = Market average Asian handicap home team odds
AvgAHA = Market average Asian handicap away team odds

Closing odds (last odds before match starts)

As above but with an additional "C" character following the bookmaker abbreviation/Max/Avg

Football-Data would like to acknowledge the following sources which have been utilised in the compilation of Football-Data's results and odds files.

Current results (full time, half time)
Xcores - http://www.xcores .com

Match statistics
BBC, ESPN Soccer, Bundesliga.de, Gazzetta.it and Football.fr

Bookmakers betting odds
Individual bookmakers

Betting odds for weekend games are collected Friday afternoons, and on Tuesday afternoons for midweek games.

Additional match statistics (corners, shots, bookings, referee etc.) for the 2000/01 and 2001/02 seasons for the English, Scottish and German leagues were provided by Sports.com (now under new ownership and no longer available).







"""
import sear
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
xls_file = pd.ExcelFile('/Users/theophanegregoir/Desktop/SportsCoding/Football/Entire_Data_PL.xlsx')
temp = dt.datetime(1899, 12, 30)    # Note, not 31st Dec but 30th!


###Creation of league tables journey after journey
League_table_features = ['Date','HomeTeam','AwayTeam','FTR','FTHG','FTAG','HTHG','HTAG']
league_tables = {}
for i in range(2000,2019):
    name = str(i) + '-' + str(i + 1)
    league_tables[name] = {}
    table = xls_file.parse(name)[League_table_features].dropna(axis=0)
    clubs = list(set(list(table['HomeTeam'])))
    
    ###Initialisation each table 
    for k in range(1,(len(clubs)-1)*2+1):
        league_tables[name][k] = {}
        
    for c in clubs:
        isHome = table['HomeTeam'] == c
        isAway = table['AwayTeam'] == c
        selected = table.loc[isHome | isAway]     
        print(c)
        for k in range(1,(len(clubs)-1)*2+1):
            if selected['FTR'][selected.index[k-1]] == "D":
                league_tables[name][k][c] = 1
            elif selected['FTR'][selected.index[k-1]] == "A" and selected['AwayTeam'][selected.index[k-1]] == c:
                league_tables[name][k][c] = 3
            elif selected['FTR'][selected.index[k-1]] == "H" and selected['HomeTeam'][selected.index[k-1]] == c:
                league_tables[name][k][c] = 3
            else:
                league_tables[name][k][c] = 0






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

###Creation of each 
###Halftime goal difference
###Fulltime goal difference


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


