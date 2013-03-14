import unittest
from linkedlist import LinkedList, ListEmptyError


class Test_LinkedList(unittest.TestCase):
    def setUp(self):
        self.ll = LinkedList(4)
        self.ll.prepend(5)

    def test_simple(self):
        self.assertEqual(5, self.ll.peek())
        self.assertEqual(2, len(self.ll))

    def test_append(self):
        self.ll.append(6)
        self.assertEqual(5, self.ll.peek())
        self.assertEqual(3, len(self.ll))

    def test_len(self):
        self.ll.append(6)
        self.assertEqual(3, len(self.ll))

    def test_len_uninitialized(self):
        ll = LinkedList()
        ll.prepend(5)
        self.assertEqual(1, len(ll))

    def test_pop(self):
        head_value = self.ll.pop()
        self.assertEqual(5, head_value)
        self.assertEqual(1, len(self.ll))
        self.assertEqual(4, self.ll.peek())

    def test_isEmpty(self):
        ll = LinkedList()
        self.assertTrue(ll.isEmpty())

    def test_pop_empty(self):
        ll = LinkedList()
        self.assertRaises(ListEmptyError, ll.pop)

if __name__ == '__main__':
    unittest.main()
