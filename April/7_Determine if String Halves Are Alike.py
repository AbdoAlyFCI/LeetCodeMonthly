# 1704. Determine if String Halves Are Alike (Easy)
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        half = int(len(s)/2) 
        a = s[:half]
        b = s[half:]

        count = 0
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        for c in a:
            if c in vowels:
                count+=1

        for c in b:
            if c in vowels:
                count -=1

        return count == 0

solution = Solution()
s = "textbook"
print(solution.halvesAreAlike(s))