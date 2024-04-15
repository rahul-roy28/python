'''List'''
'''subjects=['Control System','Computer Network','Economics','CMOS VLSI','Operating System']
print(subjects)
print(len(subjects))
print(subjects[0])
print(subjects[-1])
print(subjects[-3])
print(subjects[0:3])
print(subjects[:3])
print(subjects[2:])'''

'''Modifying List'''

#Add list
'''subjects.append('Python')
print(subjects)'''

#Add a list in a particular position
'''subjects.insert(3,'Python')
print(subjects)'''

#Add a list with an another List
subjects=['Control System','Computer Network','Economics','CMOS VLSI','Operating System']
numb=[8,4,7,1,9]
subjects_2=['Web Dev','UX/UI']
'''subjects.append(subjects_2)
print(subjects)'''
         
subjects.extend(subjects_2)
print(subjects) 

#Remove list
subjects.remove('UX/UI')
print(subjects)

poped=subjects.pop()
print(poped)
print(subjects)

#Reverse List
subjects.reverse()
print(subjects)

#Sorting List
subjects.sort()
numb.sort()
print(numb)
print(subjects)

#Sorting with Reverse
subjects.sort(reverse=True)
numb.sort(reverse=True)
print(numb)
print(subjects)

#Sorting in an another way
sorted_subjects=sorted(subjects)
print(sorted_subjects)

#Numbers
print(min(numb))
print(max(numb))
print(sum(numb))

#Finding values
print(subjects.index('CMOS VLSI'))      
print('CMOS VLSI' in subjects)

#Looping Values
for item in subjects:
 print(item)
 #~!@#$%^&*~!@#$%^&*~!@#$%^&*~!@#$%^&*&^%$@@!%##$%&%%%#$!~@!$%@^%^&^#%$!~#%!#&^*^%
 for index,item in enumerate(subjects):
    print(index,item)
#*~!@@#$%^&*~!@#$%^&*~!@#$%^&*~!@#$%^&*~!@#$%^&*!~@$#%^*^%$!~@#%^~!@$%~~@$#!!$~%#@  

#Convert list into String
subjects_str=' - '.join(subjects)
print(subjects_str)

#Convere string into list
new_list=subjects_str.split(' - ')
print(new_list)   

#Empty List
empty_list=[]
empty_list=set()