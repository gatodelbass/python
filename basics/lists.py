
dogs = ["salchicha", "scooby", "huesos", "dalmata"]
print(dogs)

#to access last element on list use index -1
print(dogs[-3])
#and you can use negative indexes to get elements from the end

#add elements to the list
#appending at end
print(dogs[0])

dogs.append("lazy")
print(dogs)

#insert method inserts at specific index and moves the other
#elements to the right

#remove element
#del dogs[2]

#print(dogs)

#remove the last element with pop()

#remove by value
#dogs.remove("salchicha")
#print(dogs)

dogs.sort()
print(dogs)


