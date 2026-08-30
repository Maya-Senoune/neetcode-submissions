class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        setNum = set(nums)
        longest = 0

        for n in nums:

            if(n-1 not in setNum):
                length = 0
                while (n+length in setNum):
                    length += 1
                
                longest = max(length,longest)
        return longest