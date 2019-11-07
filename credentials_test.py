from credentials import Credentials
import unittest

class TestCredentials(unittest.TestCase):

    def setUp(self):

        self.new_credentials = Credentials("Facebook", "user101", "user101@email", "QwerY23")