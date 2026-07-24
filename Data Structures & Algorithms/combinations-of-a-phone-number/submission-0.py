class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        result = []
        current = []

        def backtrack(index: int) -> None:
            if index == len(digits):
                result.append(''.join(current))
                return

            letters = mapping[digits[index]]

            for letter in letters:
                current.append(letter)
                backtrack(index + 1)
                current.pop()

        backtrack(0)
        return result
