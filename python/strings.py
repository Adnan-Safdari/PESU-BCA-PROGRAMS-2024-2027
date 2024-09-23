# - - - - - - - - - - - - - DEFINING STRINGS - - - - - - - - - - - - -
my_string1 = 'hello'
print(my_string1)  # Output: "hello"

my_string2 = "hello"
print(my_string2)  # Output: hello

my_string3 = '''Hello'''
print(my_string3)  # Output: Hello

my_string4 = """Hello"""
print(my_string4)  # Output: Hello

my_str = 'programming'
print('my_str=', my_str)  # Output: mystr= programming

# - - - - - - - - - - - - - SLICING STRINGS - - - - - - - - - - - - -

print('my_str[0]=', my_str[0])  # Output: my_str[0]= p
print('my_str[-1]=', my_str[-1])  # Output: my_str[-1]= g
print('my_str[1:5]=', my_str[1:5])  # Output: my_str[1:5]= rogr
print('my_str[5:-2]=', my_str[5:-2])  # Output: my_str[5:-2]= ammi

print(my_str[:2])  # output: pr
print(my_str[::2])  # output: pormig
# reverses the string
print(my_str[::-1])  # output:gnimmargorp

# - - - - - - - - - - - - - DELETING STRINGS - - - - - - - - - - - - -

temp_string = "Chalke Chalke"
print(temp_string)

del temp_string  # deleting the string
try:
    print(temp_string)  # Output: Chalke Chalke
except NameError:  # Handling the error as the string is deleted
    print("The var 'temp_string' does not exist")

# - - - - - - - - - - - - - HANDLING STRINGS WITH DIGITS - - - - - - - - - - - - -

string_filter_digits = "Hello 321 World 123"

# Checking if all characters are a digit
result_digits_check = all(char.isdigit() for char in string_filter_digits)
print(result_digits_check)  # Output: False

# Checking if any are digits
result_digits_check = any(char.isdigit() for char in string_filter_digits)
print(result_digits_check)  # Output: True

# - - - - - - - - - - - - - IN BUILT FUNCTIONS FOR STRINGS - - - - - - - - - - - - -

myVarForMaxMin = "HelloWorld89"

# Maximum
print(f"Max: {max(myVarForMaxMin)}")  # Output: Max:r

# Minimum
print(f"Min: {min(myVarForMaxMin)}")  # Output: Min:r

# Type
print(f"Type: {type(myVarForMaxMin)}")  # Output:  <class 'str'>

# Length
print(f"Length: {len(myVarForMaxMin)}")  # Output: Length: 12

# ID
print(f"ID: {id(myVarForMaxMin)}")  # Output: ID:  2733265750064


# as_integer_ratio()
myFloatingNumber = float("5.5")  # Converting string to float
print(f"Ratio: {myFloatingNumber.as_integer_ratio()}")  # Output: (11.2)
# Checking the type
print(f"Ratio: {type(myFloatingNumber.as_integer_ratio())}")  # Output: Tuple

# bit_length()
bit_check_number = 15
print(f"Bit Length: {bit_check_number.bit_length()}")  # Output: 4
