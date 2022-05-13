# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution1:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # 方法1：双指针l,r
        # 边界处理
        if not head: return None
        # 加空节点，简化逻辑
        empty = ListNode()
        empty.next = head
        l,r = empty,empty.next
        isEqual = False
        while r.next:
            r = r.next
            if l.next.val == r.val: # 重复
                isEqual = True
                continue
            else :# 不重复
                if isEqual: # 有一段重复
                    l.next = r #去掉中间节点
                    isEqual = False
                else:
                    # 遍历下一个节点
                    l = l.next
        # 最后一段有重复，也要去掉
        if isEqual:l.next = None
        return empty.next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # 简化逻辑，单指针遍历，记录重复值，while循环遍历一个个去掉
        if not head : return head
        dump = ListNode(0,head)
        cur = dump
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                x = cur.next.val # 记录重复值
                while cur.next and cur.next.val == x:
                    cur.next = cur.next.next
            else:
                cur = cur.next
        return dump.next


# [1,2,3,3,4,4,5]