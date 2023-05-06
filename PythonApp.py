

import myModule

print("This is my app!")

print(myModule.my_var)

myModule.my_function()

from myModule import my_var

# print("This is my app!")
#
# print(my_var)
#
# my_function()
#
# line 17, in <module>
#     my_function()
# NameError: name 'my_function' is not defined

from myModule import *

print("This is my app!")

print(my_var)

my_function()