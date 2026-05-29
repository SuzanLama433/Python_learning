'''
====================MODULE=========================

Module:-- It is a file that contain python code(variable, function, loop, oop) 
that is useable for other program.

Scripts,module ,package,library
package
folder -->
       __init__.py
       module.py
       module2.py
       module3.py

library
folder -
->package1
->package2
->package3

IMPORTANCE of MODEULE:

1.Reuseable
2.Code Maintain
3.Debugging

TYPE of MODULE

1.Built in Module
2.User define Module
3.External Module

'''
print('==========Built in Module========')
# Pre define by python 
import random
a = random.choices([1,2,3], k=2)
print(a)

print("====================================")

import keyword
print(keyword.kwlist)

print("====================================")

import calendar
print(calendar.calendar(2026))
print(calendar.month(2025,5))

print("====================================")

import datetime 
print(datetime.datetime.now())
print(datetime.datetime.now().year)
print(datetime.datetime.now().month)
print(datetime.datetime.now().time)

print("====================================")

import math
#from math import sqrt,ceil
print(math.sqrt(36))
a=math.radians(30)
print(math.sin(a))
print(math.floor(1.455))
print(math.ceil(3,990))
print(round(3.1415))
print(round(3.1415, 1))
print(dir(math))

print("====================================")

from file import names, show #import file from module
print(names) 
show(2,3)


