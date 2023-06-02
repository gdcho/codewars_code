'''
In this kata we want to convert a string into an integer. The strings simply represent the numbers in words.

Examples:

    "one" => 1
    "twenty" => 20
    "two hundred forty-six" => 246
    "seven hundred eighty-three thousand nine hundred and nineteen" => 783919

Additional Notes:

    The minimum number is "zero" (inclusively)
    The maximum number, which must be supported is 1 million (inclusively)
    The "and" in e.g. "one hundred and twenty-four" is optional, in some cases it's present and in others it's not
    All tested numbers are valid, you don't need to validate them

'''
## My Solution:
def parse_int(string):
    words = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
        'ten': 10,
        'eleven': 11,
        'twelve': 12,
        'thirteen': 13,
        'fourteen': 14,
        'fifteen': 15,
        'sixteen': 16,
        'seventeen': 17,
        'eighteen': 18,
        'nineteen': 19,
        'twenty': 20,
        'thirty': 30,
        'forty': 40,
        'fifty': 50,
        'sixty': 60,
        'seventy': 70,
        'eighty': 80,
        'ninety': 90,
        'hundred': 100,
        'thousand': 1000,
        'million': 1000000
    }

    parts = string.replace(' and', '').replace('-', ' ').split()
    total = 0
    temp = 0

    for part in parts:
        if part in words:
            value = words[part]
            if value == 100:
                temp *= value
            elif value >= 1000:
                temp *= value
                total += temp
                temp = 0
            else:
                temp += value
    total += temp
    return total

## Other Solution:
ONES = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
        'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 
        'eighteen', 'nineteen']
TENS = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

def parse_int(string):
    print(string)
    numbers = []
    for token in string.replace('-', ' ').split(' '):
        if token in ONES:
            numbers.append(ONES.index(token))
        elif token in TENS:
            numbers.append((TENS.index(token) + 2) * 10)
        elif token == 'hundred':
            numbers[-1] *= 100
        elif token == 'thousand':
            numbers = [x * 1000 for x in numbers]
        elif token == 'million':
            numbers = [x * 1000000 for x in numbers]
    return sum(numbers)