import pyperclip
import string
import random
class Credentials:
    credentials_list = []

    def __init__(self, username, password):
        self.username =  username
        self.password = password

    def save_credentials(self):

        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        Credentials.credentials_list.remove(self)