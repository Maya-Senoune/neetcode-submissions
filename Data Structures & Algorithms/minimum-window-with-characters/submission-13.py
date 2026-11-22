class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        need = Counter(t)
        missing = len(t)
        left = 0
        best = ""

        for right, ch in enumerate(s):

            if need[ch] > 0:
                missing -= 1
            need[ch] -=1 #decreasing it anyway in case of duplicates

            while missing == 0: #our window is valid
                if not best or ((right - left) + 1) < len(best):
                    best = s[left: right + 1]

                need[s[left]] += 1

                if need[s[left]] > 0:
                    missing += 1
                left += 1
        return best





            
                



            