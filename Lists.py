# Introduction to lists

# Assigning basic list to a variable
# This will then return a list of the elements in that list: [1, 2, 3, 'Daniel', 'Maia']
my_list = [1,2,3,"Daniel", "Maia", 2.3]
print(my_list)
# ----------------------------------------------------------------------------------------------------------------


# Creating a list: within in a list you simply add another [] within in the list as seen below:
# This will then return: [1, 2, 3, 'Daniel', 'Maia', ["Another", "List"]]
my_list_2 = [1, 2, 3, 'Daniel', 'Maia', ["Another", "List"]]
# ---------------------------------------------------------------------------------------------------------------------


# Gowing lists:
favourite_things = ["raindrops on roses", "whiskers on kittens", "bright copper kettles"]
# Can a new item to the list by using the + operand as below:
favourite_things + ["warm wollen mittens"]
# however this change is not permanent to make it permanent you will need to use the +=
favourite_things += ["warm wollen mittens"]
# ---------------------------------------------------------------------------------------------------------------------


# Alternatively you can use the append() method which works the same way:
# return ['raindrops on roses', 'whiskers on kittens', 'bright copper kettles', 'warm wollen mittens', ['another item in the list']]
favourite_things.append(["another item in the list"])
#                       ^                          ^
# These need to be removed if you don't want a another list in a list
# As you can see the append() creates another list to the list you added to unless you remove [].
# ---------------------------------------------------------------------------------------------------------------------


# To remove you can use the del keyword and -1 as its the last item in the list
del favourite_things[-1]
# ---------------------------------------------------------------------------------------------------------------------


# To add an item with the append() method, as just an item and not another list:
favourite_things.append("Another item added 1")
# Just need to remove the []
# This will then return 'Another item added 1'] at the end of the list
# ---------------------------------------------------------------------------------------------------------------------


# Another option is the extend() function, this takes a list [] and adds it to another list as items
favourite_things.extend(["item added 2", "items added 3"])
# When you run it 'item added 2', 'items added 3' has been added to the list
# This can be done as long as the item is iterable so:
a = [1,2,3]
a.extend("abc")
# This will return [1, 2, 3, 'a', 'b', 'c']
# ---------------------------------------------------------------------------------------------------------------------


# The insert() function takes 2 arguments the index, where in the list you want the item to go and then the item itself
favourite_things.insert(0, "Added to the begining of the list")
# This is then added to the beginning of the list and can be accessed with the [0] index
# ---------------------------------------------------------------------------------------------------------------------


# Removing Items from a list
'''
Removing a element in the list you use the function remove()
however, when using this function if there are more than one element the same and use remove it will only remove the
first instance.
When you remove an item from the list, the item is not returned and its lost forever
'''
remove_list = [1,2,3,1]
remove_list.remove(1)
remove_list.remove(1)
# Now it will remove all the 1's in the list
# ----------------------------------------------------------------------------------------------------------------------

'''
Removing an item from a list but returning the value back you use the function pop()
see the examples of pop() below
'''
# 1. Create a list
my_list = [1,2,3,4,5]
# Remove an item and return it using the index
my_list.pop(0)
# Now we can use pop() and assign it to a variable like so:
element = my_list.pop(0)
element
# Now we can access the element variable whenever we want but you will notice the my_list list no longer has that variable
