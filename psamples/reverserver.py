''' reverserver.py - a simple xmlrpc server that exposes a function
                     to reverse a string'''

from SimpleXMLRPCServer import SimpleXMLRPCServer


class ReverServer(SimpleXMLRPCServer):
    '''a simple xmlrpc server that exposes a function to reverse a string'''
    def __init__(self, host, port):
        SimpleXMLRPCServer.__init__(self, (host, port))

        self.register_introspection_functions()
        self.register_function(self.reverse, "reverse")

    @classmethod
    def reverse(cls, data):
        '''return the reverse of the input string'''
        return data[::-1]

    def start(self):
        '''start spreading the news'''
        self.serve_forever()

if __name__ == "__main__":
    SERVER = ReverServer("localhost", 6666)
    SERVER.start()
