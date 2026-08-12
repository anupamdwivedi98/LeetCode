class Solution:
    def numOfSubarrays(self, arr, k, threshold):
        window_sum = sum(arr[:k])
        count = 0

        if window_sum >= k * threshold:
            count += 1

        for i in range(k, len(arr)):
            window_sum += arr[i]
            window_sum -= arr[i - k]

            if window_sum >= k * threshold:
                count += 1

        return count