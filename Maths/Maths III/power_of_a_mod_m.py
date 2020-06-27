import sys
sys.setrecursionlimit(10**6)

class Solution:
    def mod_exp(self,n,p,m):
        global ans
        if p == 1:
            return n%m
        ans = self.mod_exp(n,p//2,m)
        ans = (ans * ans)%m
        if p % 2 != 0:
            ans = (ans * n) % m
        return ans

if __name__ == '__main__':
    n=3
    p=17
    m=4
    A=Solution()
    print(A.mod_exp(n,p,m))
