name = "Obi-Wan"
surname = "Kenobi"
age = 36

greeting = "My name is " + name + " " + surname + " and \nI am " + str(age) + " years old."

length = len(greeting)

print(greeting)
print(greeting[0])
print(len(greeting))
print(greeting[length - 1])
print(greeting[-1])
print(greeting[3:7])
print(greeting[3:])
print(greeting[:17])
print(greeting[2:40:2])

# String formatted

print("My name is {} {}".format(name, surname))
print("My name is {1} {0}".format(name, surname))
print("My name is {s} {n}".format(n=name, s=surname))
print("My name is {} {} and I'm {} years old".format(name, surname, age))
print("My name is {} {} and I'm {} years old".format(name, name, name))

result = 200/700

print("The result is {r:1.3}".format(r=result))
print("The result is {r:8.3}".format(r=result))


print("My name is {name} {surname} and I'm {age} years old")

print("Example: ")