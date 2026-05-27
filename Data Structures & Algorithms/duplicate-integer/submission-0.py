class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_set = set(nums)
        for i in num_set:
            if nums.count(i)>1:
                return True
        return False