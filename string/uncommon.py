class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        words=s1.split()+s2.split()
        result=[]
        for word in words:
            if words.count(word)==1:
                result.append(word)
        return result

        
       
        