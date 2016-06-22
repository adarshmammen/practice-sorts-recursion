class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = list(s)
        ans = 0
        highest = 100000
        new = zip(["M","D","C","L","X","V","I"],[1000,500,100,50,10,5,1])
        flag = 0
        for i,ele in enumerate(l):
            for nums in new:
                if ele == nums[0] and nums[1]> highest:
                    if flag ==1:
                        flag=0
                        continue
                    ans-=highest
                    ans += nums[1] - highest
                    highest = nums[1]
                    flag = 1
                
                if ele == nums[0] and nums[1]<= highest:
                    if flag ==1:
                        flag=0
                        continue
                    ans+= nums[1]
                    highest = nums[1]
                    
        return ans

ob = Solution()
print ob.romanToInt("MMC")