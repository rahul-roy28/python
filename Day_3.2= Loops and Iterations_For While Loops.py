#For loop
nums=[1,2,3,4]
for num in nums:
    print(num)

#Break Statement
nums=[1,2,3,4,5,6,7,8,9]
for num in nums:
    if num==4:
        print('found!')
        break
    print(num)

#Continue statement
nums=[1,2,3,4,5,6,7,8,9]
for num in nums:
    if num==4:
        print('found!')
        continue
    print(num)


#Looping inside a loop
nums=[1,2,3,4,5,6,7,8,9]
for num in nums: 
    for letter in 'abc':
      print(num,letter)
      
#Range Statement
for i in range(10):
    print(i)
    print("------------------------")
    print("\n\n")
    print('Done')

#####
for i in range(100,121):
    print(i)
    print("------------------------")
    print("\n\n")
    print('Done')
 
#While loop
x=0
while x<10:
    print(x)
    x+=1
print('Done')
#Break and Continue statements
x=0
while x<10:
    if x == 3:
        print(x,'is the number.')
        break
    print(x)
    x+=1
print('Done')

#Infinite Loop
#This will keep running until you manually stop the program.
#It is generally not a good idea to leave an infinite loop running!
#while True:
#   print("I am stuck in this loop forever.")
'''
x=0
while True:
    print(x)
    x+=1
    '''