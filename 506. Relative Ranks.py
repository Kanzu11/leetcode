class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        n = score[:]
        b = [''] * len(n)
        for i in range(len(n)):
            c = n.index(max(n))
            n[c] = -1  
            if i == 0:
               b[c] = "Gold Medal"
            elif i == 1:
                b[c] = "Silver Medal"
            elif i == 2:
                b[c] = "Bronze Medal"
            else:
                b[c] = str(i + 1)
        return b
