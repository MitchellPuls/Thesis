#!/usr/bin/python

import csv
import sys
import math

def calculate(n,o):
    print "O ", o
    print "N ", n
    print "Nominal = ",  o-n
    print "Percent = ", round(((n-o)/o)*100,2)
    return;

f = open(sys.argv[1], "rb")
n = open(sys.argv[2], "rb")

reader1 = csv.reader(f)
reader2 = csv.reader(n)
totalo = 0
totaln = 0
count = 0

for row in reader1:
    count += 1
    row2 = map(float,next(reader2))[0]
    calculate(row2,map(float,row)[0])
    totalo += map(float,row)[0]
    totaln += row2

print "Avg nom = ", round((totalo-totaln)/count,2)
print "Avg % = ", round(((totaln-totalo)/totalo)*100,2)
