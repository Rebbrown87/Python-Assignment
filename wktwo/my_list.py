#  Creating an empty list
my_list = []

#  Appending elements
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#  Inserting 15 at the second position (index 1)
my_list.insert(1, 15)

#  Extending the list with [50, 60, 70]
my_list.extend([50, 60, 70])

#  Remove the last element
my_list.pop()

# Sorting the list in ascending order
my_list.sort()

#  Finding and printing the index of value 30
index_of_30 = my_list.index(30)
print("Sorted List:", my_list)
print("Index of 30:", index_of_30)
