''' linkedlist.py - a linked list class.   Just for practice'''


class EmptyListError(RuntimeError):
    pass


class LinkedList:
    ''' A linked list class.  Just for practice'''
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def prepend(self, value):
        if self.value is None:
            self.value = value
        else:
            # need a new Node
            new_node = LinkedList(self.value)
            new_node.next = self.next
            self.value = value
            self.next = new_node

    def append(self, value):
        if self.value is None:
            self.value = value
        else:
            temp_head = self
            while temp_head.next is not None:
                temp_head = temp_head.next
            new_node = LinkedList(value)
            temp_head.next = new_node

    def __len__(self):
        if self.value is None:
            result = 0
        else:
            result = 1
            temp_head = self
            while temp_head.next is not None:
                result += 1
                temp_head = temp_head.next
        return result

    def is_empty(self):
        return self.value is None

    def peek(self):
        if not self.is_empty():
            return self.value
        else:
            raise EmptyListError()

    def pop(self):
        if self.is_empty():
            raise EmptyListError()
        result = self.value
        if self.next is not None:
            self.value = self.next.value
            self.next = self.next.next
        return result

    def str(self):
        sb = []
        if not self.is_empty():
            sb.append(self.peek())
        temp_head = self
        while temp_head.next is not None:
            sb.append(temp_head.value)
        return "->".join(sb)

    def __iter__(self):
        new_head = self
        while new_head is not None:
            yield new_head.value
            new_head = new_head.next


if __name__ == '__main__':

    import unittest

    class Test_LinkedList(unittest.TestCase):
        def test_simple(self):
            ll = LinkedList()
            ll.append(5)
            self.assertEqual(len(ll), 1)
            self.assertEqual(ll.peek(), 5)

        def test_append(self):
            ll = LinkedList()
            ll.append(5)
            ll.append(6)
            self.assertEqual(len(ll), 2)
            self.assertEqual(ll.peek(), 5)
            self.assertEqual(ll.next.peek(), 6)

        def test_prepend(self):
            ll = LinkedList()
            ll.prepend(5)
            self.assertEqual(len(ll), 1)
            self.assertEqual(ll.peek(), 5)
            ll.prepend(4)
            self.assertEqual(len(ll), 2)
            self.assertEqual(ll.peek(), 4)
            self.assertEqual(ll.next.peek(), 5)

        def test_zero_len(self):
            ll = LinkedList()
            self.assertEqual(len(ll), 0)
            ll.append(9)
            self.assertEqual(len(ll), 1)
            ll.prepend(8)
            self.assertEqual(len(ll), 2)

    unittest.main()
