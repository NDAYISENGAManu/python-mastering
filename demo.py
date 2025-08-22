# Coding challenge part 2.
# Create a list of your favourite food items, the list should have minimum 5 elements.
# List out the 3rd element in the list.
# Add additional item to the current list and display the list.
# Insert an element named tacos at the 3rd index position of the list and print out the list elements.
# For solution refer next lecture
# start now
food = ['eggs', 'pizza', 'cupcake', 'burger', 'salmon']
print(food[2])
food.append('cake')
print(food)
food.insert(3, 'tacos')
print(food)

# Dictionary advance operations
# Add product item to the dictionary through user input
products = {'phone':100, 'tablet':200, 'laptop':500}  # A dictionary with product names as keys andprices as values
# Print the initial dictionary
print("Initial Products Dictionary:", products)  # {'phone': 100, 'tablet': 200, 'laptop': 500}
# Adding a new product item through user input
product_name = input("Enter the product name: ")  # Taking product name as input from the user
product_price = float(input("Enter the product price: "))  # Taking product price as input from the user
# Adding the new product to the dictionary
products[product_name] = product_price  # Adding the new product with its price to the dictionary
# Print the updated dictionary
print("Updated Products Dictionary:", products)  # {'phone': 100, 'tablet': 200, 'laptop': 500, 'product_name': product_price}
# Remove product item from the dictionary through user input
product_to_remove = input("Enter the product name to remove: ")  # Taking product name to remove as input from the user
# Check if the product exists in the dictionary
if product_to_remove in products:  # Checking if the product exists in the dictionary
    del products[product_to_remove]  # Removing the product from the dictionary
    print(f"Product '{product_to_remove}' removed successfully.")  # Confirmation message
else:
    print(f"Product '{product_to_remove}' not found in the dictionary.")
# Print the final dictionary after removal
print("Final Products Dictionary:", products)  # {'phone': 100, 'tablet': 200, 'laptop': 500, 'product_name': product_price}

# change the price of a product item in the dictionary through user input
product_to_change = input("Enter the product name to change its price: ")  # Taking
# product name to change its price as input from the user
# Check if the product exists in the dictionary
if product_to_change in products:  # Checking if the product exists in the dictionary
    new_price = float(input(f"Enter the new price for '{product_to_change}': "))  # Taking new price as input from the user
    products[product_to_change] = new_price  # Updating the product price in the dictionary
    print(f"Price for '{product_to_change}' changed successfully to {new_price}.")  # Confirmation message
else:
    print(f"Product '{product_to_change}' not found in the dictionary.")
# Print the final dictionary after changing the price
print("Final Products Dictionary after price change:", products)  # {'phone': 100, 'tablet': 200, 'laptop': 500, 'product_name': product_price, 'product_to_change': new_price}


# Searching for Item in the List
# The 'in' operator checks if an item exists in a list and returns a boolean value
my_list = [1, 2, 3, 4, 5]  # A list of integers
# Print the list
print("List:", my_list)  # [1, 2, 3, 4, 5]
# Check if an item exists in the list
print(3 in my_list)  # True (3 exists in the list)
print(6 in my_list)  # False (6 does not exist in the list)
# Check if an item does not exist in the list
print(6 not in my_list)  # True (6 does not exist in the list)
print(3 not in my_list)  # False (3 exists in the list)
# use input to check if an item exists in the list
item = int(input("Enter a number to check if it exists in the list: "))
if item in my_list:
    print(f"{item} exists in the list")
else:
    print(f"{item} does not exist in the list")


# Data Structure = Set
# Sets are unordered collections of unique elements.
# They are defined using curly braces {} or the set() constructor.
my_set = {1, 2, 3, 4, 5}  # A set containing integers
# Print the set
print("Set:", my_set)  # {1, 2, 3, 4, 5}
# Accessing elements in a set (not by index, as sets are unordered)
number = set([1, 2, 3, 4, 5])  # Creating a set using the set() constructor
print("Set using constructor:", number)  # {1, 2, 3, 4, 5}
# Adding an element to the set
my_set.add(6)  # Adding the element 6 to the set
# Print the updated set
print("Updated Set:", my_set)  # {1, 2, 3, 4, 5, 6}
# Removing an element from the set
my_set.remove(3)  # Removing the element 3 from the set
# Print the set after removal
print("Set after removal:", my_set)  # {1, 2, 4, 5, 6}
# Checking membership in a set
print("Is 4 in the set?", 4 in my_set)  # True
print("Is 10 in the set?", 10 in my_set)  # False
# Set operations
set_a = {1, 2, 3}
set_b = {3, 4, 5}
# Union of two sets
set_union = set_a | set_b  # {1, 2, 3, 4, 5}
print("Union:", set_union)
# Intersection of two sets
set_intersection = set_a & set_b  # {3}
print("Intersection:", set_intersection)
# Difference of two sets
set_difference = set_a - set_b  # {1, 2}
print("Difference:", set_difference)
# empty set
empty_set = set()  # Creating an empty set
print("Empty Set:", empty_set)  # set()
# symetric difference
set_sym_diff = set_a ^ set_b  # {1, 2, 4, 5}
print("Symmetric Difference:", set_sym_diff)
# set clear
set_a.clear()  # Removing all elements from set_a
print("Set A after clear:", set_a)  # set()


# Data Structure = Get method
# The get() method is used to access the value associated with a key in a dictionary.
# If the key does not exist, it returns None or a specified default value.
my_dict = { "name": "John", "age": 30, "city": "New York" }  # A dictionary with string keys and mixed value types
# Print the dictionary
print("Dictionary:", my_dict)  # {'name': 'John', 'age': 30, 'city': 'New York'}
# Accessing elements in a dictionary using get method
print("Name:", my_dict.get("name"))  # John (accessing value by key)
print("Age:", my_dict.get("age"))  # 30 (accessing value by key)
# Accessing a non-existent key using get method
print("Country:", my_dict.get("country"))  # None (key does not exist)
# why do we use get method?
# The get method is useful because it allows us to safely access dictionary values without raising a KeyError if the key does not exist.
# It also allows us to specify a default value to return if the key is not found.

# Data Structure = update and pop method
# The update() method is used to add key-value pairs to a dictionary or update existing ones.
# The pop() method is used to remove a key-value pair from a dictionary and return the value associated with the key.
# Example of using update and pop methods
my_dict = { "name": "John", "age": 30, "city": "New York" }  # A dictionary with string keys and mixed value types
# Print the dictionary
print("Dictionary:", my_dict)  # {'name': 'John', 'age': 30, 'city': 'New York'}
# Updating the dictionary using update method
my_dict.update({"email": "ere@gmail.com", "country": "USA"})  # Adding new key-value pairs
# Print the updated dictionary
print("Updated Dictionary:", my_dict)  # {'name': 'John', 'age': 30, 'city': 'New York', 'email': 'ere@gmail.com', 'country': 'USA'}
# Removing a key-value pair using pop method
removed_value = my_dict.pop("age")  # Removing the key "age" and getting its value
# Print the removed value
print("Removed Value:", removed_value)  # 30 (value associated with the key "age")
# Print the dictionary after removing the key
print("Dictionary after pop:", my_dict)  # {'name': 'John', 'city': 'New York', 'email': 'ere@gmail.com', 'country': 'USA'}

prices = { "apple": 1.2, "banana": 0.5, "orange": 0.8 }  # A dictionary with fruit prices
newPrices = { "apple": 23,"grape": 2.0, "kiwi": 1.5 }  # A dictionary with new fruit prices
# Updating the prices dictionary with new prices
prices.update(newPrices)  # Merging newPrices into prices
# Print the updated prices dictionary
print("Updated Prices:", prices)  # {'apple': 23, 'banana': 0.5, 'orange': 0.8, 'grape': 2.0, 'kiwi': 1.5}
# keys and values functions
# The keys() method returns a view object that displays a list of all the keys in the dictionary.
print("Keys in Dictionary:", my_dict.keys())  # dict_keys(['name', 'city', 'email', 'country'])
# The values() method returns a view object that displays a list of all the values in the dictionary.
print("Values in Dictionary:", my_dict.values())  # dict_values(['John', 'New York', 'ere@gmail.com', 'USA'])
# The items() method returns a view object that displays a list of dictionary's key-value tuple pairs.
print("Items in Dictionary:", my_dict.items())  # dict_items([('name', 'John'), ('city', 'New York'), ('email', 'ere@gmail.com'), ('country', 'USA')])





# Data Structure = Dictionary
# Dictionaries are mutable, unordered collections of key-value pairs.
# They are defined using curly braces {}.
my_dict = { "name": "John", "age": 30, "city": "New York" }  # A dictionary with string keys and mixed value types
# Print the dictionary
print("Dictionary:", my_dict)  # {'name': 'John', 'age': 30, 'city': 'New York'}
# Accessing elements in a dictionary
print("Name:", my_dict["name"])  # John (accessing value by key)
print("Age:", my_dict["age"])  # 30 (accessing value by key)
# Adding a new key-value pair
my_dict["email"] = " data@email.com "  # Adding a new key-value pair
# Print the updated dictionary
print("Updated Dictionary:", my_dict)  # {'name': 'John', 'age': 30, 'city': 'New York', 'email': 'data@email.com'}

# creating dictionary using dict() constructor
my_dict2 = dict(name="Alice", age=25, city="Los Angeles")  # Creating a dictionary using the dict() constructor
# Print the new dictionary
print("New Dictionary:", my_dict2)  # {'name': 'Alice', 'age': 25, 'city': 'Los Angeles'}
# modifying a value in the dictionary
my_dict2["age"] = 26  # Modifying the value associated with the key "age"
# Print the modified dictionary
print("Modified Dictionary:", my_dict2)  # {'name': 'Alice', 'age': 26, 'city': 'Los Angeles'}
my_dict2["country"] = "USA"  # Adding a new key-value pair
# Print the dictionary with the new key-value pair
print("Dictionary with new key-value pair:", my_dict2)  # {'name': 'Alice', 'age': 26, 'city': 'Los Angeles', 'country': 'USA'}
# deleting a key-value pair
del my_dict2["city"]  # Deleting the key "city" and its associated value
# Print the dictionary after deletion
print("Dictionary after deletion:", my_dict2)  # {'name': 'Alice', 'age': 26, 'country': 'USA'}



# Data Structure = Tuple
# Tuples are immutable sequences, typically used to store collections of heterogeneous data.
# They are defined using parentheses ().
# Example of a tuple
my_tuple = (1, 2, 3, "hello", 4.5)  # A tuple containing integers, a string, and a float
# Print the tuple
print("Tuple:", my_tuple)  # (1, 2, 3, 'hello', 4.5)
# Accessing elements in a tuple
print("First element:", my_tuple[0])  # 1 (first element)
print("Last element:", my_tuple[-1])  # 4.5 (last element)
# Slicing a tuple
print("Slice from index 1 to 3:", my_tuple[1:4])  # (2, 3, 'hello')
# Tuples are immutable, meaning we cannot change their elements
# my_tuple[0] = 10  # This will raise a TypeError

# Data Structure = addition and multiplication
a = [1, 2, 3, 4, 5]  # List of integers
b = [6, 7, 8, 9, 10]  # Another list of integers
# Adding two lists
c = a + b  # Concatenates the two lists
# Multiplying a list by an integer
d = a * 2  # Repeats the list twice
# Print the results
print("List a:", a)  # [1, 2, 3, 4, 5]
print("List b:", b)  # [6, 7, 8, 9, 10]
print("List c (a + b):", c)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("List d (a * 2):", d)  # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
# nested list
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # A list containing other lists
# Print the nested list
print("Nested List:", nested_list)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# index position of nested list
print("Element at nested_list[0][1]:", nested_list[0][1])  # 2 (second element of the first list)
# Mutability of lists
# Lists are mutable, meaning we can change their elements
nested_list[0][1] = 20  # Changing the second element of the first list
# Print the modified nested list
print("Modified Nested List:", nested_list)  # [[1, 20, 3], [4, 5, 6], [7, 8, 9]]

# Data Structure = list slicing
people = ["manu", "sachin", "suresh", "ramesh", "mahesh"]

# List functions
# Append an element to the list
people.append("john")
# Insert an element at a specific position
people.insert(2, "peter")  # Insert "peter" at index 2
# Remove an element from the list
people.remove("suresh")  # Remove "suresh" from the list
# Pop an element from the list (removes and returns the last element)
last_person = people.pop()  # Removes and returns the last element
# Sort the list in alphabetical order
people.sort()  # Sorts the list in place
# Reverse the list
people.reverse()  # Reverses the order of the list
# Print the modified list
print(people)  # ['ramesh', 'peter', 'mahesh', 'manu', 'john']
# Length of the list
print(len(people))  # 5
# Index of an element in the list
print(people.index("manu"))  # 3
# Count occurrences of an element in the list
print(people.count("manu"))  # 1
# Copy the list
people_copy = people.copy()  # Creates a shallow copy of the list
print(people_copy)  # ['ramesh', 'peter', 'mahesh', 'manu', 'john']
# Clear the list
people.clear()  # Removes all elements from the list
# Print the cleared list
print(people)  # []
# Reinitialize the list
people = ["manu", "sachin", "suresh", "ramesh", "mahesh"]
# Print the original list
print(people)  # ['manu', 'sachin', 'suresh', 'ramesh', 'mahesh']
# extend the list with another list
people.extend(["john", "peter"])  # Adds "john" and "peter" to the end of the list
# max and min functions
print(max(people))  # 'suresh' (alphabetically last)
print(min(people))  # 'john' (alphabetically first)
# mutability of lists
# Lists are mutable, meaning we can change their elements
people[0] = "john"  # Change the first element to "john"
# Print the modified list
print(people)  # ['john', 'sachin', 'suresh', 'ramesh', 'mahesh', 'john', 'peter']
# List comprehension
# Create a new list with the lengths of each name in the people list
name_lengths = [len(name) for name in people]  # List comprehension to get lengths of names
# Print the list of name lengths
print(name_lengths)  # [4, 6, 6, 6, 6, 4, 5]



# In & Not In operators
# Check if an element is in the list
print("manu" in people)  # True
print("john" in people)  # False
# Check if an element is not in the list
print("john" not in people)  # True

# print the list
print(people[1:3])  # ['manu', 'sachin', 'suresh']
# print the first three elements
print(people[:3])  # ['manu', 'sachin', 'suresh']
# print the last three elements
print(people[-3:])  # ['suresh', 'ramesh', 'mahesh']
# print the last two elements
print(people[-2:])  # ['ramesh', 'mahesh']
# print the first two elements
print(people[-5:-2]) # ['manu', 'sachin', 'suresh']

# Data Structure = list

people = ["manu", "sachin", "suresh", "ramesh", "mahesh"]
# print the list
print(people)
# print the first element
print(people[0])  # manu
# print the last element
print(people[-1])  # mahesh

# BMI calculator or Body Mass Index calculator
# BMI = weight in kg / (height in m * height)

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in m: "))
bmi = weight / (height * height) # or bmi = weight / height ** 2
print("Your BMI is: ", bmi)
print(f"Your BMI is: {bmi}")
print("Your BMI is: " + str(bmi))



# interest calculator
# SI = P * N * R / 100

principal = int(input("Enter the amount bollowed : "))
years = float(input("Enter the period in years: "))
rate = float(input("Enter the rate of interest: "))

interest = (principal * years * rate) / 100
print("The interest is: ", interest)
print("the principal is: "+ str(principal) + " and the interest is: " + str(interest))
print(f"the principal is: {principal} and the interest is: {interest}")




print("hello world")
# print("hello world")
print("manu is here")
''' multi line 
    comments
 '''
a = int(input("Enter a first number: ")) # get the input as integer
b = input("Enter a second number: ")  #wherever we get the input from user, it is always string

print(type(a))
print(type(b))

b = int(b) # converting string to int

c = a + b
print(c)
print(a+b)

# simple login
firstname = input("Enter your first name: ")
lastname = input("Enter your last name: ")

username = firstname + lastname
email  = username + "@gmail.com"
print("Your username is: " + username)
print("Your email is: " + email)
print(email)

# comparing strings

saved_password = "manu123"
password = input("Enter your password: ")
if password == saved_password:
    print("Login successful")
else:
    print("Login failed, please try again")

print(saved_password == password)


# Variable naming rules in Python
radius = 10   # Allowed
ra20dius= 20   # Allowed
# 10radius = 30 # Not allowed
# 1radius=20   # Not allowed
_radius=10  # Allowed
circle_radius = 10 # Allowed