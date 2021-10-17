

cal_lookup = {'apple': 95, 'banana': 105, 'orange': 45, 'strawberry': 12}

cal_lookup['banana']

my_fruit_list = ['orange', 'apple', 'strawberry']

for f in my_fruit_list:
    print(f)

for f in my_fruit_list:
    pass
print(f)

def sq_int(x):
    y = x**2
    return y

sq_int(5)
sq_int(11)

## Excercises 

# Write a loop that uses while instead of the built-in looping structure

    

# Write a loop that loop over the keys in a dictionary and prints the values

for key in cal_lookup.keys():
    print(cal_lookup[key])


# Write the functions is_odd and is_even that are shown in the lecture

def is_even(x):

    if (x % 2) == 0:
        return True
    else:
        return False
    
def is_odd(x):

    if (x % 2) != 0:
        return True
    else:
        return False


def describe_evenness(x):

    if is_even(x):
        print("It's even")
    
    elif is_odd(x):
        print("It's odd!")
    else:
        print("It's neither even or odd!")

describe_evenness()

# Loop over my_first_list and square the value if the value is a number, 
# and print the calories of the fruit if it’s a fruit (hint: use the dictionary to look up the calories)

my_first_list = [2, 'apple', 4, 'orange', 'strawberry']
my_first_list

for f in my_first_list:
    if type(f) is int:
        print(f*2)
    else:
        print(cal_lookup[f])

# # - Write a function that:
#     - Takes a dictionary as an argument
#     - Loops over the keys in the dictionary
#     - Prints the square of the value in the value
#     - Hint: use the `cal_lookup` dictionary for testing.

def last_func(f):
    for key in f.keys():
        print(f[key]**2)

last_func(cal_lookup) # Works well!   
