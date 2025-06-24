class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        n = []
        for I in range(len(names)):
            x = heights.index(max(heights))
            heights[x] = 0
            n.append(names[x])
        return n        
        
        
