import fractions
class Solution:
    def dp(self,A,i,num,total):
        n=len(A)
        if i > n-1 or num <= 0 or total <= 0:
            return
        elif num == 1 and A[i] == total:
            return [A[i]]
        else:
            include = self.dp(A,i+1,num-1,total - A[i])
            exclude = self.dp(A,i+1,num,total)
            if include:
                return [A[i]] + include
            elif exclude:
                return exclude

    def Solve(self,A):
        s,n = sum(A), len(A)
        gcd = fractions.gcd(s,n)
        num = n//gcd
        A.sort()
        for i in range(num, n//2+1,num):
            k=self.dp(A,0,i,s*i//n)
            if k:
                tmp=k[:]
                return [k,[i for i in A if not i in tmp or tmp.remove(i)]]
        return []

A=[1,7,15,29,11,9]
B=Solution()
print(B.Solve(A))
