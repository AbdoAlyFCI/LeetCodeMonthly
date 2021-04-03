# 32. Longest Valid Parentheses
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        sList = list(s)
        stackOpen = list()
        
        for index,paren in enumerate(sList):
            if paren == '(':
                stackOpen.append(index)
                pass
            elif paren == ')':
                if len(stackOpen)> 0:
                    openIdx = stackOpen.pop()
                    sList[openIdx]= '_'
                    sList[index] = '_'
                pass
        
        ans = 0
        tmpCounter = 0
        for c in sList:
            if c == '_':
                tmpCounter +=1
            else:
                ans  = max(ans,tmpCounter)
                tmpCounter = 0
        ans  = max(ans,tmpCounter)
        return ans


s = Solution()

str = "(()"
ans = s.longestValidParentheses(str)
print(ans)
