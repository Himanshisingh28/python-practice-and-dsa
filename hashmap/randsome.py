class Solution(object):

    def fun(self, have, need):

        for ch in need:

            fneed = need[ch]
            fhave = have.get(ch, 0)

            if fhave < fneed:
                return False

        return True


    def canConstruct(self, ransomNote, magazine):

        have = {}
        need = {}

        for ch in ransomNote:
            need[ch] = need.get(ch, 0) + 1

        for ch in magazine:
            have[ch] = have.get(ch, 0) + 1

        return self.fun(have, need)