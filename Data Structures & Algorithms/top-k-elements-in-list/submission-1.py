class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        d = {} #to store the numbers and how many times they occur

        for x in nums:
            d[x] = d.get(x,0) + 1

        freq = []

        for num, count in d.items():
            freq.append([count,num])
        freq.sort()


        result = []

        while len(result) < k: #because we only want the k most frequents
            result.append(freq.pop()[1])
        
        return result