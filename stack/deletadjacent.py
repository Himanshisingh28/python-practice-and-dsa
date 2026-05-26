class Solution(object):
    def removeDuplicates(self, s, k):
        stack=[]
        for ch in s:
            if stack and stack[-1][0]==ch:
                stack[-1][1]+=1
                if stack[-1][1]==k:
                    stack.pop()
            else:
                stack.append([ch,1])
        res=[]
        for ch, cnt in stack:
            res.append(ch*cnt)
        return "".join(res)