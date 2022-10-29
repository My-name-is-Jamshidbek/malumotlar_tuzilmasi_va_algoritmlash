# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        rl = ListNode()
        u = 0
        while head:
            u+=1
            rl.val = head.val
            rl = ListNode(next=rl)
            head = head.next
        head = rl.next
        if u%2 != 0:u=int(u/2)+1
        else:u=int(u/2)
        rl = ListNode()
        while u:
            u-=1
            rl.val = head.val
            rl = ListNode(next=rl)
            head = head.next
        return rl.next
