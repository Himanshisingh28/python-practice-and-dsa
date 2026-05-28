class Solution(object):
    def firstUniqChar(self, s):
        f={}
        for ch in s:
            f[ch]=f.get(ch,0)+1
        for i, ch in enumerate(s):
            if f[ch] ==1:
                return i
        
        return -1