class Solution:
    def Solve(self,A):
        n=len(A)
        me , cnt = A[0], 1
        for i in range(1,n):
            if me == A[i] and cnt > 0:
                cnt += 1
            elif cnt == 0:
                me = A[i]
                cnt += 1
            elif me != A[i] and cnt > 0:
                cnt -= 1
        max_cnt = n // 2 + 1
        me_count = 0
        for i in range(n):
            if A[i] == me:
                me_count += 1
        if me_count >= max_cnt:
            return me
        return -1

if __name__ == '__main__':
    A=[3,3,2,2,4,4,4,4,4,4]
    B=Solution()
    print(B.Solve(A))
