from __future__ import annotations
from decimal import Decimal
from typing import Self
from dataclasses import dataclass
from pathlib import Path
import math
import random
import os
import shutil
import builtins
import cmath
import re
import keyword
import asyncio
from datetime import datetime, date
import pytz
import time
import threading
import numpy 
import requests
import matplotlib.pyplot as plt


sequence=numpy.random.normal(10.0,1.0,500)

a=numpy.array([-1,-2,-3,1,-0,100])
print(numpy.abs(a))

b=numpy.array([True,False,False,True])
c=numpy.array([False,False,False,True])

print(numpy.logical_and(c,b),c*b)


a = numpy.array([[815, 70, 115],
                [767, 80, 50],
                [912, 74, 77],
                [400, 88, 70],
                [1008, 65, 128]])

mean,stdev=numpy.mean(a,axis=0),numpy.std(a,axis=0)



print(mean,stdev,sep='\n')

outliers=((numpy.abs(a[:,0]-mean[0])>stdev[0])
         *(numpy.abs(a[:,1]-mean[1])>stdev[1])
         *(numpy.abs(a[:,2]-mean[2])>stdev[2]))

print((numpy.abs(a[:,0]-mean[0])>stdev[0])
         *(numpy.abs(a[:,1]-mean[1])>stdev[1])
         *(numpy.abs(a[:,2]-mean[2])>stdev[2]))

print(a[outliers])

basket = numpy.array([[0, 1, 1, 0],
                    [0, 1, 0, 1],
                    [1, 1, 1, 0],
                    [0, 1, 1, 1],
                    [1, 1, 1, 0],
                    [0, 1, 1, 0],
                    [1, 1, 0, 1],
                    [1, 1, 1, 1]])

copurchases=numpy.sum(numpy.all(basket[:,2:],axis=1))/basket.shape[0]

print(numpy.all(basket[:,2:],axis=1))

print(copurchases)

copurchases=[(i,j,numpy.sum(basket[:,i]+basket[:,j]==2))
            for i in range(4) for j in range (i+1,4)]

print(copurchases)

print(max(copurchases,key=lambda x:x[2]))