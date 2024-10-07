users = ['Dave', 'John', 'Sara']

data = ['Yann', 42, True]

emptyList = [] 

print("Dave" in users)
print("Yann" in data)
print("Dave" in emptyList)

print(users[0])
print(data[0])
print(data[-3])

print(users.index('Sara'))
print(users[0: 2])
print(users[1: ])
print(users[-3:-1])

print(len(data))

users.append("Elsa")
print(users)

users += data
print(users)

data.extend(["I", "Love","My_Country"])
print(data)

# users.extend(data)
# print(users)

data.insert(0, 'Bob')
print(data)

data[2:3] = ['Eddie', 'Alex']
print(data)

data.remove("Yann")
print(data)

print(data.pop())

del users[0]
print(users[0])

# del data
data.clear()
print(data)

# users.sort()
print(users)

users[4:] = []
print(users)

users[4:] = ["yann"]
users.sort()
print(users)

users.sort(key=str.lower)
print(users)

nums = [4, 42, 78, 1, 5]
nums.reverse()
print(nums)

# nums.sort(reverse=True)
# print(nums)

print(sorted(nums, reverse=True))
print(nums)

# ways to make a copy
numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

mycopy.sort()

print(numscopy, mynums, mycopy)

print(type(nums))

mylist = list([1, "Neil", True])
print(mylist)

# Tuples

mytuple = tuple(('Dave', 42, True))
anothertuple = (1, 4, 2, 8, 2)

print(mytuple, anothertuple)
print(type(mytuple), type(anothertuple))

newlist = list(mytuple)
newlist.append('Neil')

newtuple = tuple(newlist)
print(newtuple)

# unpacking a tuple
(one, *two, hey) = anothertuple
print(one, two, hey)

print(anothertuple.count(2))
