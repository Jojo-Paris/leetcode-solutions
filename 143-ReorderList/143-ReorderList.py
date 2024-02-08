
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        first = head

        while second:
            
        second = prev
            temp1, temp2 = first.next, second.next

        slow.next = None
        prev = None
            fast = fast.next.next
        
        curr = slow.next

        while fast and fast.next:
            slow = slow.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2

[1,2,3,4]
