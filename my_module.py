print('Imported Import Module....')

test= 'test string'

def find_index(search_index,target):
    for i,value  in enumerate(search_index):
        if value == target:
            return i
    return -1
    