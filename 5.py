"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
import math


def is_divisible(num):
    # Maybe create a function that creates this list
    check_nums = [20, 19, 18, 17, 16, 14, 13, 11]
    fact_num = math.factorial(num)
    fact_range = num

    while fact_range != fact_num:
        if all(fact_range % check_num == 0 for check_num in check_nums):
            return fact_range

        fact_range += num

print is_divisible(20)
