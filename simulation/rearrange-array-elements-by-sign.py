class Solution:
    def rearrangeArray(self, nums):
        n = len(nums)
        ans = [0] * n

        posIndex = 0
        negIndex = 1

        for num in nums:
            if num > 0:
                ans[posIndex] = num
                posIndex += 2
            else:
                ans[negIndex] = num
                negIndex += 2

        return ans
