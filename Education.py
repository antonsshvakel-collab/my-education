from __future__ import annotations
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



with open('demofile.txt','a+',encoding='utf-8') as f:
    pass

class Alphabet:
    def __init__(self,stroka:str='') -> None:
        self._stroka=stroka

    @property
    def stroka(self)->str:
        return self._stroka

    @stroka.setter
    def stroka(self,value:str)->None:
        self._stroka=value

    @stroka.deleter
    def stroka(self)->None:
        print("Deliting")
        del self._stroka


x=Alphabet()
print(x.stroka)
x.stroka='Abdul Ballout'
print(x.stroka)

delattr(x,'stroka')
print(hasattr(x,'stroka'))

numbers=range(0,101,2)
for item in numbers:
    print(item,end=' ')

print(type(numbers),list(numbers),list(range(-45,-100,-5)))


nums='foooo'

pr=repr(nums)
print(repr(nums))

class Person:
    name='Adam'

    def __repr__(self) -> builtins.str:
        return repr(f'Hello {self.name}')

    def __str__(self) -> builtins.str:
        return f'Hello {self.name}'

print(repr(Person()))