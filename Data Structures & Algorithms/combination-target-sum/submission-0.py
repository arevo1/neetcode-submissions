class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        current = []

        def backtrack(index: int, remaining: int) -> None:
            if remaining == 0:
                result.append(current.copy())
                return

            if index == len(nums) or remaining < 0:
                return

            current.append(nums[index])

            backtrack(index, remaining - nums[index])

            current.pop()

            backtrack(index + 1, remaining)

        backtrack(0, target)

        return result