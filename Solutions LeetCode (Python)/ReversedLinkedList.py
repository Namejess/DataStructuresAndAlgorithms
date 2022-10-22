# Le but est d'inverser une linked list.
# Pour se faire, on va initialiser plusieurs variables que l'on va utiliser pour : parcourir, changer de nodes, et retourner la llist finale
# Tant que current n'est pas NULL, on avance dans la liste, on changeant le next des noeuds par son précédent
# Comme chaque noeud suivant devient "précédent", une fois que l'on arrive à la fin au NULL, on peut retourner un head qui démarre au dernier noeud de la liste initiale, puis qui se poursuis vers le début de la liste initiale

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        current = head

        while current is not None:

            next = current.next
            current.next = prev
            prev = current
            current = next

            if current is None:
                head = prev

        return head


