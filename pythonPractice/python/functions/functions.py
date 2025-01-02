# def age_in_seconds():
#     age=int(input("Enter the age : "))
#     seconds=age*365*24*60*60
#     print(f"Age of person is {age} and seconds is {seconds}")

# age_in_seconds()


def add(x,y):
    pass

###########################3
# #keyword arguments
# def say_hello(name,surname):
#     print(f"Hello, {name} {surname}")

# say_hello(surname="Bob",name="Laila")


#default parameter
def add(x,y= 8,z=5):
    print(x+y)

add(5,2,3)
print(add(5,2))
