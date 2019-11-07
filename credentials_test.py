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

    def test_delete_credential(self):
        self.new_credentials.save_credentials()
        test_credential = Credentials("Bitbucket", "user2", "u@u.com", "123asdf")
        test_credential.save_credentials()

        self.new_credentials.delete_credentials()  # Deleting a contact object
        self.assertEqual(len(Credentials.credentials_list), 1)

    def test_find_by_platform(self):
        """
        test to check if we can find a credential by platform name and display information
        """

        self.new_credentials.save_credentials()
        test_credential = Credentials("Bitbucket", "user2", "u@u.com", "123asdf")
        test_credential.save_credentials()

        found_credential = Credentials.find_by_platform("Bitbucket")

        self.assertEqual(found_credential.platform, test_credential.platform)

        def test_credential_exists(self):
            """
            test to check if we can return a Boolean  if we cannot find the credential.
            """

            self.new_credential.save_credential()
            test_credential = Credentials("Bitbucket", "user2", "u@u.com", "123asdf")
            test_credential.save_credentials()

            self.assertTrue(Credentials.credentials_exists("Bitbucket"))

        def test_display_credentials(self):
            """
            method that returns a list of all saved credentials
            """
            self.assertEqual(Credentials.display_credentials(), Credentials.credentials_list)

        def test_copy_password(self):
            """
            Test to confirm that we are copying the password from a found credential
            """

            self.new_credential.save_credential()
            Credentials.copy_password("Github")

            # self.assertEqual(self.new_credential.password, pyperclip.paste())

        def test_generate_password(self):
            """
            Test to confirm that the password we are generating ahs the desired length
            """
            self.new_credential.save_credential()
            generated_password = Credentials.generate_password(12)
            test_credential = Credentials("Bitbucket", "user2", "u@u.com", generated_password)
            test_credential.save_credential()

            self.assertEqual(len(test_credential.password), 12)

    if __name__ == "__main__":
        unittest.main()