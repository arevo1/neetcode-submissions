class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result, current_partition = [], []

        def is_palindrome(left:int, right:int) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False

                left += 1
                right -= 1

            return True

        def backtrack(start:int) -> None:
            if start == len(s):
                result.append(current_partition.copy())
                return

            for end in range(start, len(s)):
                if is_palindrome(start, end):
                    current_partition.append(s[start:end+1])
                    backtrack(end+1)
                    current_partition.pop()

        backtrack(0)
        return result