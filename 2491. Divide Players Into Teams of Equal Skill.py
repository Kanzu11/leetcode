class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        print(skill[1])
        skill.sort()
        ans,i,j = 0,0,len(skill)-1
        t = skill[0]+skill[-1]
        while i < j :
            if skill[i]+skill[j] != t:
                return -1
            ans += skill[i]*skill[j]
            i+=1
            j-=1
        return ans
