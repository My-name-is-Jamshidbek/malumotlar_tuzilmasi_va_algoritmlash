# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ll = []
        if list1:pass
        else:return list2
        if list2:pass
        else:return list1
        while True:
            if list1.val < list2.val:
                ll.append(list1.val)
                list1 = list1.next
                if list1 == None:
                    while list2:
                        ll.append(list2.val)
                        list2=list2.next
                    break
            else:
                ll.append(list2.val)
                list2 = list2.next
                if list2 == None:
                    while list1 != None:
                        ll.append(list1.val)
                        list1=list1.next
                    break
        rl = ListNode()
        for i in ll[::-1]:
            rl.val = i
            rl = ListNode(next = rl)
        return rl.next