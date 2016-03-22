'''
Define a function called data_type, to take one argument. Compare and return results, based on the argument supplied to the function.
Complete the test to produce the perfect function that accounts for all expectations.

For strings, return its length.
For None return string 'no value'
For booleans return the boolean
For integers return a string showing how it compares to hundred e.g.
For 67 return 'less than 100' for 4034 return 'more than 100' or equal to 100 as the case may be
For lists return the 3rd item, or None if it doesn't exist
'''



# solutions
def data_type(data):
    if type(data) == str:
        return len(data)
    elif type(data) == bool:
        return data
    elif type(data) == int:
        if data < 100:
            return 'less than 100'
        elif data == 100:
            return 'equal to 100'
        else:
            return 'more than 100'

    elif type(data) == list:
        if len(data) > 4:
            return data[3]
        else:
            return None
