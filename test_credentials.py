import pyperclip
from credentials import Credentials
import unittest


class TestCredential(unittest.TestCase):

    def setUp(self):
        self.credentials = Credentials()
        self.new_credentials = Credentials("user300", "Boom", "user300@email", "GitHub")

    def test_init(self):
        self.assertEqual(self.new_credentials.username, "user300")
        self.assertEqual(self.new_credentials.password, "Boom")
        self.assertEqual(self.new_credentials.email, "user300@email")
        self.assertEqual(self.new_credentials.platform, "GitHub")

    def test_save_credential(self):
        self.new_credentials.save_credentials()  # saving the new contact
        self.assertEqual(len(Credentials.credentials_list), 1)

    def tearDown(self):
        Credentials.credentials_list = []

    def test_save_multiple_contact(self):
        self.new_credentials.save_credentials()
        test_credential = Credentials("user2", "124asdf", "u@u.com", "Bitbucket")  # new contact
        test_credential.save_credentials()
        self.assertEqual(len(Credentials.credentials_list), 2)

    def test_delete_credential(self):
        self.new_credentials.save_credentials()
        test_credential = Credentials("user2", "124asdf", "u@u.com", "Bitbucket")
        test_credential.save_credentials()

        self.new_credentials.delete_credentials()  # Deleting a contact object
        self.assertEqual(len(Credentials.credentials_list), 1)

    def test_find_by_platform(self):
        """
        test to check if we can find a credential by platform name and display information
        """

        self.new_credentials.save_credentials()
        test_credential = Credentials("user2", "124asdf", "u@u.com", "BitBucket")
        test_credential.save_credentials()

        found_credential = Credentials.find_by_platform("BitBucket")

        self.assertEqual(found_credential.platform, test_credential.platform)

    def test_credential_exist(self):
        self.new_credentials.save_credentials()
        test_credential = Credentials("Bitbucket", "user2", "u@u.com", "123asdf")
        test_credential.save_credentials()

        self.assertTrue(Credentials.credentials_exists("123asdf"))

    def test_display_credentials(self):
        self.assertEqual(Credentials.display_credentials(), Credentials.credentials_list)

    def test_copy_password(self):
        self.new_credentials.save_credentials()
        Credentials.copy_password(self.new_credentials.platform)

        self.assertEqual(self.new_credentials.password, pyperclip.paste())

    def test_generate_password(self):
        """
        Test to confirm that the password we are generating ahs the desired length
        """
        self.new_credentials.save_credentials()
        generated_password = Credentials.generate_password(5)
        test_credential = Credentials("Bitbucket", "user2", "u@u.com", generated_password)
        test_credential.save_credentials()

        self.assertEqual(len(test_credential.password), 5)


if __name__ == "__main__":
    unittest.main()
