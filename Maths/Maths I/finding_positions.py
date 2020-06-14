from math import log2, floor
class Solution:
    def Solve(self,A):
        log = floor(log2(A))
        return pow(2,log)

if __name__ == '__main__':
    A=10
    B=Solution()
    print(B.Solve(A))
