class Solution:
    def canJump(self, nums: List[int]) -> bool:
        gp = len(nums) - 1

        for i in range(len(nums)-1,-1, -1):

            if i + nums[i] >= gp:
                gp = i

        if gp == 0:
            return True
        else:
            return False