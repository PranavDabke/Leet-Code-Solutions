class Solution:
    def merge(self, intervals: List[List[int]]):

        # Step 1: Sort according to start time
        intervals.sort(key=lambda x: x[0])

        result = []

        for interval in intervals:

            # If result is empty OR no overlap
            if not result or result[-1][1] < interval[0]:
                result.append(interval)

            # Overlap found
            else:
                result[-1][1] = max(result[-1][1], interval[1])

        return result