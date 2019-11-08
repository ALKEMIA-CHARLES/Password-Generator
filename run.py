from credentials import Credentials
from user import User
import random

welcome = "Welcome to Password Locker "
parser = argparse.ArgumentParser(description=welcome)
parser.parse_args()


def create_user(username, password):
    new_user = User(username, password)
    return new_user
