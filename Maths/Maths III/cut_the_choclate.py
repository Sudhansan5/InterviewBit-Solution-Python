class Solution:
    def Solve(self,A,B):
        ans = A*B-1
        if ans % 2 == 1:
            return 1
        else:
            return 0

if __name__ == '__main__':
    A=1
    B=2
    C=Solution()
    print(C.Solve(A,B))
