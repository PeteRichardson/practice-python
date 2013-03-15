import unittest
from linkedlist import LinkedList, ListEmptyError


class Test_LinkedList(unittest.TestCase):
    def setUp(self):
        self.ll = LinkedList(4)
        self.ll.prepend(5)

    def test_simple(self):
        self.assertEqual(5, self.ll.peek())
        self.assertEqual(2, len(self.ll))

    def test_prepend(self):
        ll = LinkedList(3)
        self.assertEqual(1, len(ll))
        self.assertEqual(3, ll.peek())
        ll.prepend(2)
        self.assertEqual(2, len(ll))
        self.assertEqual(2, ll.peek())
        ll.prepend(1)
        self.assertEqual(3, len(ll))
        self.assertEqual(1, ll.peek())

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

    def test_reversed(self):
        ll = LinkedList(7)
        ll.append(8)
        ll.append(9)
        self.assertEqual(3, len(ll))
        self.assertEqual(7, ll.peek())
        self.assertEqual("7->8->9", str(ll))
        rev = ll.reversed()
        self.assertEqual("9->8->7", str(rev))
        self.assertEqual(9, rev.peek())
        self.assertEqual(3, len(ll))
        self.assertEqual(7, ll.peek())
        self.assertEqual("7->8->9", str(ll))

    def test_reverse(self):
        ll = LinkedList(7)
        ll.append(8)
        ll.append(9)
        self.assertEqual(3, len(ll))
        self.assertEqual(7, ll.peek())
        self.assertEqual("7->8->9", str(ll))
        ll.reverse()
        self.assertEqual("9->8->7", str(ll))
        self.assertEqual(9, ll.peek())

    def test_reverse_double(self):
        ll = LinkedList(45)
        ll.append(46)
        self.assertEqual(2, len(ll))
        self.assertEqual(45, ll.peek())
        self.assertEqual("45->46", str(ll))
        ll.reverse()
        self.assertEqual(2, len(ll))
        self.assertEqual(46, ll.peek())
        self.assertEqual("46->45", str(ll))


    def test_reverse_single(self):
        ll = LinkedList(358)
        self.assertEqual(358, ll.peek())
        self.assertEqual(1, len(ll))
        ll.reverse()
        self.assertEqual(358, ll.peek())
        self.assertEqual(1, len(ll))

    def test_reverse_empty(self):
        ll = LinkedList()
        self.assertTrue(ll.isEmpty())
        ll.reverse()
        self.assertTrue(ll.isEmpty())

if __name__ == '__main__':
    unittest.main()
