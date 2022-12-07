motorcycles = ['honda', 'yamaha', 'suzuki']

print(motorcycles)

# Modifying elements in a list 
motorcycles[0] = 'ducati'

print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']


# Adding element to a list
#Appending Element to the end of a list
motorcycles.append('ducati')

print(motorcycles)

# Using an empty list, let's add elements to it.

motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)

# Inserting elements into a list

motorcycles = ['honda', 'yamaha', 'suzuki']

motorcycles.insert(0, 'ducati')

print(motorcycles)

# Removing elements from a list using del statement

motorcycles = ['honda', 'yamaha', 'suzuki']

print(f"\n{motorcycles}")

del motorcycles[0]

print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']

del motorcycles[1]

print(motorcycles)

# Removing an item using the pop() method

motorcycles = ['honda', 'yamaha', 'suzuki']
print(f"\n{motorcycles}")

popped_motorcycles = motorcycles.pop()
print(f"{motorcycles}")
print(popped_motorcycles)

# Pop method usefulness, case of showing last motorcycle last bought

motorcycles = ['honda', 'yamaha', 'suzuki']

last_owned = motorcycles.pop()
print(f"\nThe last motorcycle I owned was a {last_owned.title()}")

# Popping items from any position in a list 
motorcycles = ['honda', 'yamaha', 'suzuki']

first_owned = motorcycles.pop(0)
print(f"\n The first motorcycle I owned was a {first_owned.title()}.")

# Removing an item by value, used if you only know the value of the item you want to remove.

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(f"\n{motorcycles}")

motorcycles.remove('ducati')
print(motorcycles)

# You can also use the remove() method to work with a value that's beong removed from a list.

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too too_expensive for me.")