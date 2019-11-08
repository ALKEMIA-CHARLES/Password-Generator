from credentials import Credentials
from user import User
import random

welcome = "Welcome to Password Locker "
parser = argparse.ArgumentParser(description=welcome)
parser.parse_args()


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
