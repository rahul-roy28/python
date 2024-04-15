def function(a,b):
    sum=a+b
    print(sum)
    return sum
#call ing the function with two arguments 5 and  10
function(5,10)
function(3,8)

def another_func(x,y,z):
        result = x + y + z 
        print(result)
        return result
    # calling the function with three argument
another_func(2,4,6)

#####
def hello_function(greeting,name='Rahul'):
    return '{},{}' .format(greeting, name)
print(hello_function('Hello'))
print(hello_function('Hello', 'John'))
print(hello_function('Hello', 'David'))

#Tuples and Dictionary in Function
def student_info(*args,**kwargs):#*args is used to pass multiple non-keyworded variable as tuple. **kwargs is used to pass multiple keyworded arguments to a function as a dictionary
    print(args)
    print(kwargs)
student_info('Physics','Maths',Name='Rahul',Age=22)

#Explanation of the above code
def student_info(*args,**kwargs):
    print(args)
    print(kwargs)
courses=['Physics', 'Maths']
info={'Name': 'Rahul', 'Age': 22}
student_info(courses,info)#In this case the output is not same what we want. 
#So, the solution is ------
def student_info(*args,**kwargs):
    print(args)
    print(kwargs)
courses=['Physics', 'Maths']
info={'Name': 'Rahul', 'Age': 22}
student_info(*courses,**info)

#Example of Function
month_days=[0,31,28,31,30,31,30,31,31,30,31,30,31]

def is_leap(year):
    return year % 4 == 0 and(year%100!=0 or  year%400==0)
def days_in_month(year,month):
    if 1<=month>=12:
        return 'Invalid month number'
    if  month==2 and  is_leap(year):
        return 29
    return month_days[month]
print(is_leap(2000))
print('Days in this month:',days_in_month(2001,3))