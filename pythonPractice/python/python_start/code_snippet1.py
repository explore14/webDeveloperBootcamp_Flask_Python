# #no.of months for given year
# year=input("Enter no.of years : ")
# month=(int(year))*12
# print(f"no.of months for {year} year is {month}")

# #list
# l=["bob","mob","lob"]
# t=("bob","mob","lob")
# s={"bob","mob","lob"}
# print(l[0])
# print(t[0])
# print(s)
# l.append("cat")
# print(l)
# s.add("Smith")
# print(s)
# s.add("bob")
# print(s)

# #Advanced operations on set

# friends={"Bob","Rolf","Anne"}
# abroad={"bob","Anne"}

# local_friends=abroad.difference(friends)
# print(local_friends)

# local_union= friends.union(abroad)
# print(local_union)

# local_intersection = friends.intersection(abroad)
# print(local_intersection)

# day_of_week= input("what day of the week is it today ?").lower()

# if day_of_week=='monday':
#     print("Today is Monday")

# elif day_of_week=='tuesday':
#     print("Today is Tuesday")

# else:
#     print("Full speed ahead")


# #in in python

# movies_watched={"The Matrix","Green Book","Her"}
# user_movie=input("Enter the movie which you want to watch?")

# if user_movie in movies_watched:
#     print(f"I've watched {user_movie} too!")
# else:
#     print(f"I haven't watched {user_movie} yet")


# number=7
# user_input=input("Would you like to play the Game ?(Y/n)")

# while user_input in ("Y"):
#     user_number = int(input("Guess the number : "))
#     if user_number is number:
#         print("Wohoo ,you won the Game !")
    
#     elif abs(number-user_number) in (1,-1):
#         print("You were off by one")

#     else:
#         print("Oops!Try again")

#     user_input=input("Would you like to play the Game ?(Y/n)")

# if user_input=='n':
#     print("Thanks for playing!!")



# number=7

# while True:
#     user_input=input("Would you like to play the Game ?(Y/n)")


#     if user_input=='n':
#         break

#     elif user_input=="Y":
#         user_number = int(input("Guess the number : "))
#         if user_number is number:
#             print("Wohoo ,you won the Game !")
        
#         elif abs(number-user_number) in (1,-1):
#             print("You were off by one")

#         else:
#             print("Oops!Try again")
##########################################
# friends=["Rolf","Jen","Bob","Anne"]

# for f in friends:
#     print(f)

# #list comprehensions in Python

# numbers=[1,3,5]
# doubled=[x*2 for x in numbers]
# print(doubled)

# l=[x for x in range(1,50) if x%3==0]
# print(l)

# string_names=["Bob","Vob","lob"]
# string_first_letter=[x[0] for x in string_names]
# print(string_first_letter)

# friends=["Rolf","Sam","Samantha","Jen"]
# starts_s=[friend for friend in friends if friend.startswith("S")]
# print(starts_s)

# # instead of :
# #  for friend in friends:
# #     if friend.startswith("S"):
# #         starts_s.append(friend)
######for knowing memory address : id(friends)

# ##Dictionary in python
# friend_ages= {"Rolf":24 ,"Adam":30 , "Anne":27}
# friend_ages["Bob"]=20
# print(friend_ages)

# ##list of dictionary
# friends = [
#     {"name": "Rolf", "age": 24},
#     {"name": "Bob", "age": 30},
#     {"name": "Anne", "age": 27}
# ]
# print(friends[0]["name"])
################################################
# student_attendance={"Rolf":96,"Bob":80,"Anne":100}

# for student,attendance in student_attendance.items():
#     print(f"{student} : {attendance}")

# attendance_values=student_attendance.values()
# print(sum(attendance_values)/len(attendance_values))
#############################################

# #Destructing in python
# people = [("Bob",42,"Mechanic"),("James",24,"Artist"),("Harry",32,"Professor")]

# for name,age,profession in people:
#     print(f"name: {name} , age: {age} , profession : {profession}")

# for person in people:
#     print(f"name: {person[0]} , age: {person[1]} , profession : {person[2]}")


