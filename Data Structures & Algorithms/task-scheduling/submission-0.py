class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequencies = Counter(tasks)

        max_freq = max(frequencies.values())

        max_count = sum(freq == max_freq for freq in frequencies.values())

        required_cycles = (max_freq - 1) * (n + 1) + max_count

        return max(len(tasks), required_cycles)