import hashlib
import getpass
import sys

class login_directory:
    def __init__(self):
      self.__directory = {}

    @property
    def directory(self):
        raise PermissionError("Direct access to user directory is not allowed.")

    def add_user(self):
      if self.__directory:
        Main=self.authentication()
        if Main==True:
          print("Enter username:")
          username=input().strip()
          while True:
            print("Enter password:-")
            password=getpass.getpass().strip()
            print("Re-enter password:-")
            password2=getpass.getpass().strip()
            if password != password2:
              print("Passwords do not match. User not added.")
              continue
            else:
              break
          hashed_password = hashlib.sha256(password.encode()).hexdigest()
          self.__directory[username] = hashed_password
          print("User added successfully.")
          print()
        else:
          print("authentication failed. Cannot add user.")
      else:
          print("Enter username:")
          username=input().strip()
          while True:
            print("Enter password:-")
            password=getpass.getpass().strip()
            print("Re-enter password:-")
            password2=getpass.getpass().strip()
            if password != password2:
              print("Passwords do not match. User not added.")
              continue
            else:
              break
          hashed_password = hashlib.sha256(password.encode()).hexdigest()
          self.__directory[username] = hashed_password
          print("User added successfully.")
          print()
  
    def authentication(self):
      no=3
      while no>0:
        print("Enter UserName:")
        username =input().strip()
        if username not in self.__directory:
          print("Username not found.")
          no-=1
          print(f"You have {no} attempts left.")
          continue
        print("Enter password:-")
        password=getpass.getpass().strip()
        login_hashed_password = hashlib.sha256(password.encode()).hexdigest()
        if self.__directory[username]==login_hashed_password:
          print("Authentication successful.")
          return True
        else:
          print("Incorrect password.")
          no-=1
          print(f"You have {no} attempts left.")
          print("Authentication failed.")
      return False


    def view_users(self):
      if self.__directory:
        Main=self.authentication()
        if Main==True:
          print("Registered Users:")
          for user in self.__directory:
            print(user)
        else:
          print("authentication failed. Cannot view users.")
      else:
        print("No users registered.")
          
      
    def delete_user(self):
      if self.__directory:
        Main=self.authentication()
        if Main==True:
          print("Enter username to delete:")
          username =input().strip()
          if username in self.__directory:
            print("Are you sure you want to delete this user? (yes/no)")
            confirmation=input().strip().lower()
            if confirmation == 'yes':
              del self.__directory[username]
              print("User deleted successfully.")
              return
            else:
              print("User deletion cancelled.")
              return
          else:
            print("Username not found.")
            return
        else:
          print("authentication failed. Cannot delete user.")
      else:
        print("No users registered.")

    def change_password(self):
      if self.__directory:
        Main=self.authentication()
        if Main==True:
          print("Enter username to change password:")
          username=input().strip()
          if username in self.__directory:
            print("Enter new password:-")
            password=getpass.getpass().strip()
            print("Re-enter new password:-")
            password2=getpass.getpass().strip()
            if password != password2:
              print("Passwords do not match. Password not changed.")
              return
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            self.__directory[username] = hashed_password
            print("Password changed successfully.")
            return
          else:
            print("Username not found.")
            return
        else:
          print("authentication failed. Cannot change password.")
      else:
        print("No users registered.")

if __name__ == "__main__":
    ld = login_directory()
    print(ld.directory)
    while True:
      print("1. Add Users")
      print("2. view Users")
      print("3. Delete Users")
      print("4. Change Password")
      print("5. Exit")
      no =str(input("Enter your choice: ")).strip()
      if no=='1':
        ld.add_user()
      elif no=='2':
        ld.view_users()
      elif no=='3':
        ld.delete_user()
      elif no=='4':
        ld.change_password()
      elif no=='5':
        print("Exiting...")
        sys.exit()
      else:
        print("Invalid choice. Please try again.")
        continue  