import pyperclip
class User:
  '''
  Class that creates new intances of users
  '''

  user_list = [] # creates an empty user list

  def __init__(self,first_name,last_name,user_name,number,email):

    self.first_name = first_name
    self.last_name = last_name
    self.user_name = user_name
    self.phone_number = number
    self.email = email

  def save_user(self):
    '''
    save_user method saves user object into the user_list
    '''

    User.user_list.append(self)
# while True:
#   password = input("What is the password?")
#   if password == "nick1111":
#     print("ACCESS GRANTED")
#     break
#   else:
#     print("ACCESS DENIED")