#!/usr/bin/env python

"""
Add blood glucose reading to the specified database.
"""

import sys
import sqlite3
import datetime
import argparse
from dateutil.parser import parse

typeChoices = [ 'BB', 'AB', 'BL', 'AL', 'BD', 'AD', 'BT', 'NA' ]

#Set up argparse to handle the command line arguments
parser = argparse.ArgumentParser(description='Add a reading to a blood gulcuose monitoring database.')
parser.add_argument("reading", help="Enter the blood glucose reading.", type=int)
parser.add_argument("-d","--date", help="Enter the date of the reading")
parser.add_argument("--db", help="Enter the location of the database")
parser.add_argument("--type","-t", help="Enter the type of reading", choices=typeChoices, default='NA')
#Parse command line arguments
args = parser.parse_args()

#If the --db argument is supplied connect to that db other wise connect to the default db ~/.bloodglucose/readings.db
if args.db:
    dbconn = sqlite3.connect(args.db)
    cur = dbconn.cursor()
    cur.execute('INSERT INTO GlucoseReadings VALUES(?, ?, ?)', (parse(args.date), args.reading, args.type))
    dbconn.commit()
    cur.execute('SELECT * FROM GlucoseReadings')
    dbconn.close()
else:
    print "Please specify a DB"
