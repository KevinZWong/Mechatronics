# Lab Example #1 - Handling uninitialized variable
try:
    print(x)  # This will cause a NameError
except NameError:
    print("Lab 1: x is not defined")

# Lab Example #2 - Handling uninitialized variable in an update
try:
    x = x + 1  # This will also cause a NameError
    print(x)
except NameError:
    print("Lab 2: x is not defined")

# Lab Example #3 - Proper initialization and updating of a variable
x = 0
x = x + 1
print("Lab 3:", x)

# Lab Example #4 - Using a shortcut for increment
x = 5
print("Lab 4:", x)
x += 1
print("Lab 4:", x)

# Lab Example #5 - Countdown using a while loop
n = 5
print('Lab 5: Say Cheese...')
while n > 0:
    print(n)
    n = n - 1
print("Click!")

# Lab Example #6 - Infinite loop example (handled with a break)
n = 5
x = True  # Boolean T/F
print('Lab 6: Say Cheese...')
while x:
    print(n)
    n = n - 1
    if n < 0:  # Adding a condition to break the infinite loop
        break
print("Click!")

# Lab Example #7 - Using 'break' to exit a loop
print("Lab 7: (Type 'done' to exit)")
while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)
print('Done!')

# Lab Example #8 - Using 'continue' to skip part of a loop
print("Lab 8: (Type 'done' to exit, '#' to skip)")
while True:
    line = input('> ')
    if line.startswith('#'):
        continue
    if line == 'done':
        break
    print(line)
print('Done!')

# Additional Example (Do-While Style)
x = 5
y = 3
print("Additional Example:")
while True:
    print('x =', x, '\ny =', y)
    z = x + y
    print('x + y =', z)
    if z == 8:
        break
    x += 1
    print('y is still', y, 'but x is now', x)
print('Done!')
