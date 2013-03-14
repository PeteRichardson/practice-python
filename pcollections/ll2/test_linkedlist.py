import unittest
from linkedlist import LinkedList


class Test_LinkedList(unittest.TestCase):
    def test_simple(self):
        ll = LinkedList(4)
        ll.prepend(5)
        self.assertEqual(5, ll.peek())
        self.assertEqual(2, len(ll))

    def test_append(self):
        ll = LinkedList(4)
        ll.append(5)
        self.assertEqual(4, ll.peek())
        self.assertEqual(2, len(ll))

    def test_len(self):
        ll = LinkedList(4)
        ll.prepend(5)
        ll.append(3)
        self.assertEqual(3, len(ll))

if __name__ == '__main__':
    unittest.main()
