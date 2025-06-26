class Solution(object):
    def thirdMax(self, nums):
        k = nums
        r = []
        for i in range(len(k)):
            p = k.pop()
            if p not in r:
                r.append(p)
        r.sort(reverse=True)
        l = 0
        if len(r) < 3:
            l = max(r)
        else:
            l = r[2]
        return l
