#Given a random number:
#You have to return the digits of this number within an array in reverse order.

#Example:
#348597 => [7,9,5,8,4,3]

def digitize(n):
    return [int(d) for d in str(n)][::-1]