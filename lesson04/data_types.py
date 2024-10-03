import math
# Naming conventions in python

# literal assignments
firstName = "Yann";
lastName = "Kamche";

# print(type(firstName));
# print(type(firstName) == str);
# print(isinstance(firstName, str));

# constructor function
# fullName = firstName + " " + lastName;
# # print(fullName);
# fullName = str("Kamche Yann Arnaud");
# print(type(fullName));
# print(type(fullName) == str);
# print(isinstance(fullName, str));

# concatenation
fullName = firstName + " " + lastName;
print(fullName);

fullName += "!"
print(fullName)

# Casting a number to a string
decade = str(2000);
print(type(decade));
print(decade);

statement = "I was born in the " + decade + "s."
print(statement);

# Multiple lines
multiline = '''
Hey, how are you?                                             

I was just checking in.            
                            All good?
'''
print(multiline)

# Escaping special characters
sentence = "I'm back at work!\tHey!\n\nWhere's this at\\located?"
print(sentence)

# # String Methods: Methods are functions called on the string class
# print(fullName)
# print(fullName.lower());
# print(fullName.upper());
# print(fullName);

# print(multiline.title()) # capitalizes the statement
# print(multiline.replace("Hey,", "Yo!"))
# print(multiline)

# print(len(multiline))
# multiline += "                        " # Add some spacing after multiline
# print(multiline)
# multiline = "        " + multiline
# print(len(multiline))
# print(multiline)
print(len(multiline))
print(multiline)
multiline += "                        " # Add some spacing after multiline
print(len(multiline))

print(len(multiline.rstrip()))

print("\n\n\n");

# Build a menu
title = "menu".upper()
print(title.center(20, "="))


print("\n")
print("Fufu and Eru".ljust(16, ".") + "$1".rjust(10))
print("Fried Rice".ljust(16, ".") + "$1".rjust(10))

# string index values
print(firstName[1:])

# Some methods reutrn boolean data
print(firstName.startswith("Y"))
print(lastName.endswith("Z")); 

# Boolean data type
# myValue = True
# x = bool(False)
# print(type(x) == bool)
# print(x)
# print(isinstance(myValue, bool))
# print(myValue)

# Numeric data types

# integer type
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

# float type
gpa = 3.28
y = float(1.1)
print(type(gpa))

# complex type
comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# Built-in functions for number

print(abs(gpa))
print(round(gpa * -1))
print(round(gpa))

print(round(gpa, 1))

print(math.pi)
print(round(math.pi, 4)) #1:20:03

print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

# casting a string to a number
string = "237"
number = int(string)
print(type(number))
print(isinstance(number, int))

# Erro if you attempt to cast incorrect data
zip_value = int("New York");
print(zip_value)
