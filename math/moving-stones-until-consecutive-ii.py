class Solution:
    def numMovesStonesII(self, stones):
        stones.sort()
        n = len(stones)

        # Maximum moves
        max_moves = max(
            stones[-1] - stones[1],
            stones[-2] - stones[0]
        ) - (n - 2)

        # Minimum moves - sliding window
        min_moves = n

        j = 0
        for i in range(n):
            while stones[i] - stones[j] + 1 > n:
                j += 1

            already = i - j + 1
            moves = n - already

            # Special case
            if already == n - 1 and stones[i] - stones[j] + 1 == n - 1:
                moves = 2

            min_moves = min(min_moves, moves)

        return [min_moves, max_moves]