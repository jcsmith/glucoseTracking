#!/usr/bin/env python

"""
Create a new empty Blood Glucose Reading Database
"""

import sqlite3
import sys
import argparse

#Set up argparse to handle the command line arguments
parser = argparse.ArgumentParser(description='Create a blood glucose reading database.')
parser.add_argument("database", help="Enter the path to the database you would like to create")
#Parse command line arguments
args = parser.parse_args()

newDB = sqlite3.connect(args.database, detect_types=sqlite3.PARSE_DECLTYPES)

cur = newDB.cursor()

cur.execute('create table GlucoseReadings (ReadingTimeStamp timestamp, Reading integer, Fasting boolean)')

newDB.close()
