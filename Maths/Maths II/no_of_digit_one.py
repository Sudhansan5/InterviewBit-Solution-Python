class Solution:
    def Solve(self,A):
        count = 0
        if A <= 0:
            return 0
        else:
            for i in range(1,A+1):
                while i:
                    res = i%10
                    if res == 1:
                        count += 1
                    i //= 10
        return count

    def solve(self,A):
        ans=0
        i=1
        while i <= A:
            divider = i*10
            ans += (A // divider) * i + min(max(A%divider-i+1,0),i)
            i *= 10
        return ans


if __name__ == '__main__':
    A=10
    B=Solution()
    print(B.Solve(A))
    print(B.solve(A))
