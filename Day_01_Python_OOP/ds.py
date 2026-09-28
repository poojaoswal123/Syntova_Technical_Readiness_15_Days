# DS
# List
numbers = [10, 20, 30, 40, 50]
print(numbers[0])
print(numbers[-1])
numbers.append(60)
print(numbers)
numbers.remove(30)
print(numbers)
numbers.insert(1, 15)
print(numbers)
print(numbers.pop())
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
print(numbers[0:4])
print(max(numbers))
print(min(numbers))
print(sum(numbers))
print(len(numbers))
# change 2nd item
numbers[1]= 5
print(numbers)

# count
x = numbers.count(10)
print(x)

# extend
numbers = [10, 20, 30, 40, 50]
new = [60, 70, 80]
numbers.extend(new)
print(numbers)

# index
x = numbers.index(30)
print(x)

if 40 in numbers:
    print("Yes, 40 is in the list")

# Join two list:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

# Append list2 into list1:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)

# extend
print(list1)
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)    

# sort list alphanumerically
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

# sort list numerically:
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

# sort the list descending:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

# sort the list descending:
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

# case insensitive sort:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

# Reverse the order of the list items:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

# TUPLE
# Create a Tuple:
thistuple = ("apple", "banana", "cherry")
print(thistuple)

# Tuples allow duplicate values:
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

# create tuple with one item
thistuple = ("apple",)
print(type(thistuple))

# not a tuple
thistuple = ("apple")
print(type(thistuple))

# find lenght of tuple  
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

# type of tuple
print(type(thistuple))

# print the second item in the tuple
thistuple = ("aaple", "banana", "cherry")
print(thistuple[1])

# print the last item of the tuple
thistuple = ("aaple", "banana", "cherry")
print(thistuple[-1])

# return the 3rd 4th and 5th item
thistuple = ("apple", "banana", "cherry", "mango", "orange")
print(thistuple[2:5])

# return the 1st 2nd 3rd 4th item
thistuple = ("apple", "banana", "cherry", "mango", "orange")
print(thistuple[0:4])

# print from -4 to -1
thistuple = ("apple", "banana", "cherry", "mango", "orange")
print(thistuple[-4:-1])

# Check if Item Exists
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")

# change tuple values:
x = ("apple", "banana", "cherry")
y = list(x)  # list
y[1] = "kiwi"
x = tuple(y)   # tuple
print(x)

# Convert the tuple into a list, add "orange", and convert it back into a tuple:

x = ("apple", "banana", "cherry")
y = list(x)
y.append("orange")
x = tuple(y)
print(x)

#  Add tuple to a tuple
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)

 # Remove Items
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)

# delete item
thistuple = ("apple", "banana", "cherry")
del thistuple

# join 2 tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

# multiply tuple
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)


# count() Method: Return the number of times the value 5 appears in the tuple:
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)
print(x)

# index() Method :
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8)
print(x)

# Create a tuple with 4 elements and print it.
element = ("apple", "orange", "kiwi", "banana")
print(element)

# Try to change a value inside a tuple. What happens?
# my_tuple = (10,20,30,40)
# my_tuple[1]= 25
# error will appear

# Convert a tuple into a list.
# Tuple → List
t = (1, 2, 3)
lst = list(t)
print(lst)   

#  Convert a list into a tuple.
# List → Tuple
lst = [4, 5, 6]
t = tuple(lst)
print(t)   

#  Find the index of an element inside a tuple.
t = (10, 20, 30, 40)
x = t.index(30)
print(x)

# Count occurrences of a value in a tuple.
t = (10,20,40,10,20,30,10,40)
x = t.count(10)
print(x)

# Unpack a tuple into 3 variables and print them.
my_tuple = (100,200,300)
a,b,c = my_tuple
print("a=", a)
print("b=", b)
print("c=", c)


# SETS
# Create a Set:
thisset = {"apple", "banana", "cherry"}
print(thisset)

# Duplicate values will be ignored:
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

#True and 1 is considered the same value:
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

# False and 0 is considered the same value:
thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)

# lenght of set
thisset = {"apple", "banana", "cherry", "apple"}
print(len(thisset))

# type of set
thisset = {"apple", "banana", "cherry", "apple"}
print(type(thisset))

# Check if "banana" is present in the set:
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

# Check if "banana" is NOT present in the set:
thisset = {"apple", "banana", "cherry"}
print("banana" not in thisset)

# Add an item to a set, using the add() method:
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

# add sets
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

# Create a frozenset and check its type:
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))

# Remove "banana" by using the remove() method:
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

# Remove "banana" by using the discard() method:
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

# Remove a random item by using the pop() method:
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

# The clear() method empties the set:
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

# The del keyword will delete the set completely:
thisset = {"apple", "banana", "cherry"}
del thisset

# Join set1 and set2 into a new set:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

# Use | to join two sets:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2
print(set3)

# 4 sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {4,5,6}
set4 = {"d", "e", "f"}
set5 = set1 | set2 | set3 | set4
print(set5)

# Join a set with a tuple:
x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)
print(z)

# The update() method inserts the items in set2 into set1:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

# Join set1 and set2, but keep only the duplicates:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)

# or Use & to join two sets:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 & set2
print(set3)

#  Keep the items that exist in both set1, and set2:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print(set1)

# Keep all items from set1 that are not in set2:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3)

# or Use - to join two sets:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 - set2
print(set3)

# Use the difference_update() method to keep only the items from the first set that are not present in the other set:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)
print(set1)

# The symmetric_difference() method will keep only the elements that are NOT present in both sets. Keep the items that are not present in both sets:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3)

# or Use ^ to join two sets:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 ^ set2
print(set3)


# Create a set with duplicate values. Print it. What happens?
x = {"apple", "orange", "apple", "banana", "orange"}
print(x)

# Add an element to a set.
x = {"apple",  "banana", "orange"}
x.add("cherry")
print(x)

# Remove an element using:
#remove()
x = {"apple",  "banana", "orange"}
x.remove("apple")
print(x)

#discard()
x = {"apple",  "banana", "orange"}
x.discard("banana")
print(x)

# Perform union of two sets.
set1 = {1,2,3}
set2 = {4,5,6}
set3 = set1 | set2
print(set3)

# Perform intersection of two sets.
set1 = {1,2,3}
set2 = {3,4,5,6}
set3 = set1& set2
print(set3)

# Find difference between two sets.
set1 = {1,2,3,4}
set2 = {3,4,5,6}
set3 = set1 - set2
print(set3)

# Check if an element exists in a set.
x = {"apple",  "banana", "orange"}
if "apple" in x:
    print("Yes, 'apple' is in this list")


# Dictionary
# Create and print a dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

# Duplicate values will overwrite existing values:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

# length  of dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(len(thisdict))

# type of dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))

# Get the value of the "model" key:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)

# Get a list of the keys:
x = thisdict.keys()
print(x)

# Add a new item to the original dictionary, and see that the keys list gets updated as well:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()
print(x) #before the change
car["color"] = "white"
print(x) #after the change

# Make a change in the original dictionary, and see that the values list gets updated as well:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x) #before the change
car["year"] = 2020
print(x) #after the change


# Check if "model" is present in the dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

# Change the "year" to 2018:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018  
print(thisdict)

# Update the "year" of the car by using the update() method:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
print(thisdict)

# The pop() method removes the item with the specified key name:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

# The popitem() method removes the last inserted item:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

# The clear() method empties the dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)

# The del keyword removes the item with the specified key name:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

# nested
myfamily = {
    "child1" : {
       "name" : "Emil" ,
       "year" : 2004
    },
    "child2" : {
       "name" : "Tobias" ,
       "year" : 2007
    },
    "child3" : {
       "name" : "Linus" ,
       "year" : 2011
    }
}
print(myfamily)

# Access Items in Nested Dictionaries
myfamily = {
    "child1" : {
       "name" : "Emil" ,
       "year" : 2004
    },
    "child2" : {
       "name" : "Tobias" ,
       "year" : 2007
    },
    "child3" : {
       "name" : "Linus" ,
       "year" : 2011
    }
}
print(myfamily["child2"]["name"])

#  Create a dictionary with keys: name, age, city.
x = {
    "Name": "Pooja",
    "Age": 21,
    "City": "Kolhapur"
}
print(x)

# Access value using a key.
info = {
    "Name": "Pooja",
    "Age": 21,
    "City": "Kolhapur"
}
print(info["Age"])

# Add a new key-value pair.
info = {
    "Name": "Pooja",
    "Age": 21,
    "City": "Kolhapur"
}
info["Gender"] = "Female"
print(info) 

# Update an existing value.
info = {
    "Name": "Pooja",
    "Age": 21,
    "City": "Kolhapur"
}
info["Age"]= 22
print(info)


#  Remove a key using:
# pop()
info = {
    "Name": "Pooja",
    "Age": 21,
    "City": "Kolhapur"
}
info.pop("City")
print(info)

# del
info = {
    "Name": "Pooja",
    "Age": 21,
    "City": "Kolhapur"
}
del info["Age"]
print(info)

# Print all keys of a dictionary.
info = {
    "Name": "Pooja",
    "Age": 21,
    "City": "Kolhapur"
}
print(info.keys())


# Print all values of a dictionary.
info = {
    "Name": "Pooja",
    "Age": 21,
    "City": "Kolhapur"
}
x = info.values()
print(x)

# Loop through dictionary and print:
# keys
info = {
    "Name": "Pooja",
    "Age": 21,
    "City": "Kolhapur"
}
for keys in info.keys():
  print(keys)
# values
info = {
    "Name": "Pooja",
    "Age": 21,
    "City": "Kolhapur"
}
for values in info.values():
  print(values)
# both key and value
info = {
    "Name": "Pooja",
    "Age": 21,
    "City": "Kolhapur"
}
for keys,values in info.items():
  print(keys,values)