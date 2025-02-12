"""Write a function that takes in a list of integers and returns True if it contains in order007
def spy_game(nums):
    pass

spy_game([1,2,4,0,0,7,5]) --> True
spy_game([1,0,2,4,0,5,7]) --> True
spy_game([1,7,2,0,4,5,0]) --> False"""


def spy_game(nums):
    sequence = [0, 0, 7]
    index = 0

    for num in nums:
        if num == sequence[index]:
            index += 1
        if index == len(sequence):
            return True

    return False

nums = list(map(int, input("Enter a numbers:").split()))
print(spy_game(nums))
# [1,2,4,0,0,7,5] >>> True
