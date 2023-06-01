'''
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.
'''
## My solution
def move_zeros(lst):
    zeros = []
    while lst.count(0) > 0:
        zeros.append(0)
        lst.remove(0)
    lst.extend(zeros)
    return lst

## Other solution
def move_zeros(arr):
    l = [i for i in arr if isinstance(i, bool) or i!=0]
    return l+[0]*(len(arr)-len(l))

def move_zeros(array):
    return sorted(array, key=lambda x: x==0 and type(x) is not bool)

def move_zeros(array):
    return sorted(array, key=lambda x: not x)