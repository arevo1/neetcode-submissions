class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(numbers):
            c = target - n
            if c in seen:
                return [seen[c]+1, i+1]
            seen[n] = i