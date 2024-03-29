#  coding = utf-8 

# @Time : 2022/10/5 19:16
# @Author : HJH
# @File : numDistinct.py
# @Software: PyCharm


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        i = 0
        j = 0
        # for i in range(len(s)):
        #     for j in range(len(t)):
        #         if t[j] == s[i]:
        #             j += 1
        while j < len(t):
            if t[j] == s[i]:
                j += 1
            i += 1
        else:
            return 0

    def numDistinct2(self, s: str, t: str) -> int:
        n1 = len(s)
        n2 = len(t)
        dp = [[0] * (n1 + 1) for _ in range(n2 + 1)]
        for j in range(n1 + 1):
            dp[0][j] = 1
        for i in range(1, n2 + 1):
            for j in range(1, n1 + 1):
                if t[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]
        # print(dp)
        return dp[-1][-1]


if __name__ == '__main__':
    so = Solution()

    s = 'baggabgabg'
    t = 'bag'

    print(so.numDistinct2(s, t))
