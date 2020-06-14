class Solution:
    def Solve(self,A):
        ans=""
        while A:
            A -= 1
            tmp = A%26
            A //= 26
            ans += chr(tmp+ord('A'))
        return ans[::-1]

if __name__ == '__main__':
    A=100
    B=Solution()
    print(B.Solve(A))
