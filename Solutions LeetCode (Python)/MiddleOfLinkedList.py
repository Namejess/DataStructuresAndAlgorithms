#Trouver le milieu d'une linked list et retourner head
# Pour le trouver, je le "traverse" avec .next tant que tail.next n'est pas NULL et j'incrémente un compteur
# Ensuite je divise FLOOR ce compteur ce qui me donne le milieu de la Llist
# Pour retourner le head, tant que le middleIndex est différent de 0, je next un dummy, puis je décrémente MiddleIndex

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        tail = head
        dummy = head
        counter = 1

        while tail.next != None:
            counter += 1
            tail = tail.next
            head = tail

        middleIndex = counter // 2

        while middleIndex != 0:
            dummy = dummy.next
            middleIndex -= 1

        return dummy









