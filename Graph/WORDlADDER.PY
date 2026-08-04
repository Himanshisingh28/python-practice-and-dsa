from collections import deque

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        f = set(wordList)

        if endWord not in f:
            return 0

        q = deque()
        q.append((beginWord, 1))

        if beginWord in f:
            f.remove(beginWord)

        while q:
            s, val = q.popleft()

            if s == endWord:
                return val

            for i in range(len(s)):
                ch = s[i]

                for j in range(97, 123):
                    c = chr(j)

                    if ch == c:
                        continue

                    new_word = s[:i] + c + s[i + 1:]

                    if new_word in f:
                        q.append((new_word, val + 1))
                        f.remove(new_word)

        return 0