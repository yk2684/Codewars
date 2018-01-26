#This time no story, no theory. The examples below show you how to write function accum:

#Examples:
#accum("abcd")    # "A-Bb-Ccc-Dddd"
#accum("RqaEzty") # "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
#accum("cwAt")    # "C-Ww-Aaa-Tttt"
#The parameter of accum is a string which includes only letters from a..z and A..Z.

def accum(s):
    return '-'.join([str(s[i]*(i+1)).capitalize() for i in range(len(s))])