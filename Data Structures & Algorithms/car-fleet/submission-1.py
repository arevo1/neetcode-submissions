class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ## Variable approach
        cars = []
        for p, s in zip(position, speed):
            t = (target - p)/s
            cars.append((p,t))

        cars.sort(reverse = True)

        f = 0
        st = 0

        for p, t in cars:
            if t > st:
                f += 1
                st = t
        return f