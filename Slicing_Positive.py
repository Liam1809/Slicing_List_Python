# Suppose we have a list of letters:

# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# Suppose we want to select from b through f.

# We can do this using the following syntax: letters[start:end], where:

# start is the index of the first element that we want to include in our selection. In this case, we want to start at b, which has index 1.
# end is the index of one more than the last index that we want to include. The last element we want is f, which has index 5, so end needs to be 6.
# sublist = letters[1:6]
# print(sublist)
# This example would yield:
# ['b', 'c', 'd', 'e', 'f']
# Notice that the element at index 6 (which is g) is not included in our selection.
# Creating a selection from a list is called slicing.

suitcase = ['shirt', 'shirt', 'pants', 'pants', 'pajamas', 'books']
# get the first 4 elements of suitcase
beginning = suitcase[0:4]
print(beginning)
# get the middle two items from suitcase
middle = suitcase[2:4]
print(middle)
# geet the last two items from suitcase
Last_two = suitcase[4:6]
print(Last_two)

# If we want to select the first 3 elements of a list, we could use the following code:

# >>> fruits = ['apple', 'banana', 'cherry', 'date']
# >>> print(fruits[0:3])
# ['apple', 'banana', 'cherry']
# When starting at the beginning of the list, it is also valid to omit the 0:

# >>> print(fruits[:3])
# ['apple', 'banana', 'cherry']
# We can do something similar when selecting the last few items of a list:

# >>> print(fruits[2:])
# ['cherry' , 'date']
# We can omit the final index when selecting the final elements from a list.

# If we want to select the last 3 elements of fruits, we can also use this syntax:

# >>> print(fruits[-3:])
# ['banana', 'cherry', 'date']
# We can use negative indexes to count backward from the last element.

suitcase = ['shirt', 'shirt', 'pants', 'pants', 'pajamas', 'books']
# get first 3 elements of suitcase
start = suitcase[:3]
print(start)
# get the final two elements of suitcase
end = suitcase[4:]
print(end)