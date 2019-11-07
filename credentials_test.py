from credentials import Credentials
import unittest

class TestCredentials(unittest.TestCase):

    def setUp(self):

        self.new_credentials = Credentials("Facebook", "user101", "user101@email", "QwerY23")

    def test_init(self):
        self.assertEqual(self.new_credentials.password, "QwerY23")
        self.assertEqual(self.new_credentials.username, "user101")
        self.assertEqual(self.new_credentials.platform, "Github")

    def test_save_credential(self):
        self.new_credential.save_credential()  # saving the new contact
        self.assertEqual(len(Credentials.credentials_list), 1)