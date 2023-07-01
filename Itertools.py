# Itertools

list1 = [1, 2, 3, "a", "b", "c"]
list2 = [101, 102, 103, "X", "Y"]

# chain() -     This function simply takes several sequences
#               as arguments and chains them together.

'''chain(list1, list2)
< itertools.chain
object
at
0x10f5c79d0 >
for i in chain(list1, list2):
    print(i)

        1
        2
        3
        a
        b
        c
        101
        102
        103
        X
        Y'''

'''list(chain(list1, list2))
[1, 2, 3, 'a', 'b', 'c', 101, 102, 103, 'X', 'Y']'''


# count() -     function returns an iterator that generates consecutive
#               integers until you stop it.Otherwise it will go on forever.
#               That's why you should use it wisely so you won't end up
#               with an infinite loop and a huge computer resource
#               consumption.

# count(element1,element2)
# where:
# element1 - starting point
# element2 - a step to increment by

'''for i in count(10, 2.5):
    if i <= 50:
        print(i)
    else:
        break

        10
        12.5
        15.0
        17.5
        20.0
        22.5
        25.0
        27.5
        30.0
        32.5
        35.0
        37.5
        40.0
        42.5
        45.0
        47.5
        50.0'''

# cycle() -     This function returns an iterator that simply repeats
#               the value given as an argument infinitely.
#               Again, if you use it inside the program, you have to
#               find a way to break out of the infinite loop.
#               Otherwise your program will crash.

'''a = range(11, 16)
for i in range(a):
    print(i)'''



# filterfalse() -   It will return the elements for which the function you
#                   provide as an argument returns False.

'''filterfalse(lambda x: x < 5, [1, 2, 3, 4, 5, 6, 7])
<itertools.filterfalse object at 0x105854d00>

list(filterfalse(lambda x: x < 5, [1, 2, 3, 4, 5, 6, 7]))
[5, 6, 7]'''


# islice() -    it basically does the same thing as
#               list slices and string slices.

'''range(10)
range(0, 10)
list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list(range(10)) [2:9:2]
[2, 4, 6, 8]
islice(range(10), 2, 9, 2)
<itertools.islice object at 0x105736590>
list(islice(range(10), 2, 9, 2))
[2, 4, 6, 8]'''


