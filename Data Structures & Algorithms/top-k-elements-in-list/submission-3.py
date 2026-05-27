class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ## manual count freq_map
        ## initialize buckets
        ## bucket sort
        ## iterate thorugh buckets
        ## check for target length
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        buckets = [[] for _ in range(len(nums)+1)]
        #index -> freq
        #value -> list of nums
        for n, freq in freq_map.items():
            buckets[freq].append(n)
        res = []
        for freq in range(len(buckets)-1, 0, -1):
            for n in buckets[freq]:
                res.append(n)
                if len(res)==k:
                    return res