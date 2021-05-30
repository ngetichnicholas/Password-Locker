#!/usr/bin/env python3.6
from password import User

def create_user(fname,lname,uname,phone,email):
  '''
  Function to create a new user
  '''
  new_user = User(fname,lname,uname,phone,email)
  return new_user

def save_user(user):
  '''
  Function to save user
  '''
  user.save_user()

def del_user(user):
  '''
  Function to delete a user
  '''
  user.delete_user()

def copy_email(user,number):
  '''
  Function to delete a user
  '''
  user.copy_email(number)

def find_user(number):
  '''
  Function that finds a user by number and returns the user
  '''
  return User.find_by_number(number)

def check_existing_user(number):
  '''
  Function that check if user exists with number and returns a Boolean
  '''
  return User.user_exist(number)

def display_users():
  '''
  Function that returns all the saved users
  '''
  return User.display_users()

def main():
  print("Hello Welcome to your user list. What is your name?")
  user_name = input()

  print(f"Hello {user_name}. what would you like to do?")
  print('\n')

  while True:
    print("Use these short codes : \n cc - create a new user \n dc - display users \n fc -find a user \n dl - to delete user \n cp - to copy email address \n ex -exit the user list ")

    short_code = input().lower()

    if short_code == 'cc':
      print("New user")
      print("-"*10)

      print ("First name ....")
      f_name = input()

      print("Last name ...")
      l_name = input()

      print("Username ...")
      u_name = input()

      print("Phone number ...")
      p_number = input()

      print("Email address ...")
      e_address = input()


      save_user(create_user(f_name,l_name,u_name,p_number,e_address)) # create and save new user.
      print ('\n')
      print(f"New user {f_name} {l_name} created")
      print ('\n')

    elif short_code == 'dc':

      if display_users():
        print("Here is a list of all your users")
        print('\n')

        for user in display_users():
          print(f"{user.first_name} {user.last_name} .....{user.phone_number}")

        print('\n')
      else:
        print('\n')
        print("You dont seem to have any users saved yet")
        print('\n')

    elif short_code == 'fc':
      print("Enter the number you want to search for")

      search_number = input()
      if check_existing_user(search_number):
        search_user = find_user(search_number)
        print(f"{search_user.first_name} {search_user.last_name}")
        print('-' * 20)

        print(f"Phone number.......{search_user.phone_number}")
        print(f"Email address.......{search_user.email}")
      else:
        print("That user does not exist")


    elif short_code == 'dl':

      print("Enter the number you want to delete")

      delete_number = input()
      if check_existing_user(delete_number):
        dl_user = find_user(delete_number)
        print(f"{dl_user.first_name} {dl_user.last_name} will be deleted")
        dl_user = del_user(dl_user)
        print("user deleted successfully")

      else:
        print("That user does not exist")

    elif short_code == 'cp':

      print("Enter the number you want to copy email from")

      find_number = input()
      if check_existing_user(find_number):
        email_user = find_user(find_number)
        print(f"{email_user.first_name} {email_user.last_name}  {email_user.email} email address will be copied")
        email_user = copy_email(email_user,find_number)
        print("Email address copied successfully")

      else:
        print("That user does not exist")


    elif short_code == "ex":
      print("Bye .......")
      break
    else:
      print("I really didn't get that. Please use the short codes")

if __name__ == '__main__':

  main()