import unittest
import pyperclip
from password import User


class TestUser(unittest.TestCase):
  '''
  Test class that defines test cases for the user class behaviours.

  Args:
    unittest.TestCase: TestCase class that helps in creating user test cases
  '''
def setUp(self):
  '''
  Set up method to run before each test cases in User
  '''
  self.new_user = User("Nicholas","Ngetich","NgetichNick","0725470732","ngetichnicholas903@gmail.com") #creating user object