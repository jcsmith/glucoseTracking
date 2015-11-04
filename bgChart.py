#!/usr/bin/env python

"""
Calculate some statistics about my blood glucose readings and chart them.

"""

import numpy as np
import matplotlib.pyplot as plt
import sqlite3

#connect to the database
dbconn = sqlite3.connect('/home/jsmith/bloodGlucose/glucose.db')
dbcur = dbconn.cursor()

dbcur.execute('SELECT glucose from glucose')

blood_glucose=[]
for reading in dbcur:
    blood_glucose.append(reading[0])

#plt.axvspan(80,120,color='green',alpha=0.5)
plt.hist(blood_glucose, normed=True)
plt.title("Blood Glucose")
plt.xlabel("mg/dL")
plt.ylabel("Frequency")
plt.show()

#disconnect from the database
dbconn.close()
