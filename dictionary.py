# Remove items

phone_book = {"Batman": 468426,
              "Cersei": 237734,
              "Ghostbusters": 44678}
print(phone_book)

cersei = phone_book.pop("Cersei")
print(phone_book)
print(cersei)

lst = [2,4,7]
lst.pop()
print(lst)
lst.remove(2)
print(lst)

# Removes and returns the last inserted pair, as a tuple
# In Python versions before 3.7, popitem() removes and returns the random item
lastAdded = phone_book.popitem()
print(lastAdded)

# Dictionary Comprehension

houses = {1: "Gryffindor", 2: "Slytherin", 3: "Hufflepuff", 4: "Ravenclaw"}

for (i,j) in houses.items():
  print(i,j)
  
new_houses = {n**2: house + "!" for (n, house) in houses.items()}
print(houses)
print(new_houses)
