"""
By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms.
"""

fib = [0, 1]
max_value = 4000000

# Could have made a recursive function, however this works fine.
# While the last number in the fibonacci sequence is less than max_value
# Appends the next_num in the sequence by adding the 2 previous numbers
while fib[-1] <= max_value:
    i = len(fib)

    next_num = fib[i-1] + fib[i-2]
    if next_num > max_value:
        break

    fib.append(next_num)

even_fib = [even_num for even_num in fib if even_num % 2 == 0]
print sum(even_fib)
