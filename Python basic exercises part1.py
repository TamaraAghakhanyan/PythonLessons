# 1. Write a Python program to print the following
# string in a specific format (see the output).
'''print('Twinkle, twinkle, little star,')
print("         ", "How I wonder what you are!")
print("                     ", "Up above the world so high,")
print("                     ", "Like a diamond in the sky.")
print('Twinkle, twinkle, little star,')
print("         ", "How I wonder what you are!")'''

'''print('Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\tHow I wonder what you are!')'''


#Write a Python program to count the number of characters (character frequency)
# in a string.
# def char_frequency(str1):
#     dict = {}
#     for n in str1:
#         keys = dict.keys()
#         if n in keys:
#             dict[n] += 1
#         else:
#             dict[n] = 1
#     return dict
# print(char_frequency('google.com'))

num = int(input('Write a value: '))
counter = int(input('break value: '))

result = 0

for i in range(1, num):
    result += i
    if result == counter:
        break
print( result, 'pppp')














