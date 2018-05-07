import unittest
from password import Credentials

class TestCredential(unittest.TestCase):
	def setUp(self):
		self.crede= Credentials("github", "JaredAhaza","0717149020")
		self.newlist = []
		self.newlist.append(self.crede)
	def test_init(self):
		"""this method checks whether instantiation is correctly done"""

		self.assertEqual(self.crede.site, 'github')
		self.assertEqual(self.crede.username, 'JaredAhaza')
		self.assertEqual(self.crede.password, '0717149020')
	
	def test_number_of_credential(self):
		"""
        searches for the number of credentials for a user
        """
		print(self.newlist)
		self.assertEqual(len(self.newlist),1)

	def test_search_for_credentials(self):
		"""
        checks whether the searched account matches an account in the system
        """
		found_credential = Credentials("github", "JaredAhaza","0717149020")
		self.assertEqual(found_credential.site, "github")


if __name__ == '__main__':
	unittest.main()