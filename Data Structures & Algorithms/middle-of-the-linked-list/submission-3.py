# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr=head
        list = []

        while curr:

            list.append(curr)
            curr=curr.next

        return list[(len(list)//2)]