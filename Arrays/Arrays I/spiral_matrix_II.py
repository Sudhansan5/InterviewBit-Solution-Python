class Solution:
    def Solve(self,A):
        ans=[[0]*A for _ in range(A)]
        T=0
        B=A-1
        L=0
        R=A-1
        direction=0
        num = 1
        while T <= B and L <= R:
            if direction == 0:
                for i in range(L,R+1):
                    ans[T][i] = num
                    num += 1
                T +=  1
                direction = 1
            elif direction == 1:
                for i in range(T,B+1):
                    ans[i][R] = num
                    num += 1
                R -= 1
                direction = 2
            elif direction == 2:
                for i in range(R,L-1,-1):
                    ans[B][i] = num
                    num += 1
                B -= 1
                direction = 3
            else:
                for i in range(B,T-1,-1):
                    ans[i][L] = num
                    num += 1
                L += 1
                direction = 0
        return ans

if __name__ == '__main__':
    A=3
    B=Solution()
    print(B.Solve(A))
