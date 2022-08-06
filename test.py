z = [4, 1, 5, 4, 10, 4]

z.sort() #The sort method sorts and alters the original list in place.
z.append(11) #The append method adds an element to the end of a list.
z.remove(4) #The remove method removes the first occurrence of a value in a list.
z.extend([3,2]) #The method extends a list by appending items. The benefit of this is you can add lists together.

z.sort(reverse=True) #Sort a python list from high to low.
z.insert(5, [6,7]) #The insert method inserts an item before the index you provide.


print(z.index(4,1)) #1 specifies the index where you start your search.
print(z.count(4)) #It counts the number of times a value occurs in a list
print(z.pop(3)) #The pop method removes an item at the index you provide. This method will also return the item you removed from the list.
print(z)