class Solution:
    def longestOnes(self, nums, k):
        left = 0
        zeros = 0
        max_length = 0

        for right in range(len(nums)):

            # Add current element
            if nums[right] == 0:
                zeros += 1

            # Too many zeros → shrink window
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            # Current window is valid
            max_length = max(max_length, right - left + 1)

        return max_length