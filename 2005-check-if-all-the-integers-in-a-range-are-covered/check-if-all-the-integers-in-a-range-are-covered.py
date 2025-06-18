class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        c=[]
        for x,y in ranges:
            for i in range(x,y+1):
                c.append(i)
        for i in range(left,right+1):
            if i not in c:
                return False
        return True