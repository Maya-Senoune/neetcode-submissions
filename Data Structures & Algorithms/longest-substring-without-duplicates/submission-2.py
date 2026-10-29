class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left = 0
        sett = set()
        longest = 0
        

        for r in range(len(s)):
            while s[r] in sett:
                sett.remove(s[left])
                left = left +1
            currwindow = (r-left) + 1
            longest = max(currwindow,longest)
            sett.add(s[r])
        return longest