''' converts written strings of numbers to numbers '''

def numberfyer(inp):
    # for the bases/ones
    nums = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6,
            "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11,
            "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15,
            "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19}

    # for the tens
    tens = {"ten": 10, "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50,
            "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90}

    # for the zeroes
    digits = {"ten": 10, "hundred": 100, "thousand": 1000, "million": 1000000, "billion": 1000000000}

    inp = inp.split()
    finale = 0

    # going through the input number by index to generate the number
    for i in range(len(inp)):
        temp = 0
        if inp[i] in nums:
            temp = temp + nums[inp[i]]
        if inp[i] in tens:
            temp = temp + tens[inp[i]]
        if i+1 < len(inp) and inp[i+1] in digits:
            # handles to ensure you don't just keep multiplying
            # bc when i originally put six thousand seven hundred it did 6000700
            temp = temp * digits[inp[i+1]]
            i+=1
        if i+1 < len(inp) and inp[i+1] in digits:
            # for cases like two hundred billion or one hundred thousand
            temp = temp * digits[inp[i+1]]
            i+=1
        finale += temp

    # add commas
    finale = list(str(finale))
    for i in reversed(range(3, len(finale), 3)): # reversed so it doesn't fuck up the indexes
        finale.insert(i*-1, ',') # makes sure it inserts into the right place

    return ''.join(finale)

number = input('enter number: ')
print(numberfyer(number))

assert(numberfyer("seventeen") == '17')
assert(numberfyer("sixty one") == '61')
assert(numberfyer("two hundred billion") == '200,000,000,000')
assert(numberfyer("eight thousand three hundred") == '8,300')
assert(numberfyer("fifteen thousand") == '15,000')
assert(numberfyer("three hundred million") == '300,000,000')
assert(numberfyer("four hundred eighty three") == '483')