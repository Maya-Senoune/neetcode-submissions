class Solution:
    def hasDuplicate(self, nums: List[list]) -> bool:
        hashset = set()

        for x in nums:
            if x in hashset:
                return True
            hashset.add(x)
        return False    