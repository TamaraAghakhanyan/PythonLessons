# match(); search()

mystr = "You can learn programming language, whatever it is Python2, Python3, Pearl, Java" \
        "javascript or PHP"

# import re
#
# # a = re.match(pattern, string, optional flags)
#
# a = re.match("You", mystr)

mystr = " can  You learn programming language, whatever it is Python2, Python3, Pearl, Java" \
        "javascript or PHP"

arp = "22.22.22.1   0     b4:a9:ff:c8: 45 VLAN#222        L"

# a = re.search(r"(.+?) +(\d) +(.+?)\s{2,}(\w)*",arp)

# . - represents any character except a new line character
# + - means 1 or more repetitions of the expression before it
# * - means 0 or more repetitions of the expression before it
# +,* - greedy expressions - they try to match as much text as possible
# ? - matching as few characters as possible (it's optional)

# a = re.search(r"(.+?) +(\d) +(.+?)\s{2,}(\w)*",arp)
# a.group(1)
# '22.22.22.1'

# without ? mark
# a = re.search(r"(.+) +(\d) +(.+?)\s{2,}(\w)*",arp)
# a.group(1)
# '22.22.22.1  '


# (\d) - any decimal digit
# a.group(2)
# '0'

# \s - matches any whitespace character
#{2,} - means 2 or more repetitions of the expression before it
#(\w) represents:
# a-z
# A-Z
# 0-9
# _(underscore character)

# a.group()
# '22.22.22.1   0   b4:a9:ff:c8: 45 VJAN#222        L'
# a.group(0)
# '22.22.22.1   0   b4:a9:ff:c8: 45 VJAN#222        L'
# a.groups()
# ('22.22.22.1  ', '0', 'b4:a9:ff:c8: 45 VJAN#222', 'L')


# findall(); sub()

# a = re.findall(r"\d\d\. \d{2}\.[0-9] [0-9]\. [0-9] {1,3}", arp)
#
# where:
# \d\d - means that 2 consecutive digits should be expected
# \. - character escaping (escape dot)
# \d{2} - means the occurrence of previous character 2 times ONLY
# \. - to represent the real dot(.) in the pattern
# [0-9] [0-9] - defines a range of characters or a character class should be expected
#               at the particular location in the pattern ([0-9] is doubled, because
#               2 digits are expected
# {1,3} - means the occurrence of previous character between 1 and 3 times



# sub() -  replaces all the occurences of the specified pattern in the target string
#               with provided string

# special sequences:
# \d digits
# \s whitespace
# \w word
# \D - matches any non-digit characters inside the string
# \S - matches any non-whitecpace characters inside the string
# \W - matches any non-word characters inside the string
# \A - matches the character at the beginning of the string
# \Z - matches the character at the end of the string



# \D - to match any non-digit characters inside the string
a = "I enjoy learning programming languages such as Python 3"
        # result = re.search("\D+",a)
        # result.group()
        # 'I enjoy learning programming languages such as Python

# \S - to match any non-whitecpace characters inside the string
        # result = re.search("\S+", a)
        # result.group()
        # 'I'

# \W - matches any non-word characters inside the string
        # result = re.search("\W+", a)
        # result.group()
        # ' '
        # a.index(result.group())
        # 1


# # \A - matches the character at the beginning of the string
        # result = re.search("\AI", a)
        # result.group()
        # 'I'

# \Z - matches the character at the end of the string
        # result = re.search("3\Z", a)
        # result.group()
        # '3'

# sets of characters
# to get all the lowercase letters in the string:
#       result = re.findall("[a-z]", a)

# to get all the uppercase letters in the string:
#       result = re.findall("[A-Z]", a)

# to match all of the lowercase letters in a certain subset of letters:
#       result = re.findall("[a-d]", a)
#       ['a', 'a', 'a', 'a', 'c', 'a']

# to match the subset of characters we are trying to match doesn't contain
# consecutive letters:
#       result = re.findall("[a,P,g]",a)
#       result
#       ['a', 'g', 'g', 'a', 'g', 'a', 'g', 'a', 'g', 'a', 'P']

# to match all the characters in the string except a specific character:
#       result = re.findall("[^a]", a)
#       result
#       ['I', ' ', 'e', 'n', 'j', 'o', 'y', ' ', 'l', 'e', 'r', 'n', 'i', 'n',
#       'g', ' ', 'p', 'r', 'o', 'g', 'r', 'm', 'm', 'i', 'n'
#       , 'g', ' ', 'l', 'n', 'g', 'u', 'g', 'e', 's', ' ', 's
#       ', 'u', 'c', 'h', ' ', 's', ' ', 'P', 'y', 't', 'h', 'o', 'n', ' ', '3']


# to match all the digits in the string:
#       result = re.findall("[0-9]", a)
#       result
#       ['3']

# to match all the digits between 1-5 in the string:\
#         result = re.findall("[1-5]", a)
#         result
#         ['3']

# to match all the occurences of certain digits in the string:
#         result = re.findall("[135]", a)
#         result
#         ['3']

#  to match all the characters in the string except a certain digit:
#         result = re.findall("[^3]", a)
#         result



# OR in RegEx
# to specify two regular expressions for pattern matching at the same time with
# the or operator in between them