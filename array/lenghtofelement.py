class Solution(object):
    def lengthOfLastWord(self, s):
       list1=s.split()
       last=list1[len(list1)-1]
       return len(last)
        