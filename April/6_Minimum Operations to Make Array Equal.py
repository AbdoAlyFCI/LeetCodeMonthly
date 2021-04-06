# 1551. Minimum Operations to Make Array Equal (Medium)
class Solution:
    def minOperations(self, n: int) -> int:
        ans = 0
        i = 0
        while i < n/2:
            ai = (2*i)+1
            ans += (n-ai)
            i+=1
        return ans

s = Solution()
print(s.minOperations(3))
