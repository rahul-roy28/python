#List Sorting


li=[9,2,4,1,6,8,3,5,7,0]
s_li=sorted(li)
print('Sorted list:', s_li)

#Sorting in an another way
li.sort()
print('Sorted using sort method:', li)


#reverse sort
li=[9,2,4,1,6,8,3,5,7,0]
s_li=sorted(li,reverse=True)
print('Sorted list:', s_li)

#Sorting in an another way
li.sort(reverse=True)
print('Sorted using sort method:', li)


#Tuples Sorting

tup=(3,5,7,9,1,4,6,8,2,0)
s_tup=sorted(tup)
print('Sorted Touples:',s_tup)

#Tuples Dictionary
dic={'Rahul','Puja','Sajeeb','HIllol','Ayeshee','Rajorshi','Udita','Srijan'}
s_dic=sorted(dic)
print('Sorted Dict:',s_dic)

#Absolute Sorting
li=[-6,-4,-5,1,2,3]
s_li=sorted(li,key=abs)
print('Shorted List :',s_li)
