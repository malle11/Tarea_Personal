class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 != 0:
            return False

        objetivo = total // 2

        dp = [False] * (objetivo + 1)
        dp[0] = True

        for numero in nums:
            for w in range(objetivo, numero - 1, -1):
                if dp[w - numero]:
                    dp[w] = True

            if dp[objetivo]:
                return True

        return dp[objetivo]