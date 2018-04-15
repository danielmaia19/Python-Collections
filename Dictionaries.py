# Introduction to Dictionaries or Dict (for short)

# These are mutable and unsorted

# To create a dict you do using {} NOT []:
courses = {"title": "Python Basics", "Teacher": "Daniel Maia", "Length": 123}
courses # This will return the whole dict
# You cannot use a index on a dict, but dicts use what is called Key-value pairs.

# To get specific parts of the dict we need to specify by the key so:
courses["title"] # will return Python Basics
# The key doesnt have to be a string
# You can have all sorts of data types as the value

# If you try to get a key which doesnt exist like:
#courses["popcorn"] # You will get a KeyError

# You can also nest key-values within a dict like:
courses_full = {"title": "Python Basics", "Teacher": {"first_name":  "Daniel", "last_name": "Maia"}, "Length": 123}
# So now if you go to the key Teacher, you will now see 2 further key-value pairs, first_name Daniel and last-name Maia
courses_full["Teacher"]
# If you just want the first_name for example you do the following:
courses_full["Teacher"]["first_name"] # Just returns Daniel
# ----------------------------------------------------------------------------------------------------------------------

# Editing Keys and Values

# Just create a new dict
courses_example1 = {"title": "Python Basics", "Teacher": {"first_name":  "Daniel", "last_name": "Maia"}, "Length": 123}

# To create a new key in the dict you just need to set the keys value
courses_example1["location"] = "London" # This adds the new key Location and the value London to the dict

# update() lets us set or change, i can do:
courses_example1.update({"title": "Java Basics", "editor": "sublime"}) # Now title has changed to Java Basics and I
# have added editor to the dict with the value of sublime

# You can change a key-value as you add a key
courses_example1["editor"] = "any" # Now the editor is any

# To delete an item from the list you simply do:
del courses_example1["editor"]
# ----------------------------------------------------------------------------------------------------------------------


# Packing and Unpacking Dictionaries

# This is an example of packing
def packing(**kwargs):
    print(kwargs) # It prints a dictionary of the elements


packing(fname="Daniel", lname="Maia") # So this will print: {'fname': 'Daniel', 'lname': 'Maia'}
# ** kwargs (KeyWordArguments) allow you to store a dictionary to later unpack
# To retrieve the dictionary, you simply pass the function name and the then the parameters you like to unpack




def word_count(words):

    #lowercase the string and put in the list format
    word_list = words.lower().split(' ')
    my_dict = {}
    new_list = []

    #loop for count the words in the list
    for word in word_list:
        new_list.append(word)
        new_list.append(word_list.count(word))
    for index, item in enumerate(new_list):
        if index % 2 == 0:
            my_dict[item] = new_list[index+1]

    return my_dict









