class User:


    user_list = []

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def create_user(self):
        """
            this method appends new object to user_list
            """
        User.user_list.append(self)

    @classmethod
    def user_auth(cls, name, password):
        """
        This method returns a boolean True if the username and pin inputted
        matches those of a user in the user_list
        """
        for user in cls.user_list:
            if user.username == name and user.password == password:
                return True
        return False