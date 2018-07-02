#!/usr/bin/python

from __future__ import division
from ROOT import TGraph, TLine, TLegend, TObject
from array import array
import sys
import numpy as np
import math


def getInput(inp):
    if sys.version_info[0] < 3:
        return raw_input(inp)
    else:
        return input(inp)

def getSlope(x,y):
    n = len(x)
    total = 0
    totalx = 0
    totaly = 0
    totalpowx = 0

    for i in range(0,n):
	total += x[i]*y[i]
	totalx += x[i]
	totaly += y[i]
	totalpowx += math.pow(x[i],2)

    a = total * n
    b = totalx * totaly
    c = n * totalpowx
    d = math.pow(totalx,2)

    return (a-b)/(c-d)

def getYInt(slope,x,y):
    n = len(x)
    totalx = 0
    totaly = 0

    for i in range(0,n):
	totalx += x[i]
	totaly += y[i]

    e = totaly
    f = slope * totalx

    return (e-f)/n

x,y1,y2 = array('d'), array('d'), array('d')

x.extend((5,10,15,20,25))
y1.extend((18.92,28.88,37.54,46.67,55.28))
y2.extend(())
n = len(x)

graph1 = TGraph(n,x,y1)
graph1.SetLineColor(4)
graph1.SetTitle("Experiment 1")
graph1.GetYaxis().SetTitle("Timeframes Lost")
graph1.GetXaxis().SetTitle("Ticktime")
graph1.GetHistogram().SetMaximum(y1[n-1]+0.5)
graph1.GetHistogram().SetMinimum(y2[0]-0.5)
graph1.Draw("AC*")
graph2 = TGraph(n,x,y2)
graph2.SetLineColor(2)
graph2.SetMarkerStyle(20)
graph2.Draw("CP")

slope1 = getSlope(x,y1)
intercept1 = getYInt(slope1,x,y1)
point1 = slope1*x[0] + intercept1
point2 = slope1*x[n-1] + intercept1
line1 = TLine(x[0],point1,x[n-1],point2)
line1.SetLineColor(4)
line1.Draw()
print "Slope 1 = ",slope1
print "Intercept 1 = ",intercept1,"\n"

slope2 = getSlope(x,y2)
intercept2 = getYInt(slope2,x,y2)
point1 = slope2*x[0] + intercept2
point2 = slope2*x[n-1] + intercept2
line2 = TLine(x[0],point1,x[n-1],point2)
line2.SetLineColor(2)
line2.Draw()
print "Slope 2 = ",slope2
print "Intercept 2 = ",intercept2

legend = TLegend(0.1,0.7,0.48,0.9)
legend.AddEntry(graph1,"Raspberry Pi results","lep")
legend.AddEntry(graph2,"Nikhef results","lep") 
legend.Draw()

x = 0
while((slope1*x+intercept1)-(slope2*x+intercept2)<= 1):
    x += 1
print x 
while((slope1*x+intercept1)-(slope2*x+intercept2)<= 2):
    x += 1
print x
while((slope1*x+intercept1)-(slope2*x+intercept2)<= 3):
    x += 1
print x

getInput("press any key")
