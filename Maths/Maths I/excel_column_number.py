class Solution:
    def Solve(self,A):
        count = 0
        for i in A:
            count = count*26 + (ord(i) - ord('A')) + 1
        return count

if __name__ == '__main__':
    A='AB'
    B=Solution()
    print(B.Solve(A))
