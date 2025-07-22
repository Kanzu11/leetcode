class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        for i in range(len(matrix[0])):
            x = []
            for j in range(len(matrix)):
                x.append(matrix[j][i])
            res.append(x)
        return res
