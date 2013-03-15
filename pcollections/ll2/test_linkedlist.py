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
        self.assertEqual(4, self.ll.next.peek())
        self.assertEqual(6, self.ll.next.next.peek())

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

    def test_pop_to_empty(self):
        ll = LinkedList(5)
        self.assertEqual(1, len(ll))
        self.assertEqual(ll.next, None)
        self.assertFalse(ll.isEmpty())
        head_value = ll.pop()
        self.assertEqual(head_value, 5)
        self.assertEqual(0, len(ll))
        self.assertEqual(ll.next, None)
        self.assertTrue(ll.isEmpty())

    def test_isEmpty(self):
        ll = LinkedList()
        self.assertTrue(ll.isEmpty())

    def test_pop_empty(self):
        ll = LinkedList()
        self.assertRaises(ListEmptyError, ll.pop)

    def test_add(self):
        ll = LinkedList(4)
        ll.append(6)
        ll2 = LinkedList(10)
        ll2.append(12)
        ll2.append(13)
        ll = ll + ll2
        self.assertEqual(5, len(ll))

    def test_clear(self):
        self.assertFalse(self.ll.isEmpty())
        self.assertTrue(len(self.ll) == 2)
        self.ll.clear()
        self.assertTrue(self.ll.isEmpty())

    def test_clear_empty_list(self):
        ll = LinkedList()
        ll.clear()
        self.assertTrue(ll.isEmpty())

if __name__ == '__main__':
    unittest.main()
