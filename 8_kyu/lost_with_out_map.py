'''
Beginner - Lost Without a Map

Description: 
Given an array of integers, return a new array with each value doubled.

For example:

[1, 2, 3] --> [2, 4, 6]
'''

## My solution
def maps(a):
    lst = []
    for x in a:
        lst.append(x * 2)
    return lst