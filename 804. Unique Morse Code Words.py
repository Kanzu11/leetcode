class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        l = set()
        morse = [".-","-...","-.-.","-..","."
,"..-.","--.","....","..",".-
--","-.-",".-..","--","-
.","---",".--.","--.-",".-."
,"...","-","..-","...-",".--
","-..-","-.--","--.."]
        for i in range(len(words)):
            m = []
            for j in range(len(words[i])):
                m.append(morse[ord(words[i][j])-97])
