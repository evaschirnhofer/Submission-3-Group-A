"""
Upper and Lower
"""
# Provide your solution here
def count_upper_lower(my_string: str):
    return my_string.isupper()
    return my_string.islower()


"""
Check 33
"""
# Provide your solution here

def has_33(my_list):
    if 33 in my_list:
        return True
    else:
        return False

result = has_33([1, 3, 4])
print(result)

result2 = has_33([3, 4, 5])
print(result2)

result3 = has_33([5, 6, 33])
print(result3)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Test your functions by calling them here. Use different parameter values to test them with different scenarios.")

has_33([1, 3, 4])
has_33([3, 4, 5])
has_33([5, 6, 33])