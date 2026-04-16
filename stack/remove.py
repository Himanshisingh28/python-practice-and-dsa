class Solution(object):
    def removeDuplicates(self, s):
        stack = []
        n = len(s)

        for i in range(0, n):
            if not stack:
                stack.append(s[i])
                continue

            if stack[-1] == s[i]:
                stack.pop()
                continue
            else:
                stack.append(s[i])

        res = ""
        while stack:
            res += stack[-1]
            stack.pop()

        return res[::-1]