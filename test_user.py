import unittest
from user import User

class UserTest(unittest.TestCase):
    def setUp(self):
        self.new_user = User("user800", "8000")
    def test_init(self):
        self.assertEqual(self.new_user.username, "user800")
        self.assertEqual(self.new_user.password, "8000")

    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)

    def test_user_auth(self):
        """
        test_user_auth tests case to authenticate the user
        """
        self.assertTrue(self.new_user.user_auth("user800", "8000"))

if __name__ == "__main__":
    unittest.main()