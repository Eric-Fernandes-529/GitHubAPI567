import unittest
import json
from unittest.mock import Mock,patch
from HW04 import GetRepos

class Test(unittest.TestCase):
    @patch('HW04.requests.get')
    def test1(self,mock_get):
        mock_get.json=[{"name":"repo1"},{"name":"repo2"}]
        print("Result"+GetRepos("Eric-Fernandes-529"))
        self.assertIsNotNone(GetRepos("Eric-Fernandes-529"))
    
if __name__ == '__main__':
    unittest.main()