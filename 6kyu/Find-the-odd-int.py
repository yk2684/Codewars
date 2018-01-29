#Given an array, find the int that appears an odd number of times.

#There will always be only one integer that appears an odd number of times.

def find_it(seq):
    for num in seq:
        count = seq.count(num) 
        if not count % 2 == 0:
            return num 