class ListNode:
    def __init__(self,val,next) -> None:
        self.val = val
        self.next = next
        
        
        
        
def traverse(head:ListNode):
    f = s = head # f is slowly pointer ,s is faster pointer
    while(s != None):
        s = s.next 
        if s != None and s.next != None:
            s = s.next
            f = f.next
    return f


