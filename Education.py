from __future__ import annotations
from decimal import Decimal
from typing import Self
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

languages = ['Java', 'Python', 'JavaScript']
versions = [-0.98,14, 3, 6,10]
ahaha=(1,2,3,4,5)

result=zip(languages,versions,ahaha)
list_res=list(result)
z,x,c=zip(*list_res)
print(z,x,list(c))

mathematict=__import__('math',globals(),locals(),[],0)
print(mathematict.fabs(-0.09),math.fabs(10-15.97))

x=-9
mathematict.fabs(x)
math.fabs(x)