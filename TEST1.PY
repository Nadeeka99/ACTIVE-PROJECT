# Initialize the variable to store the sum
sum = 0

# Iterate over all the numbers between 1 and 200
for i in range(1, 201):
  # If the number is even, add it to the sum
  if i % 2 == 0:
    sum += i

# Print the sum
print(sum)
