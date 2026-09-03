class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums = set(nums)
        longestSequence = 0

        for n in nums:
            if n-1 in nums:
                continue

            length = 1 #because its the beginning of a squence
            while (n+length) in nums:
                length +=1
                
            longestSequence = max(length,longestSequence)
        
        return longestSequence




