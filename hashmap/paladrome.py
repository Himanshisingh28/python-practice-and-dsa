class Solution(object):
    def longestPalindrome(self, s):
        freq = {}
        res = 0

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

            if freq[ch] % 2 == 0:
                res += 2

        has_odd = any(count % 2 == 1 for count in freq.values())

        return res + (1 if has_odd else 0)