list = [1, 3, 5, 3, 56, 6, 3, 5, 1]

# append

list.append(99)

# insert at position

list.insert(2, "insert me at index 2")

# remove first item matching value

list.remove(56)

# remove item at index

list.remove(list[2])

# slice from index 5 to 7

print(list[5:7])

# access from end of list - use negative indexes
# last item
print(list[-1])
# penultimate item
print(list[-2])

# get index of a value
print(list.index(99))

# count number of items in list with a value
print(list.count(3))

# sorting
# sorts automatically numerically if full of numbers
list.sort()
print(list)

# Also automatically sorts words alphabetically
wordList = ["banana", "apple", "pineapple"]
wordList.sort()
print(wordList)
