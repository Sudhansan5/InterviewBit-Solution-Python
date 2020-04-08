from collections import deque
class Solution:
    def Solve(self,A):
        operators="+-*/"
        ans=deque()
        for i in A:
            if i not in operators:
                ans.append(int(i))
            else:
                a=ans.pop()
                b=ans.pop()
                if i == '+':
                    ans.append(b+a)
                elif i == '-':
                    ans.append(b-a)
                elif i == '*':
                    ans.append(b*a)
                else:
                    if b//a < 0 and b%a != 0:
                        ans.append(b//a+1)
                    else:
                        ans.append(b//a)
        return ans[0]
A = ["2", "1", "+", "3", "*"]
C = ["4", "13", "5", "/", "+"]
B=Solution()
print(B.Solve(A))
