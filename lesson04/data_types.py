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

# String Methods: Methods are functions called on the string class
print(fullName)
print(fullName.lower());
print(fullName.upper());
print(fullName);

print(multiline.title()) # capitalizes the statement
print(multiline.replace("Hey,", "Yo!"))
print(multiline)