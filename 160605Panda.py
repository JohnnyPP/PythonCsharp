# -*- coding: utf-8 -*-
"""
Created on Fri Jun 03 13:49:34 2016

@author: klocek
"""
import numpy
import pandas as pd
import glob
import sys, os
          
path = os.path.dirname(sys.argv[0])    # gets the path automatically    

def medianNumPy(lst):
    return numpy.median(numpy.array(lst))

glob.glob('/Misch-d_*.csv')
allFiles = glob.glob(path + "/Misch-d_*.csv")
frame = pd.DataFrame()
list_ = []
for file_ in allFiles:
    df = pd.read_csv(file_,index_col=None, header=0)
    list_.append(df)
MischD = pd.concat(list_)


Thk=MischD.ix[:,'T1_Thk(um)':'T4_Thk(um)']
Thk['median'] = Thk.median(axis=1)

Twid=MischD.ix[:,'T1_TW(um)':'T4_TW(um)']
Twid['median'] = Twid.median(axis=1)

middleW=MischD.ix[:,'T1_MW(um)':'T4_MW(um)']
middleW['median'] = middleW.median(axis=1)

bottomW=MischD.ix[:,'T1_BW(um)':'T4_BW(um)']
bottomW['median'] = bottomW.median(axis=1)

median = Twid['median']

medianLenght = len(median)

medianSliced = []
medianSlicedLow = []    # this stores first 4 values (approx 40)
medianSlicedHigh = []   # this stores next 4 values (approx 60)
median4High = []
median4Low = []

for i in xrange(0,medianLenght,4):
    medianSliced.append(median[i:4+i])

for i in range(0,len(medianSliced)):
    if i % 2 == 0:
        medianSlicedLow.append(medianSliced[i])
        median4Low.append(medianNumPy(medianSliced[i]))
    else:
        medianSlicedHigh.append(medianSliced[i])
        median4High.append(medianNumPy(medianSliced[i]))

print median4High