class Solution:
    def longestKSubstr(self, s, k):
        n=len(s)
        left=0
        freq={}
        res=-1
        for right in range(n):
            freq[s[right]]=freq.get(s[right],0)+1
            while len(freq)>k:
                freq[s[left]]-=1
                if freq[s[left]]==0:
                    del freq[s[left]]
                left+=1
            if len(freq)==k:
                res=max(res,right-left+1)
                
        return res
        


        
class Solution(object):
    def totalFruit(self, fruits):
        left=0
        freq={}
        max_len=0
        for right in range(len(fruits)):
            fruit=fruits[right]
            freq[fruit]=freq.get(fruit,0)+1

            while len(freq)>2:
                freq[fruits[left]]-=1
                if freq[fruits[left]]==0:
                    del freq[fruits[left]]
                left+=1
            max_len=max(max_len,right-left+1)
        return max_len
        


















