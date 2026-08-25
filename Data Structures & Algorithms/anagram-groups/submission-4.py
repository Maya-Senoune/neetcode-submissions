class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for string in strs:
            x = "".join(sorted(string))

            if x in d:
                d[x].append(string)
            else: d[x] = [string]

        return list(d.values())
