# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Handle edge cases
        if not head or not head.next or k == 0:
            return head
        
        # Calculate the length of the linked list
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
        
        # Calculate the new head position after rotation
        k = k % length
        if k == 0:
            return head
        
        # Break the linked list into two parts
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next
        
        # Connect the end of the second part to the original head
        new_head = new_tail.next
        new_tail.next = None
        tail.next = head
        
        return new_head