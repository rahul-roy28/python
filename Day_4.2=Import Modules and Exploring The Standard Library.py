# No.1:

import my_module
subject=['math','english',  'computer', 'history', 'biology']

index=my_module.find_index(subject,'english')
print(index)


#No.2:

import my_module as mm
subject=['math','english', 'chinese', 'computer', 'history', 'biology']

index=mm.find_index(subject,'english')#use the function find_index in my_module
print(index)


#No.3:

from my_module import find_index
subject=['math','english', 'chinese', 'computer', 'history', 'biology']

index=find_index(subject,'english')#call the function from the module directly without using "as" keyword 
print(index)


#No.4:
from my_module import find_index ,test
subject=['math','english', 'chinese', 'computer', 'history', 'biology']

index=find_index(subject,'english')

print(index)
print(test)#call the function test in my_module 

#call the function test in file "my_module" 
from my_module import find_index ,test
import sys
subject=['math','english', 'chinese', 'computer', 'history', 'biology']

index=find_index(subject,'english')
print(sys.path)#show the path of python search for modules

#Random Module
import random
subject=['math','english', 'chinese', 'computer', 'history', 'biology']
random_course=random.choice(subject)#select one subject randomly from list
print('your course is : ',random_course)

#Math Module
import math
rads=math.radians(180) #convert degree to radian
print("the radian of 180 degrees is ",rads)
print(math.sin(rads))   #calculate sin value by using radian

#Datetime and Calender Module
import datetime
import calendar
print(datetime.date.today())#get today's date
print(calendar.isleap(2000))    #judge if it's a leap year or not, return True/False

#OS Module
import os
print(os.name)     #return name of operating system e.g., posix for Unix / Linux, nt for Windows
print(os.getcwd()) #return current working directory
print(os.__file__)