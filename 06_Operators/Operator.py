#Python Operators
#Operators are used to perform operations on variables and values.

#Python divides the operators in the following groups:

#1.Arithmetic operators  :- Arithmetic operators are used with numeric values to perform common mathematical operations:
#                          Operator  Name          Example
#                          +         Addition      x + y
#                          -         Subtraction   x - y
#                          *         Multiplication x * y   
#                          /         Division       x / y
#                          %         Modulus        x % y
#                          **        Exponentiation x ** y
#                          //        Floor division x // y


#2.Assignment operators  :- Assignment operators are used to assign values to variables:
#                          Operator  Example   Same As
#                          =         x = 5     x = 5
#                          +=        x += 3    x = x + 3
#                          -=        x -= 3    x = x - 3
#                          *=        x *= 3    x = x * 3
#                          /=        x /= 3    x = x / 3
#                          %=        x %= 3    x = x % 3
#                          //=       x //= 3   x = x // 3
#                          **=       x **= 3   x = x ** 3
#                          &=        x &= 3    x = x & 3

#3.Comparison operators  :- Comparison operators are used to compare two values:
#                           Operator  Name                 Example
#                           ==        Equal                x == y
#                           !=        Not equal            x != y
#                           >         Greater than         x > y
#                           <         Less than            x < y
#                           >=        Greater than equal   x >= y
#                           <=        Less than equal      x <= y

#4.Logical operators  :- Logical operators are used to combine conditional statements:
#                        Operator  Description                                                            Example
#                        and       Returns True if both statements are true                           x < 5 and  x < 10
#                        or        Returns True if one of the statements is true                      x < 5 or x < 4
#                        not       Reverse the result, returns False if the result is true            not(x < 5 and x < 10)

#5.Identity operators  :- Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
#                         Operator  Description                                                         Example
#                         is        Returns True if both variables are the same object                  x is y
#                         is not    Returns True if both variables are not the same object              x is not y


#6.Membership operators  :- Membership operators are used to test if a sequence is presented in an object:
#                           Operator  Description                                                                            Example
#                           in        Returns True if a sequence with the specified value is present in the object           x in y
#                           not in    Returns True if a sequence with the specified value is not present in the object       x not in y

#7.Bitwise operators  :- Bitwise operators are used to compare (binary) numbers:
#                        Operator  Name                 Description
#                        &         AND                  Sets each bit to 1 if both bits are 1
#                        |         OR                   Sets each bit to 1 if one of two bits is 1
#                        ^         XOR                  Sets each bit to 1 if only one of two bits is 1
#                        ~         NOT                  Inverts all the bits
#                        <<        Zero fill left shift Shift left by pushing zeros in from the right and let the leftmost bits fall off
#                        >>        Signed right shift   Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off

#8.String operators  :- There are two string operators:
#                       Operator  Description                           Example
#                       +         Concatenation         To concatenate two strings  x + y
#                       *         Repetition            Returns the string multiplied by the number of times  x * y

#9.Print operators  :- There is only one print operator in Python:
#                       Operator  Description                           Example
#                       %         Format                Formats the specified value(s) and insert them inside the string placeholder  %s

#10.Exponentiation operator  :- Python 3.5 added a new operator @ for matrix multiplication. It is used as:
#                                Operator  Description                           Example
#                                @         Matrix multiplication  multiplies values in two matrices


#Operator Precedence

#The following table lists all operators from highest precedence to lowest.

#Operator	Description
#**	        Exponentiation
#~ + -	    Complement, unary plus and minus (method names for the last two are +@ and -@)
#* / % //	Multiply, divide, modulo and floor division
#+ -	        Addition and subtraction
#>> <<	    Right and left bitwise shift
#&	        Bitwise 'AND'
#^ |	    Bitwise exclusive `OR' and regular `OR'
#<= < > >=	Comparison operators
#<> == !=	Equality operators
#= %= /= //= -= += *= **=	Assignment operators
#and or not	Logical operators
#if - else	Conditional expression
#lambda	    Lambda expression


#Example
#Parentheses has the highest precedence, meaning that expressions inside parentheses must be evaluated first
print((6 + 3) - (6 + 3))  #Output: 0





