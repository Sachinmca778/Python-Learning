#Python Data Types

#Built-in Data Types :- 
#1.Text Type:	str  

X = "Hello World"

#2.Numeric Types:	int, float, complex
X = 20
X = 20.5
X = 1j

#3.Sequence Types:	list, tuple, range
X = ["apple", "banana", "cherry"]
X = ("apple", "banana", "cherry")
X = range(6)

#4.Mapping Type:	dict
X = {"name" : "John", "age" : 36}

#5.Set Types:	set, frozenset
X = {"apple", "banana", "cherry"}
X = frozenset({"apple", "banana", "cherry"})

#6.Boolean Type:	bool
X = True

#7.Binary Types:	bytes, bytearray, memoryview
X = b"Hello"
X = bytearray(5)
X = memoryview(bytes(5))

#Getting the Data Type :- You can get the data type of any object by using the type() function:
X = 5
print(type(X))    #Output: <class 'int'>


##python Numbers

#Type Conversion
x = 1    # int
a = float(x)  #convert from int to float

#Random Number
import random
print(random.randrange(1, 10))  


#Python Casting
#1.Integers
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3








