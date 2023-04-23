'''
ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. 
Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

Please note that using encode is considered cheating.

'''

## My solution

def rot13(message):
    lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
             "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", 
             "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    output = ""
    for x in message:
        if x in lower:
            x = lower[lower.index(x) - 13]
            output += x
        elif x in upper: 
            x = upper[upper.index(x) - 13]
            output += x
        else:
            output += x
    return output

## One liner

def rot13(message):
    return message.translate(message.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz','NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'))