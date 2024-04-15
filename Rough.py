'''
file=open('test.txt','r')
print(file.read())
'''
'''
subjects=['Control System','Computer Network','Economics','CMOS VLSI','Operating System']
numb=[8,4,7,1,9]
subjects_2=['Web Dev','UX/UI']

for index,item in enumerate(subjects):
    print(index,item)
    
    
    
# Adding an elif statement to handle other possible languages
language='Java'
if language=='Python':
   print("Correct!")
elif language=='Java':
   print("That's not Python, it's Java.")
else:
   print("I don't recognize that language.")    
 
 
   '''
   
   #infinite Loop
'''
x=0
while x<10:
    if x == 3:
      print(x,"is the number.")
      continue
    print(x)
    x+=1
print('Done')   
'''
#Finding Leap Year
'''
month_days=[0,31,28,31,30,31,30,31,31,30,31,30,31]

def leap_year(year):
   return  year%4==0 and (year%100!=0 or year%400==0)
print('Leap Year:',leap_year(2000))

def days_in_month(year,month):
   if not  month in range(1,13):
       return 'Invalid'
   if month==2 and  leap_year(year):
      return 29
   return month_days[month]
print('Days in this Month is:',days_in_month(2000,12))
'''