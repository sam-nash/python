# Using Operators with Strings
# Python supports concatenating strings using the addition operator

welcome = "Welcome"+' '+'to'+' '+'Python!'
print(welcome)

# Python also supports multiplying strings to form a string with a repeating sequence:
hello = 'hello ' * 10
print(hello)
myString = "HelLo WOrld!"
print('The String is : ', myString)
print('The length of the string is : ', len(myString))

"""
multi line comments are enclosed in 3 double quotes which are called docstrings
============================================================================================================
myString = |H|e|l|l|o| |W|o|r|l|d |! |
Index    = |0|1|2|3|4|5|6|7|8|9|10|11| ==> Index starts at 0 when counting from left to right
============================================================================================================
"""
# print the index of a character
print('The index of the character "W" is : ', myString.index('W'))

# print the index of the first occurance of a character
print('The index of first occurance of character "o" is : ', myString.index('o'))

# case sensitive - it gets the index of the upper case character
print('The index of first occurance of character "O" is : ', myString.index('O'))

# SLICING - Extracts a slice of the string
# Usage : "string[start:end:step]"

# In the below example, it extracts the characters between the specified start index(included) and ends at the end index(excluded)
print('The characters between index 4 & 8 are : ', myString[4:8])

# extract just the character at the specified index
print('The character at the index 6 is : ', myString[6])

# The below returns a slice from the start to the number on the left
print('The format ":5" returns characters from start to the 5th char :',
      myString[:5])

# The below returns a slice from the first number to the end.
print('The format "5:" returns characters from the 5th to the last :',
      myString[5:])

# Stepping
print('======Stepping Indexes======')
# start from first, step by 1 char till the end
print('start from first, step by 1 char till the end : ', myString[0:12:1])
# start from first, step by 2 char2 till the end
print('start from first, step by 2 char till the end : ', myString[0: 12: 2])

# Negative Indexes
print('======Negative Indexes======')
"""
============================================================================================================
myString = |H  |e  |l  |l |o |  |W |o |r |l |d |! |
Index    = |-12|-11|-10|-9|-8|-7|-6|-5|-4|-3|-2|-1| ==> Index starts at -1 when counting from right to left
============================================================================================================
"""
# returns the first character from reverse
print('The first character from reverse is : ', myString[-1])

# returns characters from that position specified(included) to last
print('Characters from -6th pos to last are : ',
      myString[-6:])   # same as myString[5:]
# same as myString[0:]
print('Characters from -12th pos to last are: ', myString[-12:])

# returns characters from the beginning up until the specified index(excluded)
print('The characters from start to the position 6 are :',
      myString[:-6], '& the length of the extracted string is : ', len(myString[:-6]))

# returns characters in reverse order
print('The string in reverse order is : ', myString[::-1])
