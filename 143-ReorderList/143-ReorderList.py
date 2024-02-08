
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        first = head

        while curr:
            
        second = prev
            temp1, temp2 = first.next, second.next

            first.next = second
            second.next = temp1
            first = temp1
        slow.next = None
        prev = None
            second = temp2



        


        
[1,2,3,4]
