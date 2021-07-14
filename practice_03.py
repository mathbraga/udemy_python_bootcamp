# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, 
# but returns the greater if one or both numbers are odd
def lesser_of_two_evens(a,b):
    if a%2 == 0 and b%2 == 0:
        if a < b:
            return a
        else:
            return b
    else:
        if a > b:
            return a
        else:
            return b
print(lesser_of_two_evens(2,4))
print(lesser_of_two_evens(2,5))

# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
def animal_crackers(mystring):
    first, second = mystring.split()
    
    if first[0].lower() == second[0].lower():
        return True
    else:
        return False
print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy Kangaroo'))

# MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
def makes_twenty(n1,n2):
    if n1+n2 == 20 or n1 == 20 or n2 == 20:
        return True
    else:
        return False
print(makes_twenty(20,10))
print(makes_twenty(2,3))

# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
def old_macdonald(name):
    res = ""
    for index, letter in enumerate(name):
        if index == 0 or index == 3:
            res = res + letter.upper()
        else:
            res = res + letter
    return res
print(old_macdonald('macdonald'))

# MASTER YODA: Given a sentence, return a sentence with the words reversed
def master_yoda(text):
    words = text.split()
    reversed_words = words[::-1]
    reversed_phrase = " ".join(reversed_words)
    return reversed_phrase
print(master_yoda('I am home'))
print(master_yoda('We are ready'))

# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
def almost_there(n):
    if abs(n-100) <= 10 or abs(n-200) <= 10:
        return True
    else:
        return False
print(almost_there(104))
print(almost_there(150))
print(almost_there(209))

# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
def has_33(nums):
    index = 0
    while index < len(nums)-1:
        if nums[index] == 3:
            if nums[index+1] == 3:
                return True
        index += 1
    return False
print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))

# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
def paper_doll(text):
    res = ""
    for char in text:
        res = res + char*3
    return res
print(paper_doll('Hello'))
print(paper_doll('Mississippi'))

# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum.
# If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, 
# if the sum (even after adjustment) exceeds 21, return 'BUST'
def blackjack(a,b,c):
    acc = a+b+c
    if acc <= 21:
        return acc
    elif 11 in [a,b,c]:
        return acc-10
    else:
        return "BUST"
print(blackjack(5,6,7))
print(blackjack(9,9,9))
print(blackjack(9,9,11))

# SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending
# to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
def summer_69(arr):
    index = 0
    res = 0
    while index < len(arr):
        if arr[index] == 6:
            index = arr.index(9)
            if index == len(arr)-1:
                return res
            else:
                index += 1
                res = res + arr[index]
        else:
            res = res + arr[index]
        index += 1
    return res
print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]))

# SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
def spy_game(nums):
    test = []
    for i in nums:
        if i == 0 or i ==7:
            test.append(i)
        if test == [0,0,7]:
            return True
    return False
print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))

# COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number
def count_primes(num):
    count = num-1
    for i in range(2, num+1):
        for j in range(2, i):
            if i%j == 0:
                count -= 1
                break
    return count
print(count_primes(100))

# PRINT BIG: Write a function that takes in a single letter, and returns a 5x5 representation of that letter
def print_big(letter):
    ref = {1: "  *  ", 2: " * * ", 3: "*   *",\
        4: "*****", 5: "*    ", 6: "**** "}
    patterns = {'A': [1, 2, 4, 3, 3], 'B': [6, 3, 6, 3, 6], 'C': [4, 5, 5, 5, 4],\
        'D': [6, 3, 3, 3, 6], 'E': [4, 5, 4, 5, 4]}
    for pattern in patterns[letter.upper()]:
        print(ref[pattern])
print_big('a')