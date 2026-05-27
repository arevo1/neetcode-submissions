import itertools
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {i:nums.count(i) for i in set(nums)}
        freq_map_sorted = dict(itertools.islice(sorted(freq_map.items(), key= lambda item: item[1], reverse= True),k))
        return list(freq_map_sorted.keys())