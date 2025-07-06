class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=s.split()
        l=[]
        s=sorted(s,key=lambda x:x[-1])
        for i in s:
            l.append(i[:-1])
        return ' '.join(l)
