# class Bank:
#     def __init__(self, owner, pinkod, balance):
#         self.owner = owner
#         self.__pinkod = pinkod
#         self._balance = balance

#     @property
#     def show_balance(self):
#         return f"Balance: {self._balance}"

#     @show_balance.setter
#     def show_balance(self, amount):
#         if amount > 0:
#             self._balance+=amount
#             return f"New balance {self._balance}"

# card1 = Bank("Ehson", 1234, 10000)

# print(card1.show_balance)
# card1.show_balance = 10
# print(card1.show_balance)




# from datetime import datetime

# task_db = []
# user_db = []

# is_login = None
# user_id = 0
# task_id = 0


# def create_task(title, description, dueration, user_id):
#     global task_id

#     task_id += 1

#     task = {
#         "task_id": task_id,
#         "title": title,
#         "description": description,
#         "dueration": dueration,
#         "status": False,
#         "user_id": user_id,
#         "created_at": datetime.now()
#     }

#     task_db.append(task)


# def read_task(task_id, user_id):
#     for i in task_db:
#         if i["task_id"] == task_id and i["user_id"] == user_id:

#             username = ""

#             for user in user_db:
#                 if user["user_id"] == i["user_id"]:
#                     username = user["username"]

#             return f"""
# Your task {i["task_id"]}:
# Username: {username}
# Title: {i["title"]}
# Description: {i["description"]}
# Dueration: {i["dueration"]}
# Status: {i["status"]}
# Created at: {i["created_at"]}
# """

#     return False


# def update_task(task_id, title, descp, due, status, user_id):
#     for i in task_db:
#         if i["task_id"] == task_id and i["user_id"] == user_id:
#             if title:
#                 i["title"] = title
#             if descp:
#                 i["description"] = descp
#             if due:
#                 i["dueration"] = due
#             if status:
#                 i["status"] = status
#             return True
#     return False


# def delete_task(task_id, user_id):
#     for i in task_db:
#         if i["task_id"] == task_id and i["user_id"] == user_id:
#             task_db.remove(i)
#             return True

#     return False


# def registration(username, password):
#     global user_id, is_login

#     user_id += 1

#     user = {
#         "user_id": user_id,
#         "username": username,
#         "password": password,
#         "created_at": datetime.now()
#     }

#     user_db.append(user)

#     is_login = user


# def login(username, password):
#     global is_login

#     for user in user_db:
#         if user["username"] == username and user["password"] == password:
#             is_login = user
#             return True

#     return False


# def change_password(user_id, old_password, new_password):
#     for user in user_db:

#         if user["user_id"] == user_id:

#             if user["password"] == old_password:
#                 user["password"] = new_password
#                 return True

#             return False

#     return False


# def show_profile(user_id):
#     for user in user_db:

#         if user["user_id"] == user_id:

#             return f"""
# ===== PROFILE ======

# ID: {user["user_id"]}
# Username: {user["username"]}
# Created at: {user["created_at"]}

# =================================
# """

#     return False

# while True:
#     if is_login is None:
#         n = int(input("\n1)Register\n2)Login\n0)Exit\nChoose one: "))

#         match n:

#             case 1:
#                 username = input("Username: ")
#                 password = input("Password: ")
#                 registration(username, password)
#                 print("Registration successful!")
#             case 2:
#                 username = input("Username: ")
#                 password = input("Password: ")
#                 if login(username, password):
#                     print("Login successful!")
#                 else:
#                     print("Wrong username or password!")
#             case 0:
#                 print("Good bye")
#                 break
#             case _:
#                 print("Invalid input!")
#     else:

#         n = int(input("1)Create Task\n2)Read Task\n3)Update Task\n4)Delete Task\n5)Change Password\n6)Show Profile\n7)Search User\n0)Exit\nChoose one: "))

#         match n:
#             case 1:
#                 print("Start create task")
#                 title = input("Title: ")
#                 descp = input("Description: ")
#                 durat = input("Duration: ")
#                 create_task(title,descp,durat,is_login["user_id"])
#                 print("Task created!!")
#             case 2:
#                 k = int(input("Enter id task: "))
#                 result = read_task(k,is_login["user_id"])
#                 if result:
#                     print(result)
#                 else:
#                     print("This task doesn't exist!")


#             case 3:
#                 print("===Start update task===")
#                 k = int(input("Enter id task: "))
#                 if read_task(k, is_login["user_id"]):
#                     title = input("Title or put enter for continue: ")
#                     descp = input("Description or put enter for continue: ")
#                     durat = input("Duration or put enter for continue: ")
#                     status = input("Status (True/False) or put enter: ")

#                     if status:
#                         status = status.lower() == "true"
#                     else:
#                         status = False

#                     update_task(k,title,descp,durat,status,is_login["user_id"])
#                     print("Task updated!!")
#                 else:
#                     print("This task doesn't exist!")
#             case 4:

#                 k = int(input("Enter id task: "))

#                 if delete_task(k,is_login["user_id"]):
#                     print("Your task deleted!")
#                 else:
#                     print("This task doesn't exist!")
#             case 5:

#                 print("Change Password")

#                 old_password = input("Old password: ")
#                 new_password = input("New password: ")

#                 if change_password(is_login["user_id"],old_password,new_password):
#                     print("Password changed successfully!")
#                 else:
#                     print("Old password is incorrect!")
#             case 6:
#                 print(show_profile(is_login["user_id"]))
#             case 0:
#                 print("Exit")
#                 break
#             case _:
#                 print("Invalid input!")