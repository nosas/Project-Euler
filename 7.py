"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""
import math


def is_prime(n):
    for number in range(3, int(math.sqrt(n)) + 1, 2):
        if n % number == 0:
            return False
    return True


# Prime count starts at 6 because it was given to us in the problem description.
prime_count = 6
curr_num = 13

while prime_count <= 10001:
    if is_prime(curr_num):
        print curr_num, "is a prime #", prime_count
        prime_count += 1
    curr_num += 2

print
print "Prime count:", prime_count
