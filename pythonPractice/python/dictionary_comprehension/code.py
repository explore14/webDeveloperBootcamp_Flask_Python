users = [
    (0,"Bob","cat"),
    (1,"Rolf","dog"),
    (2,"Charlie","bird"),
    (3,"Jacob","Rabbit"),
]
username_mapping={user[1]:user for user in users}
print(username_mapping)

