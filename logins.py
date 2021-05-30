class Credential:
  """
  a class that creates new credentials for users
  """
  credential_list = []

  def __init__(self, user_name, password):
      self.user_name = user_name
      self.password = password

  def save_credential(self):
      """
      save_credential method saves credentials objects into credential_list
      """
      Credential.credential_list.append(self)

  @classmethod
  def display_credential(cls):
      """
      method that returns the credential array
      """
      return cls.credential_list


