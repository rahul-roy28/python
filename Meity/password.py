import random

# Define character sets
characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
special_characters = '`~@#$%^&*()_:;"<>|?.'
numbers = '0123456789'

input_char=int(input('How many characters you want in your Password :')) 

input_special_char=int(input('How many special characters you want in your Password :'))

input_nums=int(input('How many numbers you want in your Password :'))

password_list=[]
for i in range(1,input_char+1): 
    char=random.choice(characters)
    password_list+=char


for i in range(1,input_char+1):
    char=random.choice(special_characters)
    password_list+=char


for i in range(1,input_char+1):
    char=random.choice(numbers)
    password_list+=char


random.shuffle(password_list)


password=""
for char in password_list:
    password+=char
print(password)    
