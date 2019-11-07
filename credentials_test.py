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
        self.new_credentials.save_credentials()  # saving the new contact
        self.assertEqual(len(Credentials.credentials_list), 1)

    def tearDown(self):
        Credentials.credentials_list = []

    def test_save_multiple_contact(self):
        self.new_credentials.save_credentials()
        test_credential = Credentials("Bitbucket", "user2", "u@u.com", "123asdf")  # new contact
        test_credential.save_credentials()
        self.assertEqual(len(Credentials.credentials_list), 2)
