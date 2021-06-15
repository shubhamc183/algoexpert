# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
    self.value = value
    self.next = None

# T.C: O(max(l1, l2)), l1 & l2 are length of linked list
# S.C: O(max(l1, l2))
def sumOfLinkedLists(linkedListOne, linkedListTwo, carry=0):
    if linkedListOne is None and linkedListTwo is None:
        return LinkedList(carry) if carry else None
    if linkedListOne != None:
        carry += linkedListOne.value
        linkedListOne = linkedListOne.next
    if linkedListTwo != None:
        carry += linkedListTwo.value
        linkedListTwo = linkedListTwo.next
    _ = LinkedList(carry % 10)
    _.next = sumOfLinkedLists(linkedListOne, linkedListTwo, carry // 10)
    return _
