class Solution1:
    def reverseList(self, head: ListNode) -> ListNode:
        # 双指针pre、cur,从头开始遍历，指导cur.next为None，缓存cur的next,然后将cur的next指向pre，
        # 极限值
        if not head:
            return head
        # 初始化
        cur = pre = ListNode()
        pre.val = head.val
        # 不使用原有的node对象，会导致混乱，创建新的node对象作为链表的节点
        while head.next:
            head = head.next
            cur = ListNode()
            cur.val = head.val
            cur.next = pre
            pre = cur
        return cur

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 双指针pre、cur,从头开始遍历，指导cur.next为None，缓存cur的next,然后将cur的next指向pre，
        # 极限值
        if not head:
            return head
        # 初始化
        pre,cur = None,head
        # 使用原有的node对象
        while cur.next:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        cur.next = pre
        return cur