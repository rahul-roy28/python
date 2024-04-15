student={'Name':'Puja','Age':21,'City':'Kolkata','Country':'India','Occupation':'Student','Courses':'[BSc, MSc]'}
print(student['Courses'])

print(student.get('Address', 'No Address Provided'))  # If key not found, returns default value

# Adding a new item to the dictionary
student['Email'] = 'pm4504795@gmail.com'
print(student)

# Updating an existing item in the dictionary
student['Name'] = 'Misti'
print(student)

# Removing an item from the dictionary using del keyword
del student['Age']
print(student)

# Adds/Updates items in the dictionary
student.update(Gender='Female',PH='9330287718',Maritallstatus='Single')  
                     #OR
student.update({'Gender':'Female','PH':'9330287718','Maritallstatus':'Single'})  
                     
print(student)

# Checking if a Key is present in the Dictionary    
if 'Courses' in student:
    print("Key exists")
else:
    print( "Key does not exist" )
    
#length
print(len(student))
#keys
print(student.keys())
#values
print(student.values())
#items
print(student.items())

#looping
for keys,values in  student.items():
    #print(f"{keys} : {values}")
    print(keys,' : ', values)