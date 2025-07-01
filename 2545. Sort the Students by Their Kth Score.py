class Solution(object):
    def sortTheStudents(self, score, k):
        """
        :type score: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        s = sorted(score,key = lambda row : row[k])
        s.reverse()
        return s
