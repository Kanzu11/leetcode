class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        keys = []
        values = []
        for i, j in matches:
            keys.append(i)
            values.append(j)

        a = keys + values
        l = {}

        for i in a:
            l[i] = 0

        for i in values:
            l[i] += 1

        y = []  
        z = [] 

        for i in l:
            if l[i] == 0:
                y.append(i)
            elif l[i] == 1:
                z.append(i)

        y.sort()
        z.sort()

        n = [y, z]
        return n