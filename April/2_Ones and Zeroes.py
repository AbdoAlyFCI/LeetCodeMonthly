# 474. Ones and Zeroes (Medium)
# This Solution by 01leetcode UPVOTE For Him Here --> https://leetcode.com/problems/ones-and-zeroes/discuss/701736/Python-DP-Solution-explained-with-example
# For More Explanation What this video --->  https://youtu.be/qkUZ87NCYSw
class Solution:
    def findMaxForm(self, strs: list, m: int, n: int) -> int:
        dp = [[ 0 ] * (n+1) for _ in range(m+1)]
        for s in strs:
            zeros, ones = s.count("0"), s.count("1")
            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    # dp[i][j] indicates it has i zeros and j ones, can this string be formed with those ?
                    dp[i][j] = max( 1 + dp[i - zeros][j- ones], dp[i][j] )
            # print(dp)
        return dp[-1][-1]


s = Solution()

strs = ["10","0001","111001","1","0"]



m = 5 # 0
n = 3 # 1

print(s.findMaxForm(strs,m,n))
