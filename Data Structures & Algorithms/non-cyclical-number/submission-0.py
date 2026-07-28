class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        while n != 1:
            if n in visited:
                return False

            visited.add(n)

            digit_square_sum = 0

            while n > 0:
                digit = n%10
                digit_square_sum += digit * digit
                n //= 10

            n = digit_square_sum

        return True