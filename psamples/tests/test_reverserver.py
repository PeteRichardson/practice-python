''' test_reverserver.py '''

import unittest
import sys
import os
sys.path.append(os.path.join(sys.path[0], '..'))

from reverserver import ReverServer
from xmlrpclib import ServerProxy
import threading


class ServerThread(threading.Thread):
    '''run a ReverServer in a separate thread'''

    def run(self):
        ReverServer("localhost", 6666, logRequests=False).start()


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
