class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        left = max(nums)
        right = sum(nums)

        while left < right:

            mid = (left + right) // 2

            subarrays = 1
            currentSum = 0

            for num in nums:

                if currentSum + num <= mid:
                    currentSum += num
                else:
                    subarrays += 1
                    currentSum = num

            if subarrays <= k:
                right = mid
            else:
                left = mid + 1

        return left