class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        set1 ={'q','w','e','r','t','y','u','i','o','p'}
        set2 = {'a','s','d','f','g','h','j','k','l'}
        set3 = {'z','x','c','v','b','n','m'}

        res = []
        for i in words:
            x = set(i.lower())
            if (x&set1 == x) or (x&set2 == x) or (x&set3 == x):
                res.append(i)
        
        return res
        
            
