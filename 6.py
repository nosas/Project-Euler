"""
The sum of the squares of the first ten natural numbers is, 1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is, (1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square
of the sum is 3025 - 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and square of the sum.
"""


# Create a num_range from 1 -> max_num
# Create a list with each number in num_range squared
# Return the sum of the list of squared numbers
def sum_of_squares(max_num):
    num_range = range(1, max_num + 1)
    squares_list = [num**2 for num in num_range]
    return sum(squares_list)


# Create a num_range from 1 -> max_num
# Sum all the numbers in the range
# Return the sum squared
def square_of_sum(max_num):
    num_range = range(1, max_num + 1)
    sum_num = sum(num_range)
    return sum_num**2


natural_num = 100
sum_10 = sum_of_squares(natural_num)
square_10 = square_of_sum(natural_num)
diff_10 = square_10 - sum_10

print square_10, "-", sum_10, "=", diff_10
