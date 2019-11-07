import unittest
from user import User

class UserTest(unittest.TestCase):
    def setUp(self):
        self.new_user = User("user800", "8000")
    def test_init(self):
        self.assertEqual(self.new_user.username, "user100")
        self.assertEqual(self.new_user.password, "8000")

    def test_save_user(self):