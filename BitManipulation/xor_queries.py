class Solution:
    def Solve(self,A,B):
        n=len(A)
        ans=[]
        xor=[0 for _ in range(n)]
        count=[0 for _ in range(n)]
        xor[0] = A[0]
        if A[0] == 0:
            count[0] = 1

        for i in range(1,n):
            xor[i] = A[i] ^ xor[i-1]
            if A[i] == 0:
                count[i] = count[i-1] + 1
            else:
                count[i] = count[i-1]

        for i,j in B:
            l=i-1
            r=j-1
            global xor_query, count_zeros
            if l == 0:
                xor_query = xor[r]
                count_zeros = count[r]
            else:
                xor_query = xor[l - 1] ^ xor[r]
                count_zeros = count[r] - count[l-1]
            ans.append([xor_query, count_zeros])

        return ans

if __name__ == '__main__':
    A = [1, 0, 0, 0, 1]
    B = [[2, 4],
         [1, 5],
         [3, 5]]
    C = Solution()
    print(C.Solve(A, B))
