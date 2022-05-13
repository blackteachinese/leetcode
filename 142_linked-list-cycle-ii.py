# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 进阶：你是否可以使用 O(1) 空间解决此题？

class Solution1:
    def detectCycle(self, head: ListNode) -> ListNode:
        # 方法一：哈希表记录访问过的节点，遍历链表，如果哈希表已存在节点，则有环。
        hashmap = set()
        while head:
            if head in hashmap:
                return head #有环
            hashmap.add(head)
            head = head.next
        return None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # 时间复杂度O（n）,空间复杂度O(m)
        # 方法二：双指针？一个指针每次跳一格，一个指针每次跳2格，如果两个指针相遇说明有环，如果一个指针为null则无环
        # 定义slow步数为s,fast步数为f
        # 因为fast永远比slow指针多走一步，可得公式一：f = 2s
        # 定义头结点到环入口的节点数量为a,环内节点数量为b
        # 当fast和slow相遇时,fast一定比slow多走n个环，可得公式 f - s = nb
        # 两个公式计算可得，当fast和slow相遇时,s=nb , f=2nb
        # 当相遇时s=nb,如果slow再走a步,slow就可以到环入口,（a+nb == 环入口），而从head走到环入口也是a步（0+a == 环入口）
        # 因此，如果当第一次相遇以后，让slow指针从当前位置向前每次走一步走，让另一个指针X从head向前每次走一步走，当他们一起走了a步，就会相遇在环入口节点。
        if not head : return None
        slow = fast = head
        while True:
            if not slow.next or not fast.next or not fast.next.next: # 无环
                return None
            slow = slow.next
            fast = fast.next.next
            if fast == slow: # 有环，第一次相遇
                break
        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast
