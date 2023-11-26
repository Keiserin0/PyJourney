# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 00:11:12 2022

@author: tanka
"""

#tuples are immutable, meaning it can't be changed after created

#print the list x
x = ["I", "love", "you"]
print(x)

#add another love to the last index
x.append("love")
print(x)

y = ["Python", "language"]

#merge list y into list x
x.extend(y)
print(x)
print()

#count the amount of time "Love" appear in list of x
count_x = x.count("love")
print(f"The number of times/count love occurs in list_x is: {count_x}")

#shows the index of the first "love"
love_count = x.index("love")
print(f"The lowest index of love that appears in lists_x is: {love_count}")
print()

#append but can choose index to insert
x.insert(1, "hate")
print(f"Content of list_x after object hate is added: {x}")

#removes first "love" from list
x.remove("love")
print(f"Remove the object love from list_x: {x}")

# Reverse the list according to index technically... flipped
x.reverse()
print(f"Reversed list_x result: {x}")

list_z = list(reversed(x))
print(f"list_z is reversed of new list_x: {list_z}")