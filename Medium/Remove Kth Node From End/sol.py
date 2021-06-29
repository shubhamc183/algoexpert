# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# T.C: O(N), multiple loop per Linked list
# S.C: O(1)
def removeKthNodeFromEnd1(head, k):
    l = 0
    curr = head
    while curr:
        l += 1
        curr = curr.next
    if l == k:
        head.value = head.next.value
    curr = head
    for _ in range(l - k - 1):
        curr = curr.next
    if curr.next:
        curr.next = curr.next.next

# T.C: O(N), single loop once per Linked list
# S.C: O(1)
def removeKthNodeFromEnd(head, k):
    first, second = head, head
    for _ in range(k):
        second = second.next
    if second is None:
        # k == length of the Linked List
        head.value = head.next.value
        head.next = head.next.next
        return
    while second.next:
        second = second.next
        first = first.next
    first.next = first.next.next
