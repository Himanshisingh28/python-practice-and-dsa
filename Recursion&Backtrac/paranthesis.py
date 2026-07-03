class Solution(object):
    def fun(self,open,close,n,temp,res):

        if open==n and close==n:
            res.append("".join(temp))
            return
        if open < n:
            temp.append('(')
            self.fun(open+1, close, n, temp, res)
            temp.pop()
        if close<open:
            temp.append(')')
            self.fun(open, close+1, n, temp, res)
            temp.pop()
    def generateParenthesis(self, n):
        res=[]
        self.fun(0, 0, n, [], res)
        return res
        