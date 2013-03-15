''' linkedlist.py - a LinkedList class '''


class ListEmptyError(ValueError):
    ''' An error to raise when an operation fails because it needs
        a non-empty list (e.g.  pop()) '''
    pass


class LinkedList:
    ''' an object that represents an element and the head of a linked
        list. '''
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def prepend(self, value):
        ''' create a new node and put it second.   can't put it first,
            since that's 'self'.  But it's easy enough to correctly update
            the first and second values '''
        if self.isEmpty():
            self.value = value
        else:
            new_node = LinkedList(self.value)
            new_node.next = self.next
            self.next = new_node
            self.value = value

    def append(self, value):
        if self.isEmpty():
            self.value = value
        else:
            new_node = LinkedList(value)
            last_node = self.getLast()
            last_node.next = new_node

    def peek(self):
        return self.value

    def push(self, value):
        self.prepend(value)

    def pop(self):
        ''' return the first value in the list and
            remove it from the list. '''
        if self.isEmpty():
            raise ListEmptyError
        tmp = self.value
        if self.next is None:
            self.value = None
        else:
            result = self.next
            self.next = result.next
            self.value = result.value
        return tmp

    def clear(self):
        self.next = None
        self.value = None

    def isEmpty(self):
        return (self.value is None) and (self.next is None)

    def getLast(self):
        last_node = None
        for item in self:
            last_node = item
        return last_node

    def __iter__(self):
        ''' yield each of the list items in order '''
        head = self
        yield head
        while head.next is not None:
            head = head.next
            yield head

    def __len__(self):
        if self.isEmpty():
            return 0
        result = 0
        for item in self:
            result += 1
        return result

    def __str__(self):
        return "->".join([str(item.value) for item in self])
       #return str(self.value)

    def __add__(self, other):
        last_node = self.getLast()
        last_node.next = other
        return self

if __name__ == '__main__':
    ll = LinkedList(4)
    ll.append(5)
    for item in ll:
        print item
    print len(ll)
