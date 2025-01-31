import random

# we define the range of numbers
data = list(range(1, 101))

# then generate a list of 20 random numbers from the range
random_numbers = random.sample(data, 20)

# count even numbers
even_count = sum(1 for num in random_numbers if num % 2 == 0)

# print results
print("Generated numbers:", random_numbers)
print("Number of even numbers:", even_count)