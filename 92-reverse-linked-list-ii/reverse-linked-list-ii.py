# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy_node = ListNode(0,head)
        Lprev = dummy_node
        curr = head
        prev = None
        for i in range(left-1):
            Lprev = curr
            curr = curr.next
        for i in range(right-left+1):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        Lprev.next.next = curr
        Lprev.next = prev
        return dummy_node.next

        