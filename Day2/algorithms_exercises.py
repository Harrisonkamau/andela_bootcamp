# 1. Array reverse
# Write a function reverse(A) that reverses a list A, of integers
def reverse_list(my_list):
    my_list = list(my_list)
    reverse = my_list[::-1]
    print reverse
reverse_list([1,2,3,4,True])


# 2. Equilibrium
def find_missing_element(my_lst):
 # Put the list in a set, find smallest and largest items
    initial_set = set(my_lst)
    minimum_element = min(initial_set)
    maximum_element =max(initial_set)
     # Create a super set of all items from minimum to maximum
    super_set = set(xrange(minimum_element, maximum_element + 1))

#Missing ielements are the ones that are in the super_set, but not in the initial_set
    return sorted(super_set - initial_set)

print find_missing_element([1, 2, 5, 6, 7, 10])
# 3. num_to_words
# Function that converts numbers to words
numbers = {'1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five','6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'}


def num_to_word(number):
    num = str(number)
    num_string = ''
    for item in num:
        num_string += numbers[item] + " "
    return num_string
print num_to_word(438483478)

# 4. factorial function
def factorial(n):
    if n < 1:
        return "This is negative number!"
    elif n == 1:
        return 1
    return factorial(n-1) * n

print factorial(5)
print factorial(-5)

# 5. Sum of Digits
def digit_sum(my_num):
    my_num = str(my_num)
    my_sum = 0
    for item in my_num:
        my_sum += int(item)
    return my_sum
print digit_sum(1234)


# 6. Sum of Unique Digits
def sum_of_unique_digits(A):
    def get_digits(number):
        digits = []
        while (number > 0):
            digits.append(number % 10)
            number = number / 10
        return digits
    used = []
    sum = 0
    for number in A:
        digits_in_number = get_digits(number)
        for digit in digits_in_number:
            if digit not in used:
                sum += digit
                used.append(digit)
    return sum

print sum_of_unique_digits([10, 20, 3, 5, 6, 23])
