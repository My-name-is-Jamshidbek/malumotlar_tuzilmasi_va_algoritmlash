# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self,l1,l2):
        s1 = ''
        while l1.next:
            s1+=str(l1.val)
            l1=l1.next
        s1+=str(l1.val)
        s2 = ''
        while l2.next:
            s2+=str(l2.val)
            l2=l2.next
        s2+=str(l2.val)
        s3 = str(int(s1[::-1])+int(s2[::-1]))
        r = ListNode()
        for i in s3:
            i = int(i)
            n = ListNode(val = i,next=r.next)
            r.next = n
        return r.next