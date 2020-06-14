class Solution:
    def Solve(self,A,B):
        while A >= 0 or B >=0:
            if A==B or A==0 or B == 0:
                return A+B
            elif A > B:
                A -= B
            else:
                B -= A

if __name__ == '__main__':
    A=5
    B=10
    C=Solution()
    print(C.Solve(A,B))
