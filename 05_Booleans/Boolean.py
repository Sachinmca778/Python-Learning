#Python Booleans :- Booleans represent one of two values: True or False.

print(10 > 9)  #Output: True

#Evaluate Values and Variables
print(bool("Hello"))  #Output: True
print(bool(15))       #Output: True


#Most Values are True
#Almost any value is evaluated to True if it has some sort of content.
#Any string is True, except empty strings.
#Any number is True, except 0.
#Any list, tuple, set, and dictionary are True, except empty ones.
print(bool("abc"))    #Output: True



#Some Values are False
#such as (), [], {}, "", the number 0, and the value None.

#Functions can Return a Boolean
def myFunction() :
  return True
print(myFunction())


