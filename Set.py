name = {'mohammed', 'Ahmed', 'Mosa', 'Khawla', 'Hdeel'}
friends = {'mohammednor', 'Ahmed', 'Mosa', 'Khokha', 'Hdoo'}

# print(name.pop()) # print a random value from the set then remove it

print(2,'#'*20)

names = name.copy()
print(names) #make a shallow copy of the set

print(3,'#'*20)

name.add('Hiba')
print(name) # add value to the set

print(4,'#'*20)

name.union(friends)
print(name) # add a set to another without repeat

print(5,'#'*20)

name.remove('mohammed')
print(name) # remove the first value only from the set

print(6,'#'*20)

name.discard('mohammed')
print(name) # remove the first value only from the set and it didn't give error if value do not excist

print(7,'#'*20)

name.update(friends)
print(name) # union the 2sets without repeat

print(8,'#'*20)

print(name.difference(friends)) # print the elements that found in the 1st set butm not found in the 2nd set

print(9,'#'*20)

name.difference_update(friends)
print(name) # make difference() work then replace the result with the original set

print(10,'#'*20)

print(name.intersection(friends)) # print the elements that excist in the 2 sets

print(11,'#'*20)

name.intersection_update(friends)
print(name) # make intersection() work then replace the result with the original set

print(12,'#'*20)

print(name.symmetric_difference(friends)) # print the elements that not excist in the 2 sets

print(13,'#'*20)

name.symmetric_difference_update(friends)
print(name) # make symmetric_difference_update() work then replace the result with the original set

print(14,'#'*20)

print(name.issuperset(friends)) # check if the elements of friends are found in name

print(15,'#'*20)

print(name.issubset(friends)) # check if the elements of name are found in friends

print(16,'#'*20)

print(name.isdisjoint(friends)) # check if element of every set are not found in other set

print(17,'#'*20)

name.clear()
print(name)