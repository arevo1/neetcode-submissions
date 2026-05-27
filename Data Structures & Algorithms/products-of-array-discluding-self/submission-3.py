import numpy as np
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_arr = {}
        suffix_arr = {}
        for idx, i in enumerate(nums):
            prefix_arr[idx] = np.prod([i for idx1, i in enumerate(nums) if idx1 < idx])
            suffix_arr[idx] = np.prod([i for idx1, i in enumerate(nums) if idx1 > idx])
        return [int(prefix_arr[i]*suffix_arr[i]) for i in range(len(nums))]
            