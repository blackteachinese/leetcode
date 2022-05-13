# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from platform import node


class Solution1: # 自己写的逻辑，使用三指针进行反转pre,cur,next
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        # method1: 
        if not head.next or left == right: return head
        # 2reverse left to right
        def reverse(first,second,rightnode):
            if first == rightnode or not second:
                return
            nextfirst = second
            nextsecond = second.next
            second.next = first
            reverse(nextfirst,nextsecond,rightnode)
        # 1find preleft nextright
        preleft = rightnode = head
        leftnode = nextright= None
        index = 1
        if left == 1:
            preleft = ListNode(0,head)
            leftnode = head
        else :
            while index+1 != left:
                preleft = preleft.next
                index+=1
            leftnode = preleft.next
        index = 1
        while index != right:
            rightnode = rightnode.next
            index+=1
        nextright = rightnode.next
        print(leftnode.val,rightnode.val)
        reverse(leftnode,leftnode.next,rightnode)
        # # 3 link preleft to right and left to nextright
        preleft.next,leftnode.next = rightnode,nextright
        return preleft.next if left == 1 else head

class Solution2: # 参考题解，简化逻辑
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        # method1: 
        if not head.next or left == right: return head
        # 2reverse left to right
        def reverse(pre,cur):
            if not cur:
                return
            next = cur.next
            cur.next = pre
            reverse(cur,next)
                    # 1find preleft nextright
        dumphead = ListNode(0,head) #!!!! 统一加上虚拟节点，避免复杂的分类讨论
        preleft = dumphead # preleft从虚拟节点开始遍历，index从0开始
        index = 0
        while index+1 != left:
            preleft = preleft.next
            index+=1
        leftnode = preleft.next
        rightnode = preleft
        while index != right:
            rightnode = rightnode.next
            index+=1
        nextright = rightnode.next
        # 切断子链表链接，让reverse子链表的逻辑变得简单很多
        preleft.next = None
        rightnode.next = None
        print(leftnode.val,rightnode.val)
        reverse(None,leftnode)
        # # 3 link preleft to right and left to nextright
        preleft.next,leftnode.next = rightnode,nextright
        return dumphead.next

class Solution: # 反转使用头插法，从头开始遍历，依次将每个元素插到头的前面，遍历完就完成revese
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head.next or left == right: return head
        dumphead = ListNode(0,head) #!!!! 统一加上虚拟节点，避免复杂的分类讨论
        preHead = dumphead # preleft从虚拟节点开始遍历，index从0开始
        indext = 0

        while indext+1 != left:
            preHead = preHead.next
            indext+=1
        p = preHead.next
        # 头插法
        indext = 0
        while indext < right - left:
            # 移除元素+修复链接
            removed = p.next
            p.next = p.next.next
            # 插入
            removed.next = preHead.next # 错误点： remove.next 后面跟preHead.next,而不是p
            preHead.next = removed
            indext += 1
            # print(dumphead.next)
            # print(preHead.val,p.val)
            # print('**')
        return dumphead.next