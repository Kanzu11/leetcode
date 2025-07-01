class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        lst = []

        for x in arr2:
            while x in arr1:
                lst.append(x)
                arr1.remove(x)

        return(lst+sorted(arr1))
