# need to do the same thing as pop where curr is index - 1
# Better strategy: keep 2 references with curr and previous
""" prev = None
 curr = self._first

 if self._first is None:
     return
 if curr.item == self._first.item and curr.next == None:
     self._first = None
 else:
     while curr is not None and curr.item != item:
         # because of lazy evaluation and if curr is none,
         # you don't need to check curr.item
         prev = curr
         curr = curr.next

     if curr is None or curr.next is None:
         prev.next = None
     else:
         prev.next = curr.next
 """

"""Sadia's implementation"
    
        prev = None
        curr = self._first
        
        while curr is not None and curr.item != item:
            prev = curr
            curr = curr.next
    
        # check if this list does not contain <item>:
            then curr is None
        # what if it's the first item 
        
        if curr: #same as saying if curr is not none
            if prev is None:
                self._first = self._first.next
            else:
                prev.next = prev.next.next 
    
    """


