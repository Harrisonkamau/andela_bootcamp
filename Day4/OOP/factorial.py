
# Factorial using a while loop
def factorial (n):
	if (n <= 1):
		return 1

	i = 1
	product = 1
	while (i <= n):
		product = product * i
		i = i + 1

	return product

print factorial(5)
# Using a For loop

def factorial(n):
    product = 1

    for i in range(1, int(n)+1):
        product *= i
    return product

print factorial(4)

# using recursion
def factorial(n):
    if n <= 1:
        return 1
    return factorial(n - 1) * n

print factorial(3) 
