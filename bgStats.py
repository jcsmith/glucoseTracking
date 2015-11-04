#!/usr/bin/env python

import sqlite3
import matplotlib
matplotlib.use('Svg')
import matplotlib.pyplot as plt
import pandas.io.sql as sql
import pandas as pd
import numpy as np
import argparse

#Setup argparse to handle the command line parameters
parser = argparse.ArgumentParser(description='Analyze blood glucose data')

parser.add_argument("database", help='Enter the path to the sqlite3 database containing the readings')

args = parser.parse_args()

def getReadingsFromDB(database):
    #connect to the databse
    dbconn = sqlite3.connect(database)
    #get all of the data into a pandas object
    bloodGlucoseReadings = sql.read_sql('SELECT * from glucoseReadings ORDER BY ReadingTimeStamp', dbconn, index_col="ReadingTimeStamp", parse_dates=["ReadingTimeStamp"])
    #close the database connection
    dbconn.close()

    #sort dataframe by the time stamps
    #bloodGlucoseReadings.sort_index(by='ReadingTimeStamp')

    return(bloodGlucoseReadings)

#def geteHbA1c( averageReading ):
#    return((averageReading + 46.7)/28.7)

bloodGlucoseReadings = getReadingsFromDB(args.database)
DailyAverageGlucoseReadings = bloodGlucoseReadings['Reading'].resample('D',how='mean',fill_method='ffill')

print bloodGlucoseReadings 
print DailyAverageGlucoseReadings

#DailyAverageGlucosePlot = DailyAverageGlucoseReadings.plot(use_index=True,title="Joshua C. Smith - Daily Blood Glucose Average")
#fig=DailyAverageGlucosePlot.get_figure()
#fig.savefig('DailyAverageGlucose')

#bloodGlucoseReadings.hist(column='Reading', ax=ax)
#ax.title("Blood Glucose Readings")
#fig.savefig('bghist')
fig = plt.figure(1)
plt.subplot(111)
plt.hist(bloodGlucoseReadings['Reading'], normed=True)
fig.savefig('foo')

