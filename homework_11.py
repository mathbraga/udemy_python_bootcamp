# Create a generator that generates the squares of numbers up to some number N.
def gen_squares(n):
    for num in range(n):
        yield num**2

for x in gen_squares(10):
    print(x)

# Create a generator that yields "n" random numbers between a low and high number (that are inputs).
from random import randint

def rand_num(low, high, n):
    for i in range(n):
        yield randint(low, high)

for num in rand_num(1, 10, 12):
    print(num)

# Use the iter() function to convert the string below into an iterator:
s = 'hello'
s_iter = iter(s)
for c in s_iter:
    print(c)

# Explain a use case for a generator using a yield statement where you would not want to use a normal function with a return statement.
# R: In the case where you don't want to occupy memory space when generating a sequence, because you would have to create a list to store this sequence.

# Can you explain what gencomp is in the code below? (Note: We never covered this in lecture! You will have to do some Googling/Stack Overflowing!)

# my_list = [1,2,3,4,5]

# gencomp = (item for item in my_list if item > 3)

# for item in gencomp:
#     print(item)

# R: gencomp is the result from the for loop, which is filtering through the list and returning only integers greater than 3.