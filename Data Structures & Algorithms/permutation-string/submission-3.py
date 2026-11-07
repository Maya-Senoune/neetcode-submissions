class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = {}

        if len(s1) > len(s2):
            return False

        for c in range(len(s1)):
            count[s1[c]] = count.get(s1[c],0) + 1

        window = {}
        for r in range(len(s1)):
            window[s2[r]] = window.get(s2[r], 0) + 1
        if window == count:
            return True

        
        for r in range(len(s1), len(s2)):
            
            window[s2[r]] = window.get(s2[r], 0) + 1

            
            l = r - len(s1)
            window[s2[l]] -= 1
            if window[s2[l]] == 0:
                del window[s2[l]]

            if window == count:
                return True

        return False


