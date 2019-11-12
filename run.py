import pyperclip
from credentials import Credentials
from user import User
import time
from getpass import getpass
import random


def create_user(username, password):
    new_user = User(username, password)
    return new_user


def save_user(user):
    """This function works to save all the user details"""
    user.save_user()


def authenticate_user(username, password):
    return User.user_auth(username, password)


def create_credentials(username, password, email, platform):
    """This function works to create all of the credentials"""
    new_credentials = Credentials(username, password, email, platform)
    return new_credentials


def save_credentials(credentials):
    """This functions saves credentials"""
    credentials.save_credentials()


def delete_credentials(credentials):
    """This function deletes credentials"""
    credentials.delete_credentials()


def look_for_credentials(platform):
    """This function looks for credentials"""
    return Credentials.find_by_platform(platform)


def check_for_existing_credentials(platform):
    """This function checks on already existing credentials"""
    return Credentials.credentials_exists(platform)


def display_credentials():
    """This function works to display the credentials"""
    return Credentials.display_credentials()


def copy_password():
    """This function copies the password"""
    return Credentials.copy_password()


def generate_password(length):
    """This function generates the password while checking the length at the same time"""
    return Credentials.generate_password(length)


def main():
    print(""""
    Welcome to GEN-PASS
    WHERE ALL KINDS OF PASSWORDS ARE GENERATED TO SUIT YOUR SPECIFICATIONS
    """)
    while True:
        print("""
           Use the following short codes to manage your account 
               'lg' - Login 
               'log-out' - Close app
               """, )
        print("What would you like to do?")
        key_word = input().lower()
        if key_word == "lg":
            print("Do you have an account? Y or N")
            decision = input().lower()

            if decision.startswith("n"):
                login_name = input("Enter your username: ")
                login_pin = getpass("Enter your password: ")
                print("Loading ...")
                time.sleep(1.5)
                print("\n")
                print("Hey Look at you, you have just created your first GEN-PASS account")
                print("Sign into your new account")
                sign_in_name = input("Enter your username: ")
                sign_in_pin = getpass("Enter your password: ")
                save_user(create_user(login_name, login_pin))
                if authenticate_user(sign_in_name, sign_in_pin):
                    print("Please wait...")
                    time.sleep(1.5)
                    print("You have just signed in")
                    print("\n")
                    pass
                else:
                    print("Please wait...")
                    time.sleep(1.5)
                    print("\n")
            else:
                sign_in_name = input("Enter your username: ")
                sign_in_pin = getpass("Enter your password: ")
                if authenticate_user(sign_in_name, sign_in_pin):
                    print("Please wait...")
                    time.sleep(1.5)
                    print("You have successfully signed in")
                    print("\n")
                    pass
                else:
                    print("Please wait...")
                    time.sleep(1.5)
                    print("\n")
            while True:
                if authenticate_user(sign_in_name, sign_in_pin):
                    ####
                    print(
                        """
                    WELCOME TO PASS-GEN:
                        Use the following commands to navigate the application:
                            'create' - enables you to create an a credential
                            'display' - displays the credentials you have saved
                            'copy' - copies the password of a given credential
                            'find' - helps you find a credential by its platform name
                            'del' - deletes a credential
                            'log-out' - logs you out
                            'help' - helps a user around the app
                                            """, "white")
                    print(f" Hello there, {sign_in_name}, what task would you like to perform?")
                    key_word = input().lower()

                    if key_word == 'create':
                        print("Save a new credential")
                        platform = input("Input the platform: ")
                        print("\n")
                        username = input("Input your username: ")
                        print("\n")
                        email = input("Input your email: ")
                        print("\n")
                        option = input("Would you like to have Gen-Pass generate a password for you? Y or N ? ").lower()
                        if option.startswith("y"):
                            print()
                            desired_len = int(
                                input("How long would you like your password to be? Provide number only? "))
                            password = generate_password(desired_len)
                        else:
                            print("\n")
                            password = getpass("Enter your password: ")

                        save_credentials(create_credentials(platform, username, email, password))
                        print('\n')
                        print(f"congratulations you have successfully created credentials for {platform} ")
                        print("_" * 50)
                        print('\n')

                    elif key_word == 'display':

                        if display_credentials():
                            print("This is how your credentials look like !")
                            print('\n')

                            for cred in display_credentials():
                                print(
                                    f"""
                                Platform --- {cred.platform}               
                                         Username --- {cred.username}               
                                         Email    --- {cred.email}                  
                                         Password --- {cred.password}
                                    """)
                                print('\n')
                            else:
                                print('\n')
                                print("You don't seem to have any credentials saved yet",)
                                print("_" * 50)
                                print('\n')

                    elif key_word == 'find':
                        print("Enter the platform you want to search for")
                        print("\n")
                        platform_search = input()
                        if check_for_existing_credentials(platform_search):
                            search_credential = look_for_credentials(platform_search)
                            print(
                                f"""
                                Platform --- {search_credential.platform}               
                                     Username --- {search_credential.username}               
                                     Email    --- {search_credential.email}                  
                                     Password --- {search_credential.password}
                                     """)
                            print("_" * 50)
                        else:
                            print("The credential you have searched does not exist",)
                elif key_word == "copy":
                    print("Enter the platform whose password you would like copied")
                    platform_find = input()
                    print("Loading...")
                    if check_for_existing_credentials(platform_find):
                        search_credential = look_for_credentials(platform_find)
                        pyperclip.copy(search_credential.password)
                        time.sleep(1.5)
                        print("\n")
                        print(f" Good work password for {search_credential.platform} has been coped")
                        print("_" * 50)

                    else:
                        print("The platform you entered does not exist", "yellow")
                        print("_" * 50)

                elif key_word == "del":
                    print("Enter the platform whose credentials you'd like to delete")
                platform_delete = input()
                if check_for_existing_credentials(platform_delete):
                    print("Please wait ...")
                    platform_credentials = look_for_credentials(platform_delete)
                    delete_credentials(platform_credentials)
                    time.sleep(1.5)
                    print(f"Credentials for {platform_credentials.platform} successfully deleted")
                else:
                    print("The credential does not exist")

        elif key_word == "help":
            print("Don't panic I got you")

        else:
            print(
                "You entered an unknown keyword. Please use the provided keywords. Type '-help' if you're stuck")
        print("_" * 50)
        break


if __name__ == '__main__':
    main()
