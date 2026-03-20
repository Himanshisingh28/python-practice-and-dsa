def square(n):
    sum=0
    while n>0:
        d=n%10
        n=n//10
        sum=sum+d*d
    return sum
class Solution(object):
    def isHappy(self, n):
        slow=n
        fast=n
        while True:
            slow=square(slow)
            fast=square(square(fast))
            if fast==1:
                return True 
            if slow==fast:
                return False
            