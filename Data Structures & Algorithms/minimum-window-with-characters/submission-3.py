
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        dict1 = {}
        shortest = float('inf')
        l = 0
        start = 0
        missing = len(t)

        if not t:
            return ""

        for char in t:
            dict1[char] = dict1.get(char, 0) + 1

        for r in range(len(s)):

            if s[r] in dict1:
                if dict1[s[r]] > 0:
                    missing -= 1

                dict1[s[r]] -= 1

            while missing == 0:
                if r - l + 1 < shortest:  # valid window
                    shortest = r - l + 1
                    start = l

                if s[l] in dict1:
                    dict1[s[l]] += 1

                    if dict1[s[l]] > 0:  # to see if we need it
                        missing += 1 

                l += 1

        if shortest == float('inf'):
            return ""
        else:
            
            return s[start:start + shortest]


        
        