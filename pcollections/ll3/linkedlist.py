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
            result = 0
            for item in self:
                result += 1
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
        else:
            self.value = None
        return result

    def __str__(self):
        sb = []
        if self.is_empty():
            return ""
        temp_head = self
        while temp_head.next is not None:
            #print "appending...", temp_head.value
            sb.append(str(temp_head.value))
            temp_head = temp_head.next
        if temp_head.value is not None:
            sb.append(str(temp_head.value))
        return "->".join(sb)

    def __repr__(self):
        return self.__str__()

    def __iter__(self):
        new_head = self
        while new_head is not None:
            yield new_head
            new_head = new_head.next

    def get_last(self):
        result = None
        for item in self:
            result = item
        return result

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

        def test_pop(self):
            ll = LinkedList(4)
            ll.append(3)
            self.assertEqual(len(ll), 2)
            head = ll.pop()
            self.assertEqual(head, 4)
            self.assertEqual(ll.peek(), 3)
            self.assertEqual(len(ll), 1)
            head = ll.pop()
            self.assertEqual(head, 3)

        def test_iter(self):
            ll = LinkedList(4)
            ll.append(5)
            ll.append(6)
            count = 0
            for item in ll:
                count += 1
            self.assertEqual(count, 3)
            self.assertEqual(ll.peek(), 4)

        def test_get_last(self):
            ll = LinkedList(4)
            ll.append(5)
            ll.append(6)
            last = ll.get_last().peek()
            self.assertEqual(last, 6)
            self.assertEqual(ll.peek(), 4)

    import cmd

    class Shell(cmd.Cmd):
        def __init__(self):
            cmd.Cmd.__init__(self)
            self.prompt = "LinkedList test shell> "
            self.intro = '''Welcome to the LinkedList test shell.\nType ? for valid commands'''

        def do_test(self, line):
            unittest.main()

        def do_dbg(self, line):
            ll = LinkedList(4)
            ll.append(5)
            ll.append(6)
            import pdb
            pdb.set_trace()

        def do_EOF(self, line):
            print "Exiting."
            return True
        do_exit = do_EOF
        do_quit = do_EOF

    Shell().cmdloop()
