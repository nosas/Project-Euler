"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""


# Check if a number is a palindrome by turning the number into a string
# and returning whether the num_string is equal to reversed_num_string
def is_palindrome(number):
    num_str = str(number)
    reverse_num_str = num_str[::-1]
    return num_str == reverse_num_str


def find_biggest_palindrome(max_range=999, min_range=99):
    # Decreasing range from [999, 99)
    # Alternatively: reversed(range(min_range, max_range))
    three_digit_range = range(max_range, min_range, -1)
    pali = (0, 0, 0)
    for first_num in three_digit_range:
        for second_num in three_digit_range:
            # Eliminate duplicates
            if second_num <= first_num:
                product = first_num * second_num
                # print first_num, second_num, product
                if is_palindrome(product) and product > pali[2]:
                    pali = first_num, second_num, product
    return pali

biggest_pali = find_biggest_palindrome()
print "%d x %d = %d" % (biggest_pali[0], biggest_pali[1], biggest_pali[2])
