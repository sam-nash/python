# Lists are similar to arrays and can contain as many number of variables of any datatype
list = []
list.append(1)
list.append('Hello')
list.append(1.0)
print(list)
print('The list is : ', list)

list.append("World")
# although its not a string the string formatter %s can be used to format a list as a string.
print('My new List is : %s' % list)

# loop through and print each in a newline
for i in list:
    print(i)

# access list items with index - index starts at 0
print('The item at index 0 is ', list[0])

# can use , or + operator to concatenate the message and the value as they are both strings
print('The item at index 1 is ' + list[1])

# cannot use + operator to concatenate message which is a string an integer value - the below will throw an error
# print('This will fail if you concatenate a string and int ' + list[0])

# cannot access items that do not exist at an index - the below will throw an error
# print(list[3])

# get the length of a list
print('Length of the list is : ', len(list))
