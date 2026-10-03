from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda intervalo: intervalo[1])

        n = len(intervals)
        if n < 2:
            return 0

        quedan = 1
        fin_ultimo = intervals[0][1]

        for i in range(1, n):
            if intervals[i][0] >= fin_ultimo:
                quedan += 1
                fin_ultimo = intervals[i][1]

        return n - quedan