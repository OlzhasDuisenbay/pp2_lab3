"""Define a functino that takes a list of integers and prints a histogram to the screen. For example, should print the following:histogram()histogram([4, 9, 7])

****
*********
*******"""
def histogram(numbers):
    for num in numbers:
        print('*' * num)

user_input = input("Enter a list of integers separated by spaces: ")
numbers = [int(num) for num in user_input.split()]

histogram(numbers)
""" 1 2 3 4 5 >>>
*
**
***
****
*****
"""
