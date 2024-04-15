#if and else statements
language='Python'
if language=='Python':
    print("Python")
else:
    print("Incorrect, the correct answer is Python.")
    
## Adding an elif statement to handle other possible languages
language='java'
if language=='Python':
    print("Python")
elif language=='java':
    print("Java")    
else:
    print("Incorrect, the correct answer is Python.")

#Handling multiple conditions with if-elif-else
age=15
if age<3:
    print('Baby')
elif 3<=age<6:
    print('Toddler')
elif 6<=age<9:
    print('Preschooler')
else:
    print('Adult')  
'''   
#Asking user for input and using it in a conditional statement.
user_input = input("Enter your favorite programming language: ")
if user_input == 'Python':
    print("That's great! I also love Python.")
elif user_input == 'Java':
        print("I prefer Java too.") 
else:
    print("Don't you like either?")
    '''
'''Boolean function(and or not)'''

#and
user_input='Admin'
validity=False
if user_input=='Admin' and validity:
    print("Welcome Admin! You have access to all features.")
else:
    print("Sorry, you don't have access.") #This will execute because validity is False.
    
#or
user_input='Admin'
validity=False
if user_input=='Admin' or validity:
    print("Welcome Admin! You have access to all features.")#This will execute because validity is False.
else:
    print("Sorry, you don't have access.") 
    
#not
user_input='Admin'
log_in=True
if not log_in:
    input("Please Log in....")
else:
    print("Welcome!") 
    
#False values
#(1)False
#(2)None
#(3)Zero of any numeric types
#(4)Any empty sequence, for example, '',(),[].
#(5)Any empty mapping, for example, {}.


condition=[]#or None ,0,'',[],(),{},
if condition:
      print("This is True") 
else:
    print("This is false")       