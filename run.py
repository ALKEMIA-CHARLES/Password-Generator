from credentials import Credentials
from user import User
import time
from getpass import getpass
import random


def create_user(username, password):
    new_user = User(username, password)
    return new_user


def save_user(user):
    "This function works to save all the user details"
    user.save_user()


def authenticate_user(username, password):
    return User.user_auth(username, password)


def create_credentials(username, password, email, platform):
    "This function works to create all of the credentials"
    new_credentials = Credentials(username, password, email, platform)


def save_credentials(credentials):
    "This functions saves credentials"
    credentials.save_credentials()


def delete_credentials(credentials):
    "This function deletes credentials"
    credentials.delete_credentials()


def look_for_credentials(platform):
    "This function looks for credentials"
    return Credentials.find_by_platform(platform)


def check_for_existing_credentials(platform):
    "This function checks on already existing credentials"
    return Credentials.credentials_exists(platform)


def display_credentials():
    "This function works to display the credentials"
    return Credentials.display_credentials()


def copy_password():
    "This function copies the password"
    return Credentials.copy_password()


def generate_password(length):
    "This function generates the password while checking the length at the same time"
    return Credentials.generate_password(length)


def main():
    print(""""
    Welcome to GEN-PASS
    WHERE ALL KINDS OF PASSWORDS ARE GENERATED TO SUIT YOUR SPECIFICATIONS
    """, "white")
    while True:
        print("""
           Use the following short codes to manage your account 
               'lg' - Login 
               'xx' - Close app
               """, "blue")
        print("What would you like to do?")
        code = input().lower()
        if code == "lg":
            print("Do you have an account? Y or N")
            decision = input().lower()

            if decision.startswith("n"):
                login_name = input("Enter your username: ")
                login_pin = getpass("Enter your pin: ")
                print("Loading ...")
                time.sleep(1.5)
                print("\n")
                print("CONGRATULATIONS, YOUR ACCOUNT HAS BEEN CREATED", "green", attrs=['bold'])
                print("Sign into your new account")
                sign_in_name = input("Enter your username: ")
                sign_in_pin = getpass("Enter your pin: ")
                save_user(create_user(login_name, login_pin))
                if authenticate_user(sign_in_name, sign_in_pin):
                    print("Please wait...")
                    time.sleep(1.5)
                    print("SUCCESSFULLY SIGNED IN", "green", attrs=['bold'])
                    print("\n")
                    pass
                else:
                    print("Please wait...")
                    time.sleep(1.5)
                    # cprint("Oops, you entered the wrong username/pin, we have to do this again :(","red")
                    print("\n")
            else:
                sign_in_name = input("Enter your username: ")
                sign_in_pin = getpass("Enter your pin: ")
                if authenticate_user(sign_in_name, sign_in_pin):
                    print("Please wait...")
                    time.sleep(1.5)
                    print("SUCCESSFULLY SIGNED IN", "green", attrs=['bold'])
                    print("\n")
                    pass
                else:
                    print("Please wait...")
                    time.sleep(1.5)
                    # cprint("Oops, you entered the wrong username/pin, we have to do this again :(","red")
                    print("\n")
            while True:
                if authenticate_user(sign_in_name, sign_in_pin):
                    ####
                    print(
                        """