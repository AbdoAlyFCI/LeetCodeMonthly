# 775. Global and Local Inversions (Medium)
class Solution:
    def isIdealPermutation(self, A: list) -> bool:

        globalI, localI = 0, 0

        current = 0
        while current < len(A):
            if current == A[current]:
                current += 1
                continue

            
            if A[current]-current == 1:
                localI += 1

            globalI += 1
            A[A[current]], A[current] = A[current], A[A[current]]

        return globalI == localI


s = Solution()

A = [2,0,1]

print(s.isIdealPermutation(A))