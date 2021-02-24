# https://www.algoexpert.io/questions/Remove%20Duplicates%20From%20Linked%20List

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# Time Complexity: O(n)
# Space Complexity: O(1)
def removeDuplicatesFromLinkedList(linkedList):
    head = linkedList
    current_ptr = linkedList
    while current_ptr and current_ptr.next:
        if current_ptr.value == current_ptr.next.value:
            current_ptr.next = current_ptr.next.next
        else:
            current_ptr = current_ptr.next
    return head
