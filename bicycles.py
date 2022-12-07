bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])
print(bicycles[0].title())
# Ask for bicycles at index 1 and 3

print(bicycles[0])
print(bicycles[3])

# Syntax for accessing last element in a list

print(bicycles[-1])

# Using individual values from a list with f strings

message = f"My first bicycle was a {bicycles[1].title()}"
print(message)