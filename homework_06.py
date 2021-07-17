# Problem 1
# Handle the exception thrown by the code below by using try and except blocks.
try:
    for i in ['a','b','c']:
        print(i**2)
except:
    print("Unsupported types for mathematical operation!")

# Problem 2
# Handle the exception thrown by the code below by using try and except blocks. Then use a finally block to print 'All Done.'
x = 5
y = 0

try:
    z = x/y
except:
    print("Can't divide by zero.")
finally:
    print("All done.")

# Problem 3
# Write a function that asks for an integer and prints the square of it. Use a while loop with a try, except, else block to account for incorrect inputs.
def ask():
    while True:
        try:
            result = int(input("Enter an integer: "))
        except:
            print("Something wen't wrong. Try again.")
        else:
            print(f"The result is: {result**2}")
            break
ask()