#Python Lists

#Lists are used to store multiple items in a single variable.
#Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
#Lists are created using square brackets:
thislist = ["apple", "banana", "cherry"]
print(thislist)   #Output: ['apple', 'banana', 'cherry']

#List Items
#List items are ordered, changeable, and allow duplicate values.
#List items are indexed, the first item has index [0], the second item has index [1] etc.
#Ordered :- When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
#Changeable :- The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.
#Allow Duplicates :- Since lists are indexed, lists can have items with the same value:

#List Length
#To determine how many items a list has, use the len() function:
print(len(thislist))   #Output: 3

#List Items - Data Types


#List items can be of any data type:
list1 = ["abc", 34, True, 40, "male"]
print(type(list1))  #Output: <class 'list'>


#The list() Constructor
#It is also possible to use the list() constructor when creating a new list.
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)   #Output: ['apple', 'banana', 'cherry']



#Access Items
#List items are indexed and you can access them by referring to the index number:
thislist = ["apple", "banana", "cherry"]
print(thislist[1])   #Output: banana

#Negative Indexing
#Negative indexing means start from the end
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])   #Output: cherry

#Range of Indexes
#You can specify a range of indexes by specifying where to start and where to end the range.
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])   #Output: ['cherry', 'orange', 'kiwi']


#Change Item Value
#To change the value of a specific item, refer to the index number:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)   #Output: ['apple', 'blackcurrant', 'cherry']

#Loop Through a List
#You can loop through the list items by using a for loop:
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)   #Output: apple banana cherry

#Check if Item Exists
#To determine if a specified item is present in a list use the in keyword:
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")   #Output: Yes, 'apple' is in the fruits list

#List Length
#To determine how many items a list has, use the len() function:
thislist = ["apple", "banana", "cherry"]
print(len(thislist))   #Output: 3

#Add Items
#To add an item to the end of the list, use the append() method:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)   #Output: ['apple', 'banana', 'cherry', 'orange']

#To add an item at the specified index, use the insert() method:
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")    
print(thislist)   #Output: ['apple', 'orange', 'banana', 'cherry']

#Remove Item
#There are several methods to remove items from a list:
#The remove() method removes the specified item:
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)   #Output: ['apple', 'cherry']

#The pop() method removes the specified index, (or the last item if index is not specified):
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)   #Output: ['apple', 'banana']

#The del keyword removes the specified index:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)   #Output: ['banana', 'cherry']

#The del keyword can also delete the list completely:
thislist = ["apple", "banana", "cherry"]
del thislist
#print(thislist)   #this will cause an error because "thislist" no longer exists.

#The clear() method empties the list:
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)   #Output: []

#Copy a List
#You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.
#There are ways to make a copy, one way is to use the built-in List method copy().
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)   #Output: ['apple', 'banana', 'cherry']



