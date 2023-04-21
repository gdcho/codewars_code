'''
Convert string to camel case

Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.
Examples

"the-stealth-warrior" gets converted to "theStealthWarrior"

"The_Stealth_Warrior" gets converted to "TheStealthWarrior"

"The_Stealth-Warrior" gets converted to "TheStealthWarrior"

'''

## My solution
def to_camel_case(text):
    camelCase = ""
    text = text.replace("-", "_").replace("_", " ")
    lst = text.split()
    for x in lst:
        if lst.index(x) == 0:
            camelCase += x
        else:
            txt = x[0].upper() + x[1:]
            camelCase += txt
    return camelCase

## One line solution
def to_camel_case(text):
    return text[:1] + text.title()[1:].replace('_', '').replace('-', '')