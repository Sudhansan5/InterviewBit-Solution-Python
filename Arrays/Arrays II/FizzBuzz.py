class Solution:
    def Solve(self,A):
        ans=[str(i) for i in range(1,A+1)]
        for i in range(1,A+1):
            if i % 3 == 0:
                ans[i-1] = 'Fizz'
            if i % 5 == 0:
                ans[i-1] = 'Buzz'
            if i % 3 == 0 and i % 5 == 0:
                ans[i-1] = 'FizzBuzz'
        return ans

if __name__ == '__main__':
    A=15
    B=Solution()
    print(B.Solve(A))
