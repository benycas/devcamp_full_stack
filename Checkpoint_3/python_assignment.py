# Exercise 1: Create a string, number, list, and boolean, each stored in their own variable.
str_example = "Cogito ergo sum"
num_example = 30
list_example = ['a', 'b', 'c', 'd']
boolean_example = True

# Exercise 2: Use an index to grab the first 3 letters in your string, store that in a variable.
str_letters = str_example[:3]

# Exercise 3: Use an index to grab the first element from your list.
first_element_list = list_example[0]

# Exercise 4: Create a new number variable that adds 10 to your original number.
new_number = num_example + 10

# Exercise 5: Use an index to get the last element in your list.
last_element_list = list_example[-1]

# Exercise 6: Use split to transform the following string into a list.
names = 'harry,alex,susie,jared,gail,conner'
names_list = names.split(',')

# Exercise 7: Get the first word from your string using indexes. Use the upper function to transform the letters into uppercase. Create a new string that takes the uppercase word and the rest of the original string.
first_word = str_example.split()[0].upper()
new_str = first_word + str_example[6:]

# Exercise 8: Use string interpolation to print out a sentence that contains your number variable.
print(f"I am {num_example} years old.")

# Exercise 9: Print “hello world”.
print('hello world')
