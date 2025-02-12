"""You are given list of numbers separated by spaces.
Write a function filter_prime which will take list of numbers as an agrument
and returns only prime numbers from the list"""
def filter_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    return [n for n in numbers if is_prime(n)]
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("Prime numbers:", filter_prime(numbers))
#3 4 5 6 >>> Prime numbers: [3, 5]
