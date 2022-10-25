# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        tortue = head
        lievre = head

        while lievre and lievre.next:
            tortue = tortue.next
            lievre = lievre.next.next

            if tortue is lievre:
                tortue = head
                while tortue != lievre:
                    tortue = tortue.next
                    lievre = lievre.next
                return tortue


# ===================SOLUTION 1======================

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        tail = head
        hasmap = {}
        counter = 0
        hashset = []
        i = 10

        if head is None:
            return "no cycle"

        if head.next is None:
            return "no cycle"

        while tail.next in hashset:
            hashmap = {counter: tail.val}
            hashset.append(tail.val)
            tail = tail.next
            counter += 1
            i -= 1

        if tail.val in hashset:
            pos = val_list.index(tail.val)
            return pos
