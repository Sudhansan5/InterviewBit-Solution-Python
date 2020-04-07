class Solution:
    def Solve(self,A):
        stack=[]
        for i in A:
            if i==')':
                top=stack.pop()
                flag=True
                while top != '(':
                    if top == '+' or top == '-' or top == '*' or top == '/':
                        flag=False
                    top=stack.pop()
                if flag:
                    return 1
            stack.append(i)
        return 0
A='((a+b))'
B=Solution()
print(B.Solve(A))
