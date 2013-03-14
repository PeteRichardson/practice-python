import unittest
from linkedlist import LinkedList


class Test_LinkedList(unittest.TestCase):
    def test_simple(self):
        ll = LinkedList()
        ll.prepend(4)
        head = ll.head()
        self.assertEqual(4, head)

    def test_len(self):
        ll = LinkedList(4)
        ll.prepend(5)
        self.assertEqual(2, len(ll))

if __name__ == '__main__':
    unittest.main()
