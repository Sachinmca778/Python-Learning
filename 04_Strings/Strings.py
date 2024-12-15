#Strings   : Strings in python are surrounded by either single quotation marks, or double quotation marks.'hello' is the same as "hello".

#Multiline Strings : You can assign a multiline string to a variable by using three quotes.
x = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'''
print(x)


#Strings are Arrays
#Python does not have a character data type
a = "Hello, World!"
print(a[1])   #Output: e


#Looping Through a String  
for x in "banana":
    print(x)   #Output: b a n a n a


#String Length    len()
a = "Hello, World!"
print(len(a))   #Output: 13


#Check String    in
txt = "The best things in life are free!"
print("free" in txt)  #Output: True


#Check if NOT    not in
txt = "The best things in life are free!"
print("expensive" not in txt)  #Output: True





#Slicing   [start:end]  : a range of characters by using the slice syntax.
b = "Hello, World!"
print(b[2:5])   #Output: llo  #Note: The search will start at index 2 (included) and end at index 5 (not included).

#Slice From the Start
b = "Hello, World!"
print(b[:5])   #Output: Hello

#Slice To the End
b = "Hello, World!"
print(b[2:])   #Output: llo, World!

#Negative Indexing
b = "Hello, World!"
print(b[-5:-2])   #Output: orl  #Note: Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item etc.






#Modify Strings
#Upper Case
a = "Hello, World!"
print(a.upper())   #Output: HELLO, WORLD!

#Lower Case
a = "Hello, World!"
print(a.lower())   #Output: hello, world!

#Remove Whitespace
a = " Hello, World! "
print(a.strip())   #Output: Hello, World!

#Replace String
a = "Hello, World!"
print(a.replace("H", "J"))   #Output: Jello, World!

#Split String
a = "Hello, World!"
print(a.split(","))   #Output: ['Hello', ' World!']  #Note: The split() method returns a list where the text between the specified separator becomes the list items.




#String Concatenation
a = "Hello"
b = "World"
c = a + b
print(c)   #Output: HelloWorld


#String Format
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))   #Output: My name is John, and I am 36



#Escape Character (Doubt)
#To insert characters that are illegal in a string, use an escape character.
#An escape character is a backslash \ followed by the character you want to insert.
# \'	Single Quote
# \\	Backslash
# \n	New Line
# \r	Carriage Return
# \t	Tab
# \b	Backspace
# \f	Form Feed
# \ooo	Octal value
# \xhh	Hex value
txt = "We are the so-called \"Vikings\" from the north."
print(txt)   #Output: We are the so-called "Vikings" from the north.


#String Methods
#Python has a set of built-in methods that you can use on strings.
#important methods:
#count()	Returns the number of times a specified value occurs in a string
#find()	Searches the string for a specified value and returns the position of where it was found.








