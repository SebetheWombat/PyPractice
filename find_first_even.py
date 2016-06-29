'''Function takes a list of integers and returns the first even number
raises an error if no evens occur'''

def first_even(listOints):
    try:
        for i in listOints:
            if i % 2 == 0 and i != 0:
                return i
        raise ValueError("No even numbers to find!")
    except ValueError as err:
        return err.args

print(first_even([1,2,3]))
print(first_even([2,4,6]))
print(first_even([1,3,5,7,4,2]))
print(first_even([0,1,3,5,7]))
            
