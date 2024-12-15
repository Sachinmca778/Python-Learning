#Variables :- Variables are containers for storing data values.

#Creating Variables
x = 5
y = "John"


#Casting
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#Get the Type  :- You can get the data type of a variable with the type() function.
x = 5
print(type(x))

#Single or Double Quotes?  :- String variables can be declared either by using single or double quotes:
x = "John"
# is the same as
x = 'John'

#Case-Sensitive  :- Variable names are case-sensitive.
a = 4
A = "Sally"
#A will not overwrite a


#Variable Names :- 1.A variable name cannot be any of the Python keywords.
#                  2.A variable name must start with a letter or the underscore character.
#                  3.A variable name cannot start with a number.

#multi words variable name :- 1.Camel Case :  myVariableName
#                             2.Pascal Case : MyVariableName
#                             3.Snake Case : my_variable_name


#Many Values to Multiple Variables :- Python allows you to assign values to multiple variables in one line
x, y, z = "Orange", "Banana", "Cherry"
print(x)

#One Value to Multiple Variables 
x = y = z = "Orange"
print(y)

#Unpack a Collection :- If you have a collection of values in a list, tuple etc. Python allows you extract the values into variables. This is called unpacking.
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)

#Output Variables
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)    #Output: Python is awesome
print(x + y + z)  #Output: Pythonisawesome

#Global Variables :- Variables that are created outside of a function and used by everyone, both inside of functions and outside.
 
x = 'sachin'
def func():
    print('My name is '+x)
func()

#The global Keyword :- If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)








