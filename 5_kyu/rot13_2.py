'''
How can you tell an extrovert from an introvert at NSA?
Va gur ryringbef, gur rkgebireg ybbxf ng gur BGURE thl'f fubrf.

I found this joke on USENET, but the punchline is scrambled. Maybe you can decipher it?
According to Wikipedia, ROT13 is frequently used to obfuscate jokes on USENET.

For this task you're only supposed to substitute characters. Not spaces, punctuation, numbers, etc.
'''

## My solution
def rot13(message):
    one = "abcdefghijklm"
    two = "nopqrstuvwxyz"
    
    rot = ""
    
    for m in message:
        if m.lower() in one:
            index = one.index(m.lower())
            rot += two[index] if m.islower() else two[index].upper()
        elif m.lower() in two:
            index = two.index(m.lower())
            rot += one[index] if m.islower() else one[index].upper()
        else:
            rot += m
    return rot

## Other solution
def rot13(message):
    def decode(c):
        if 'a' <= c <= 'z':
            base = 'a'
        elif 'A' <= c <= 'Z':
            base = 'A'
        else:
            return c
        return chr((ord(c) - ord(base) + 13) % 26 + ord(base))
    return "".join(decode(c) for c in message)