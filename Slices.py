# Introduction to slices()

# If we use the list below as an example
my_list = [0,1,2,3,4,5,6,7,8,9]
# ----------------------------------------------------------------------------------------------------------------------

# To use slices in Python an example is below:
# The below will output [0, 1, 2, 3, 4]
# 0 is the start
# 5 is the stop, but this is exclusive, up to the 5th item but not including it
# It will return a list with the elements
my_list[0:5]
# RETURNS: [0, 1, 2, 3, 4]
# ----------------------------------------------------------------------------------------------------------------------


# If you try to get an element at a index that does not exist you will get an IndexError see below:
# print(my_list[100])
# But what you can do to get the last 2 items is to do the following:
# I know there is 10 elements in my list so if i start at 8 and end at a index which doesnt exist like 100 or
# even 99999 it will return the last 2 items of the list
my_list[8:100]
# RETURNS: [8, 9]
# ----------------------------------------------------------------------------------------------------------------------


# What we can do is not put anything before the : to start at the begining and then if you supply a index after the :
# where it will stop it will return the start and finish at the index exlusive. see below:
my_list[:2]
# RETURNS: [0, 1]

# If you do the below you get the last 2 items in the list
my_list[5:]
# RETURNS: [8, 9]
# ----------------------------------------------------------------------------------------------------------------------


'''
Making copies using slices
'''
# Now if you do not supply a start or a beginning and leave it as :
my_list[:]
# RETURNS: [0,1,2,3,4,5,6,7,8,9]
# NOTE: I did not just get my list back, I got a COPY of my list

# An example:
messy_list = [1,4,3,5,6,3,8]
# If we print the messy_list its unordered, however, if we sort it:
messy_list.sort() # Now the list is ordered, but now we cannot retrieve the original list because its been sorted.
messy_list # list is now ordered

# So this is where slices comes in handy and makes a copy of the list
messy_list_2 = [1,5,7,3,4,2,3,1] # create a list
clean_list = messy_list_2[:] # We make a copy of the list
clean_list.sort() # We now sorted the new copy list
# Key part about this is that we can retrieve the original list if we needed to
# ----------------------------------------------------------------------------------------------------------------------


# You can also use steps in slices to skip parts, here below we get even numbers by skipping every 2 elements
number_list = list(range(0, 20)) # range(start, finish) a set of numbers from the start to finish. although returns a
#  range object thats why we surround it in a list. Range objects can be sliced but not very transparent
number_list[::2] # This skips every 2 and returns even numbers starting from 0  [0, 2, 4, 6, 8]
number_list[2::2] # This will just start at 2 then skip every 2nd element [2, 4, 6, 8, 10, 12, 14, 16, 18]
# You can also do it to strings like
"Birmignham"[::2] # It will return every second element in the string and return: Brina

# We can also do negative numbers like:
number_list[-2::] # This will return the last 2 elements in the list because the last element starts with -1 [18, 19]
# You cant go backwards in the list such as:
number_list[-1:-5] # This will return a empty list []

# However you can go backwards through the iterable if the step is negative:
number_list[-2:-5:-1] # This will return:[18, 17, 16]

# With this you can reverese the list using a negative step
number_list[::-1] # This will return a reversed copy of the list: [19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0]
# ----------------------------------------------------------------------------------------------------------------------


# Example functions of slicing

def first_4(val):
    return val[:4]


def first_and_last_4(val):
    last = val[-4::]
    val = first_4(val) + last
    return val


def odds(val):
    return val[1::2]


def reverse_evens(var_4):
    ret_val = var_4[::2]
    ret_val.reverse()
    return ret_val


# Deleting or replacing slices

# Just a standard list as before
rainbow = ["Red", "Blue", "Orange", "Green", "Yellow", "Black", "White", "Aqua", "Purple", "Pink"]

# Now re can remove elements in the list using the keyword del.
# Lets try and delete the color Black from the list
del rainbow[5:6] # This will delete the color black and return ['Red', 'Blue', 'Orange', 'Green', 'Yellow', 'White', 'Aqua', 'Purple', 'Pink']
# Now we can also remove multiple items at once, so lets delete White, Aqua and Purple
del rainbow[5:8] # This will now remove white, Aqua and Purple from the list. Note: the indexes are different because
#  we removed black from the list in the previous step

# That was deleting, lets look at adding items to the list
# This can be easily done just using = so lets add black at index 4
rainbow[4:5] = ["Black"] # Black has now been added at index 4

# We can add multiple items to the list too
rainbow[5:] = ["Non-color", "another one"]

# If we wanted to, we can also change multiple elements in the list
# lets say I now want non-color and another color to be Brown and Silver
rainbow[5:] = ["Brown", "Silver"]

# Or we can can change just one item in the list
# Lets change Green and Black to be Green and Baige
rainbow[3:5] = ["Green", "Baige"]

# We can also drop 2 elements and replace it with one like so:
rainbow[-2:] = ["Violet"]
print(rainbow)






