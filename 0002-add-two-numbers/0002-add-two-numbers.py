# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        answer = ListNode()
        cur = answer
        upper = 0

        while l1 or l2 or upper:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0

            _sum = a + b + upper
            upper = _sum // 10
            cur.next = ListNode(val = _sum % 10)
            cur = cur.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return answer.next
