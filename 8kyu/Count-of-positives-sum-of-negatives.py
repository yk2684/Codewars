#Given an array of integers.
#Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers.

#If the input array is empty or null, return an empty array:

#For example:
#input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
#return [10, -65].

def basic_op(operator, value1, value2):
    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1 - value2
    elif operator == '*':
        return value1 * value2
    elif operator == '/':
        return value1 / value2