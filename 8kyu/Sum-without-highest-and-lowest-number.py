#Sum all the numbers of the array (in F# and Haskell you get a list) except the highest and the lowest element (the value, not the index!).
#(The highest/lowest element is respectively only one element at each edge, even if there are more than one with the same value!)

#Example:
#{ 6, 2, 1, 8, 10 } => 16
#{ 1, 1, 11, 2, 3 } => 6

#If array is empty, null or None, or if only 1 Element exists, return 0.

def sum_array(arr):
    return 0 if not arr else sum(sorted(arr)[1:-1])