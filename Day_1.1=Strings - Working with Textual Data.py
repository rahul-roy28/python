'''String'''
message="Hello World"
print(message)

'''String Length'''

print(len(message))
print(message[0])
print(message[0:5])
print(message[:5])
print(message[6:])

'''Upper and Lower Case'''
print(message.lower())
print(message.upper())

'''String Count'''
print(message.count('l'))

'''Find String'''
print(message.find('o'))

'''Replace String'''

new_massage=message.replace('World','Universe')
print(new_massage)

'''Combine String'''

greeting='Hello'
name='Rahul'
'''Method 1'''
message=greeting+', '+name+' Welcome!'
'''Method 2'''
new_message2='{}, {} Welcome!'.format(greeting,name)
'''Method 3'''
new_message3=f'{greeting}, {name} Welcome!'
print(message)
print(new_message2)
print(new_message3)