from credentials import Credentials
from user import User
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
