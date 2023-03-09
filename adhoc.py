# The end keyword can be used to avoid the newline after the output, or end the output with a different string:

sentence = ['printed', 'with', 'a', 'dash', 'in', 'between']
for word in sentence:
    print(word, end='-')

# The sep keyword is used to specify how to separate the objects, if there is more than one:
print()
print('cats', 'dogs', 'mice', sep=',')

# The input() Function takes the input from the user and converts it into a string:

print('tell me your name?')
name = input()

print('What is your age?')   # ask for their age
age = input()

print('Hi, {}.'.format(name), 'You are {} years old'.format(age))


# input() can also be used to set a default message without using print():
name = input('Tell me your name? ')
age = input('What''s your age? ')

print('Hi, {}.'.format(name), 'You are {} years old'.format(age))
