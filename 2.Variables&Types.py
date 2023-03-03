# Every variable in Python is an object.
# There is no need to declare variables & their types before using them

# NUMBERS - Python supports two types of numbers - integers(whole numbers) and floating point numbers(decimals)

# define an integer
intVal = 10
print("The Integer value is : ", intVal)
print("The integer value is : %d" % intVal)
if (isinstance(intVal, int)):
    print(isinstance(intVal, int), " : this is an integer")
# define a float by assigning a value to it
floatVal = 10.0
print("The Float value is : ", floatVal)
# Or it can be used with precision
print("The  Float value is : %f" % floatVal)
# or by using the float function
floatVal = float(15)
print("The New Float value is : ",  floatVal)

if (isinstance(floatVal, float)):
    print(isinstance(floatVal, float), " : this is a float")

# Strings - are defined either with a single quote or a double quotes.
strVal1 = 'Welcome'
strVal2 = "Home"
print('The String values are : ', strVal1, strVal2)

# Two or more string literals enclosed between quotes next to each other are automatically concatenated
strCatUsingSpace = 'Concat' "enated"
print('The concatenated String is : ', strCatUsingSpace)
strCatUsingPlus = 'This' + 'That'
print(strCatUsingPlus)
# escape with a '\' if a quote is part of the string.
strSingleQuote1 = 'It\'s a beautiful day'
strDblQuote1 = "\"Yay\", I did this"
# OR
# enclose single quoted string inside double quotes
strSingleQuote2 = "It's a beautiful day"
# enclose double quoted string inside single quotes
strDblQuote2 = '"Yay", I did this'
print('Single quotes inside single quotes escaped with a backslash : ' +
      strSingleQuote1)
print('Single quotes inside single quotes enclosed within double quotes : ' + strSingleQuote2)
print('Double quotes inside double quotes escaped with a backslash : ' +
      strDblQuote1)
print('Double quotes inside Double quotes enclosed within single quotes : ' + strDblQuote2)

# enclose several strings in multiple lines in paranthesis
strMultiLine = ('This is a first line '
                'and the second line')
print(strMultiLine)

# Assignments can be done on more than one variable "simultaneously" on the same line like this
a, b, c = 1, 'testing', 2
print(a, b)

# Cannot mix operators between numbers and strings - the below will throw an error
# print(a+b+c)
