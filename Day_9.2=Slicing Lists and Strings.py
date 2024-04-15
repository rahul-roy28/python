# Slicing List
my_list=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#        0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#      -10,-9,-8,-7,-6,-5,-4,-3,-2,-1 
#list[start:stop:step]

print(my_list[:5])   #from the beginning to index 5 (not included)  
print(my_list[5:])    #from index 5 to the end of the list
print(my_list[-5:])   #last 5 elements from the end
print (my_list[0:9:2])  #elements with odd indexes starting from 0 till 9

#reverse list
print (my_list[::-1])   #reversed list


#Slicing Strings
sample_url='http://roy.com'

#reverse the url
print(sample_url[::-1])

#print the url without the http://
print(sample_url[7:])
#get the top level domain
print(sample_url[-4:])

#print the url without the http:// or top level domain
print(sample_url[7:-4])


