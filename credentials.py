import pyperclip
import string
import random

class Credentials:

    credentials_list = []

    def __init__(self, username, password, email, platform):
        self.username = username
        self.password = password
        self.email = email
        self.platform = platform

    def save_credentials(self):

        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        Credentials.credentials_list.remove(self)

    @classmethod
    def find_by_platform(cls, platform):

        for credentials in cls.credentials_list:
            if credentials.platform == platform:
                return credentials

    def generate_password(self, length):
        """
        this method uses the string method to generate a password of random digits and letters
        the length of the password is determined by the length passed in the function's parameter
        Args:
            the desired password length
        """
        chars = string.ascii_uppercase + string.digits + string.ascii_lowercase
        return "".join(random.choice(chars) for i in range(length))

    @classmethod
    def credentials_exists(cls, platform):
        for credentials in cls.credentials_list:
            if credentials.platform == platform:
                return True

        return False

    @classmethod
    def display_credentials(cls):
        return cls.credentials_list

    @classmethod
    def copy_password(cls, platform):
        credentials_found = Credentials.find_by_platform(platform)
        pyperclip.copy(credentials_found.password)

    @classmethod
    def generate_password(cls, length):
        chars = string.ascii_uppercase + string.digits + string.ascii_lowercase
        return "".join(random.choice(chars) for i in range(length))