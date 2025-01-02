# price=15
# print(price)

# #String formatting
# name="Sathwika"
# print(f"Hello, {name}")

# name="Sahasra"
# print(f"Hello, {name}")

# #string Template

# name="Bob"
# greeting="Hello, {}"
# with_Name=greeting.format(name)
# print(with_Name)

# #Template string example 2
# longer_phrase = "Hello, {}.Today is {}"
# formatted=longer_phrase.format("Rolf","Monday")
# print(formatted)


# #getting user input
# name=input("What is your name?")
# print(name)

size=input("Enter the size of house in square feet : ")
square_feet=int(size)
square_metres=square_feet/10.8
print(square_metres)
print(f"{square_feet} square feet is {square_metres:.2f} square metres .")
