# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         rl = ListNode()
#         while head:
#             rl.val = head.val
#             rl = ListNode(next=rl)
#             head = head.next
#         return rl.next

m = [i for i in range(1,145)]
b = 0
o = 143
while True:
    print("?")