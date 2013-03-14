class LinkedList:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def prepend(self, value):
        ''' create a new node and put it second.   can't put it first,
            since that's 'self'.  But it's easy enough to correctly update
            the first and second values '''
        new_node = LinkedList(self.value)
        new_node._next = self.next
        self.next = new_node
        self.value = value

    def append(self, value):
        new_node = LinkedList(self.value)
        last_node = None
        for item in self:
            last_node = item
        last_node.next = new_node

    def peek(self):
        return self.value

    def __iter__(self):
        head = self
        yield head
        while head.next is not None:
            head = head.next
            yield head

    def __len__(self):
        result = 0
        for item in self:
            result += 1
        return result

    def __str__(self):
        return str(self.value)

if __name__ == '__main__':
    ll = LinkedList(4)
    ll.prepend(5)
    for item in ll:
        print item
    print len(ll)
