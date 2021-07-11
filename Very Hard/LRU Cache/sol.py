
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def set_head_to(self, node):
        # if head is node itself; don't do anything
        if self.head == node:
            return
        # if no node is present i.e linked list is empty
        elif self.head is None:
            self.head = node
            self.tail = node
        # if only one node is present and it's not the node(as checked in the first condition)
        elif self.head ==  self.tail:
            self.tail.prev = node
            self.head = node
            self.head.next = self.tail
        else:
            # has more than one node
            if self.tail == node:
                # if the node is tail
                self.remove_tail()
            node.remove_bindings()
            self.head.prev = node
            node.next = self.head
            self.head = node


    def remove_tail(self):
        # if linked list is empty
        if self.tail is None:
            return
        # if only one node is present in the linked list
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
        # when linked list has more than 1 node
        self.tail = self.tail.prev
        self.tail.next = None


class DoublyLinkedListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

    def remove_bindings(self):
        if self.next is not None:
            self.next.prev = self.prev
        if self.prev is not None:
            self.prev.next = self.next
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, maxSize=5):
        self._cache = {}
        self._max_size = maxSize
        self._current_size = 0
        self._list_of_most_recent = DoublyLinkedList()

    def getValueFromKey(self, key):
        if key not in self._cache:
            return None
        self._update_most_recent(self._cache[key])
        return self._cache[key].value

    def insertKeyValuePair(self, key, value):
        if key not in self._cache:
            if self._current_size == self._max_size:
               self._evict_least_recent()
            else:
                self._current_size += 1
            self._cache[key] = DoublyLinkedListNode(key, value)
        else:
            # replace key's new value in the node
            self._cache[key].value = value
        self._update_most_recent(self._cache[key])

    def getMostRecentKey(self):
        if self._list_of_most_recent.head is None:
            return None
        return self._list_of_most_recent.head.key

    def _evict_least_recent(self):
        del self._cache[self._list_of_most_recent.tail.key]
        self._list_of_most_recent.remove_tail()

    def _update_most_recent(self, node):
        self._list_of_most_recent.set_head_to(node)
