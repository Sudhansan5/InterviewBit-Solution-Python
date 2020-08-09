class Solution:
    def dp(self,A,i,_sum, size,res,aux):
        if aux[i][_sum][size]:
            return aux[i][_sum][size]

        if size == 0:

            return _sum == 0
        if i >= len(A):
            return False

        if A[i] <= _sum:
            res.append(A[i])
            if self.dp(A,i+1,_sum-A[i],size-1,res,aux):
                aux[i][_sum][size] = True
                return aux[i][_sum][size]
            res.pop()

        if self.dp(A,i+1,_sum,size,res,aux):
            aux[i][_sum][size]=True
            return aux[i][_sum][size]
        aux[i][_sum][size]=False
        return aux[i][_sum][size]


    def Solve(self,A):
        n=len(A)
        _sum = sum(A)
        dp=[[[False for _ in range(n+1)] for _ in range(_sum+1)] for _ in range(n+1)]
        ans=[]
        for i in range(1,n):
            if (_sum*i)%n == 0:
                curr_sum = (_sum*i)//n
                res=[]
                if self.dp(A,0,curr_sum,i,res,dp):
                    if res:
                        tmp=res[:]
                        return[res,[i for i in A if not i in tmp or tmp.remove(i)]]
        return []

A=[1, 7, 15, 29, 11, 9]
B=Solution()
print(B.Solve(A))
