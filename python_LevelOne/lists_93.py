# mylist = [1,2,3]
print("This is a line of code ")
mylist = ['shdhdshrhs', 23.5, 5, 5, True, 'asdf', [1, 2, 3], False]
print(mylist)
print(len(mylist))
mylist = ['a', 'b', 'c']
print(mylist[-1])
print(mylist[-2])
mylist = ['a', 'b', 'c', 'd', 'e']
print("before reassignment")
print(mylist)
mylist[0] = 'NEW ITEM'
print("ageter reassignment")
print(mylist)
mylist.append("New Item")
print(mylist)
listtwo = ['s', 'www', 'www', 5648]
mylist.extend(listtwo)  # Use of the extend method in list
print(mylist)
