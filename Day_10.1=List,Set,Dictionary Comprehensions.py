#List Comperhensition
nums=[1,2 ,3,4,5,6,7,8,9]

#I want 'n' for each 'n' in nums
#Regular
my_list=[]
for n in  nums:
    my_list.append(n)
print(my_list)

'''Fun Code
my_list=[]
for n in  nums:
    my_list.append(n)
print(my_list)
    '''
#Comperhensition
my_list=[n for n in nums]
print(my_list)    



#I want 'n*n' for each 'n' in nums
#Regular
my_list=[]
for n in  nums:
    my_list.append(n*n)
print(my_list)
#Comperhensition
my_list=[n*n for n in nums]
print(my_list)  
#Using a map+lambda function to do the same thing as above
my_list=map(lambda n:n*n,nums)
print (list(my_list))




#I want 'n' for each 'n' in nums if 'n' is even
#Regular
my_list=[]
for  n in  nums:
    if  n%2==0:
        my_list.append(n)
print(my_list)
#Comperhensition
my_list=[n for n in nums if n%2==0]
print(my_list)        
#Using filter + lambda function
my_list=filter(lambda n: n%2==0,nums)
print(list(my_list))

#I want a (letter,num)pair  for each letter in 'abcd' in each number in'1234'
#Regular
my_list=[]
for letter in 'abcd':
    for num in range(1,5):
        my_list.append( (letter,num) )
print(my_list)
#Compensation
my_list=[(letter,num) for letter in 'abcd' for num in range(1,5)]
print(my_list)




#Dictionary  Comprehension
names=['Stark','Thor','Banner','Peter','Tijala']
heros=['Iron Man','God of Thunder','Hulk','Spider-Man','Black Panther']
print (list(zip(names,heros)))
#I want a dict{name:hero} for each name, hero in zip(names,heros).
#Regular
my_dict={}
for name,hero in zip(names,heros):
    my_dict[name]=hero
print(my_dict)
#comprehension
my_dict={name:hero for name,hero in zip(names,heros)}
my_dict1={name:hero for name,hero in zip(names,heros) if hero !='Black Panther'} #Exclude Black Panther from the dictionary

print(my_dict)
print(my_dict1)



#Set  comprehension
#Regular
nums=[0,0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9]
my_set=set()
for n in nums:
    my_set.add(n)
print(my_set)

#Compression
my_set={n for n in nums}
print(my_set)