''' test_reverserver.py '''

import unittest
from reverserver import ReverServer
from xmlrpclib import ServerProxy
import threading


class ServerThread(threading.Thread):
    '''run a ReverServer in a separate thread'''

    def run(self):
        ReverServer("localhost", 6666).start()


class Test_ReverServer(unittest.TestCase):
    '''simple tests for ReverServer'''

    def test_simple(self):
        ''' simple test reversing a single string '''
        ServerThread().start()

        proxy = ServerProxy("http://localhost:6666")
        data = 'slartybartfast'
        result = proxy.reverse(data)
        self.assertEqual(data[::-1], result)
        proxy.shutdown()

if __name__ == "__main__":
    unittest.main()
