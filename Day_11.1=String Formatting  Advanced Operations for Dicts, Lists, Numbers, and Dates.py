#For Dictionary
mine={'name':'Rahul','age':22}
sentence='My name is {} I am {} years old'.format(mine['name'],mine['age'])
print(sentence)


sentence='My name is {0} I am {1} years old'.format(mine['name'],mine['age'])
print(sentence)


sentence='My name is {0[name]} I am {1[age]} years old'.format(mine,mine)
print(sentence)


sentence='My name is {0[name]} I am {0[age]} years old'.format(mine)
print(sentence)


#For List
li=['Rahul',23]

sentence='My name is {0[0]} I am {1[1]} years old'.format(li,li)
print(sentence)

sentence='My name is {0[0]} I am {0[1]} years old'.format(li)
print(sentence)





tag='h1'
text='This is a headline'
sentence='<{0}>{1}</{0}>'.format(tag,text)
print(sentence)