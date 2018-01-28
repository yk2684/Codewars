#Write function avg which calculates average of numbers in given list.

#Python: Due to rounding issues please do not use statistics.mean or such.

def find_average(array):
    return 0 if not array else sum(array)/len(array)