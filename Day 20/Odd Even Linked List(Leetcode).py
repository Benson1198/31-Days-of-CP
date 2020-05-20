class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        elif head.next == None or head.next.next == None:
            return head 
        elif head.next.next:
            yo = head 
            temp = head.next
            counter = 1
            while(head.next.next):
                follow = head.next
                counter += 1
                head.next = head.next.next
                head = follow
            if counter % 2 == 1 :
                follow.next = temp
            else:
                follow.next.next = temp
                follow.next = None
            return yo