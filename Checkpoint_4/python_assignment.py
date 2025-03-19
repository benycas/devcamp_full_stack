# Exercise 1: Create a list, tuple, float, integer, decimal, and dictionary.
list_example = ['a', 'b', 'c', 'd']
tuple_example = ('a', 'b', 'c', 'd')
float_example = 1.23
int_example = 20

from decimal import Decimal
decimal_example = Decimal(1.23)
dict_example = {'name': 'Beñat', 'Last name': 'Iglesias','age': 32}

# Exercise 2: Round your float up.
float_rounded = round(float_example)
print(float_rounded)

# Exercise 3: Get the square root of your float.
import math
float_sqrt = math.sqrt(float_example)
print(float_sqrt)

# Exercise 4: Select the first element from your dictionary.
first_element = dict_example['name']
print(first_element)

# Exercise 5: Select the second element from your tuple.
second_element = tuple_example[1]
print(second_element)

# Exercise 6: Add an element to the end of your list.
list_example.append('e')
print(list_example)

# Exercise 7: Replace the first element in your list.
list_example[0] = 'aa'
print(list_example)

# Exercise 8: Sort your list alphabetically.
list_example.sort()
print(list_example)

# Exercise 9: Use reassignment to add an element to your tuple.
tuple_example = tuple_example + ('e',)
print(tuple_example)