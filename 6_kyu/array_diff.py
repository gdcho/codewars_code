'''
Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

It should remove all values from list a, which are present in list b keeping their order.

If a value is present in b, all of its occurrences must be removed from the other:
'''

## My solution
def array_diff(a, b):
    c = []
    for x in a:
        if x not in b:
            c.append(x)
    return c

## One line code
def array_diff(a, b):
    return [x for x in a if x not in b]