class Solution:
    def characterReplacement(self, s, k):
        count = {}
        left = 0
        max_freq = 0
        max_length = 0

        for right in range(len(s)):
            # Add current character
            count[s[right]] = count.get(s[right], 0) + 1

            # Highest frequency character in window
            max_freq = max(max_freq, count[s[right]])

            # Number of replacements needed
            window_length = right - left + 1
            changes = window_length - max_freq

            # Too many replacements needed
            while changes > k:
                count[s[left]] -= 1
                left += 1

                window_length = right - left + 1
                changes = window_length - max_freq

            # Valid window
            max_length = max(max_length, right - left + 1)

        return max_length