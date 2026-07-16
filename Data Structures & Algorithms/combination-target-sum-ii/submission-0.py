class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        current = []

        def backtrack(start: int, remaining: int) -> None:
            if remaining == 0:
                result.append(current.copy())
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i]==candidates[i-1]:
                    continue

                if number > remaining:
                    break

                current.append(number)

                backtrack(i + 1, remaining - number)

                current.pop()

        backtrack(0, target)
        return result
