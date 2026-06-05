
class Solution(object):
    def rotateRight(self, head, k):
        if head==None:
            return None
        n=1
        last=head
        while last.next!=None:
            n+=1
            last=last.next

        
        k=k%n
        if k==0:
            return head
        c=n-k
        count=1
        t=head
        while t!=None:
            if count==c:
                break
            count+=1
            t=t.next
        last.next=head
        res=t.next
        t.next=None
        return res
        
        