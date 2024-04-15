set_1={'Control System','Computer Network','Economics','CMOS VLSI','Operating System'}
set_2={'python','web dev','Computer Network','CMOS VLSI'}
print('CMOS VLSI' in set_1)

#Common Between 2 sets
print(set_1.intersection(set_2))

#Difference Between 2 sets
print(set_1.difference(set_2))

#Combine 2 sets
print(set_1.union(set_2))

#Empty sets
empty_set=set()