name = ['mohammed', 'Ahmed', 'Mosa', 'Khawla', 'Hdeel']

name.reverse()
print(name) # print the list from the end

names = name.copy()
print(names) #make a shallow copy of the list

name.append('Hiba')
print(name) # add value to the end of the list

name.extend(names)
print(name) # add a list to another

print(name.index('Mosa')) # print the index of the element

name.insert(2, 'Ibrahim')
print(name) # add the value befor the index you write

print(name.pop(3)) # print the value of the index

name.remove('mohammed')
print(name) # remove the first value only from the list

name.sort()
print(name) # Arrang elements int only or str only not both

print(name.count('Mosa'))

name.clear()
print(name)
