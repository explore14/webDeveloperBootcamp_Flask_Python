users=[
    (0,"Bob","cat"),
    (1,"Rolf","dog"),
    (2,"Charlie","bird"),
    (3,"Jacob","Rabbit"),
]

user_mapping={user[1]:user for user in users}

username_input= input("Enter username: ")
password_input = input("Enter password: ")

_,username,password= user_mapping[username_input]

if password_input==password:
    print("Successfully logined")
    print("Welcome!!")

else:
    print("Invalid username or password")