"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""
import math

big_num = 600851475143
# To find the prime factors of a number, range from 2 -> sqrt(num) + 1
sqrt_big_num = int(math.sqrt(big_num)) + 1
# Even numbers can't be prime, except for 2, so eliminate all
# the even numbers to make finding primes faster.
odd_num = [num for num in range(3, sqrt_big_num, 2)]
prime_nums = [2]


# To find if a number is prime, create a range of numbers from 3 -> sqrt(num) + 1
# If any of the numbers in that range evenly divide into n, then n is not prime.
def is_prime(n):
    for number in range(3, int(math.sqrt(n)) + 1, 2):
        if n % number == 0:
            return False
    return True


# Find all the prime numbers in the range given from the given big_num
# and append the numbers to prime_nums
for num in odd_num:
    if is_prime(num):
        prime_nums.append(num)


# Find the prime factors of any given numbers. The index variable is used
# to navigate through the prime_nums list. While the given number isn't 1,
# check if the current_number at prime_num[index] divides evenly into the given number.
# If it does, while the current_number still divides evenly into the given number, append
# current_number onto the list of factors, and divide given number by current number.
# If the number doesn't divide evenly, increase the index number and repeat for each
# number in the primes list OR until the given number is equal to 1.
def prime_factors(n):
    index = 0
    factors = []

    while n != 1 and index < len(prime_nums):
        cur_num = prime_nums[index]
        while n % cur_num == 0:
            factors.append(cur_num)
            n /= cur_num
        else:
            index += 1
    return factors

print "Prime factors of %d are %s" % (big_num, str(prime_factors(big_num))[1:-1])
print "Largest Prime Factor: %d " % max(prime_factors(big_num))
