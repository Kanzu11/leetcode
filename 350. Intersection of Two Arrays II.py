class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        i,j=0,0
        x=[]
        nums1.sort()
        nums2.sort()
        n1=len(nums1)
        n2=len(nums2)
        while i<n1 and j<n2:
            if nums1[i]<nums2[j]:
                i+=1
            elif nums1[i]>nums2[j]:
                j+=1
            else:
                x.append(nums1[i])
                i+=1
                j+=1
        return x
