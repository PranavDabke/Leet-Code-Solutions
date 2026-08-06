from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        dq = deque()      # Stores indices
        result = []

        for i in range(len(nums)):

            # Remove indices that are out of the current window
            while dq and dq[0] < i - k + 1:
                dq.popleft()

            # Remove smaller elements from the back
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            # Add current index
            dq.append(i)

            # Window of size k is ready
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result