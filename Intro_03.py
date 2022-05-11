# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 10:31:56 2022

@author: João
"""

#boolean
print(10 > 9)
print(10 == 9)
print(10 < 9)

print(bool("Hello"))
print(bool(15))

x = 3
y = 4

print(bool(x))
print(bool(y))

#Arithmetic Operators

#modulus operator - mostra o resto da divisão inteira
print(x % y)
# ** - exponecial
print(y ** x)
# // - floor division - divisão inteira
print(y//x)#4/3 =1,3333 ->1

#Python Assignment Operators

'''
Operator Example Same As
     =	  x = 5 	x = 5
    += 	 x += 3  	x = x + 3	
    -=	 x -= 3 	x = x - 3	
    *=	 x *= 3	    x = x * 3	
    /=	 x /= 3 	x = x / 3	
    %=	 x %= 3 	x = x % 3	
    //=	 x //= 3	x = x // 3	
    **=	 x **= 3	x = x ** 3	
    &=	 x &= 3 	x = x & 3	# & - bitwise AND
    |=	 x |= 3 	x = x | 3	# | - bitwise OR
    ^=	 x ^= 3 	x = x ^ 3	# ^ - bitwise XOR
    >>=	 x >>= 3	x = x >> 3	# >> - bitwise right shift
    <<=	 x <<= 3	x = x << 3  # << - bitwise left shift
    '''                         # ~ - bitwise NOT
    

#Python Comparison Operators

'''
==	Equal	x == y	
!=	Not equal	x != y	
>	Greater than	x > y	
<	Less than	x < y	
>=	Greater than or equal to	x >= y	
<=	Less than or equal to	x <= y
'''

#Python Logical Operators
'''
and 	Returns True if both statements are true	                x < 5 and  x < 10	
or	   Returns True if one of the statements is true	            x < 5 or x < 4	
not	   Reverse the result, returns False if the result is true    	not(x < 5 and x < 10)'''

#Python Identity Operators
'''
is 	Returns True if both variables are the same object	x is y	
is not	Returns True if both variables are not the same object	x is not y'''

#Python Membership Operators
#Membership operators are used to test if a sequence is presented in an object:
    
'''
in 	Returns True if a sequence with the specified value is present in the object	x in y	
not in	Returns True if a sequence with the specified value is not present in the object	x not in y'''

#Python Bitwise Operators
#Bitwise operators are used to compare (binary) numbers:
'''
& 	AND 	Sets each bit to 1 if both bits are 1
|	OR  	Sets each bit to 1 if one of two bits is 1
 ^	XOR 	Sets each bit to 1 if only one of two bits is 1
~ 	NOT 	Inverts all the bits
<<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
>>	Signed right shift	    Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off'''



