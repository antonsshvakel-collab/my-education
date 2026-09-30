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
import matplotlib.pyplot as plt



words='Hello World!!!'

srez=slice(0,None,2)

print(words[srez])

letters_amazon = '''
We spent several years building our own database engine,
Amazon Aurora, a fully-managed MySQL and PostgreSQL-compatible
service with the same or better durability and availability as
the commercial engines, but at one-tenth of the cost. We were
not surprised when this worked.
'''

find= lambda x,q: x[max(0,x.find(q)-18):x.find(q)+len(q)+18] if q in x else -1

print(find(letters_amazon,'Amazon Aurora'),type(find))

price = [[9.9, 9.8, 9.8, 9.4, 9.5, 9.7],
        [9.5, 9.4, 9.4, 9.3, 9.2, 9.1],
        [8.4, 7.9, 7.9, 8.1, 8.0, 8.0],
        [7.1, 5.9, 4.8, 4.8, 4.7, 3.9]]

sample=[line[::2] for line in price]
print(sample)
for line in price:
    line[::2]=[10] *3
print(price)

visitors = ['Firefox', 'corrupted', 'Chrome', 'corrupted',
            'Safari', 'corrupted', 'Safari', 'corrupted',
            'Chrome', 'corrupted', 'Firefox', 'corrupted']

visitors[1::2]=visitors[::2]
print(visitors)

nums=numpy.array([1,0,3,0,4,0,6,0,8,0,10,0])
nums[1::2]=[x+1 for x in nums[::2]]
nums[1::2]=nums[::2]+1
print(nums)

cardiac_cycle = [62, 60, 62, 64, 68, 77, 80, 76, 71, 66, 61, 60, 62]

print(cardiac_cycle[2:-2])

expected_cycyles=cardiac_cycle[1:-2]*10
#plt.plot(expected_cycyles)
#plt.show()


companies = {
    'CoolCompany' : {'Alice' : 33, 'Bob' : 28, 'Frank' : 29},
    'CheapCompany' : {'Ann' : 4, 'Lee' : 9, 'Chrisi' : 7},
    'SosoCompany' : {'Esther' : 38, 'Cole' : 8, 'Paris' : 18}}

illegal = [x for x in companies if any(y<9 for y in companies[x].values())]
print(illegal)

list1=[1,0]
tuple1=(1,0)
set1={1,0}

print(any((list1)),all((list1)))

list1=['Anton','Artem','Maksim']
list2=[366,278,233]
zipped=list(zip(list1,list2))
print(zipped)

list1,list2=zip(*zipped)
print(list(list1),list(list2))

list3=['name','grade','game']
list4=[('Anton',366,'Dota2'),
        ('Artem',278,'War thunder'),
        ('Maksim',233,'Roblox')]
print(dict(zip(list3,list4)))

data_base=[dict(zip(list3,row)) for row in list4]
print(data_base)

flt=10
str1=str(flt)
print(str1,type(str1),0.1+0.2==0.3)