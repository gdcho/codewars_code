'''
Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

    HH = hours, padded to 2 digits, range: 00 - 99
    MM = minutes, padded to 2 digits, range: 00 - 59
    SS = seconds, padded to 2 digits, range: 00 - 59

The maximum time never exceeds 359999 (99:59:59)

'''

## My solution
def make_readable(seconds):
    hours = seconds // 3600
    minutes = (seconds // 60) % 60
    newSeconds = seconds % 60
    return '{:02}:{:02}:{:02}'.format(hours, minutes, newSeconds)

## One line code
def make_readable(s):
    return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)