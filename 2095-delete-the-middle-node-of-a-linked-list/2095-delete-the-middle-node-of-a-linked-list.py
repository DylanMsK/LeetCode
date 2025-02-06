# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        cur = head
        while cur is not None:
            cur = cur.next
            length += 1
        
        if length == 1:
            return None
        
        prev = None
        cur = head
        nxt = cur.next
        for i in range(length):
            if i == length // 2:
                prev.next = nxt
                break
            prev = cur
            cur = cur.next
            if cur is not None:
                nxt = cur.next
            
        return head