''' test_reverserver.py '''

import unittest
from xmlrpclib import ServerProxy

class Test_ReverServer(unittest.TestCase):
    '''simple tests for ReverServer'''

    def test_simple(self):
        ''' simple test reversing a single string '''
        data = 'slartybartfast'
        proxy = ServerProxy("http://localhost:6666")
        result = proxy.reverse(data)
        self.assertEqual(data[::-1], result)


if __name__ == "__main__":
    unittest.main()
