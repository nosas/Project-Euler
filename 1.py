# Create a list for every number ranging from 1,1000
# that's a multiple of either 3 or 5. This solution uses
# list comprehension: https://docs.python.org/2/tutorial/datastructures.html#list-comprehensions
result = [num for num in range(1000) if num % 3 == 0 or num % 5 == 0]

sum = 0
for num in result:
    sum += num

print sum, result
