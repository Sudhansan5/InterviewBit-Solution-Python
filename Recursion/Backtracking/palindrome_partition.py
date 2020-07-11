class Solution:
    def isPalindrome(self,A):
        return A == A[::-1]

    def check(self,A,i,aux):
        if i == len(A):
            self.ans.append(list(aux))
            return
        for j in range(i,len(A)):
            if self.isPalindrome(A[i:j+1]):
                aux.append(A[i:j+1])
                self.check(A,j+1,aux)
                aux.pop()

    def Solve(self,A):
        self.ans = []
        self.check(A,0,[])
        return self.ans

if __name__ == '__main__':
    A = 'aab'
    B = Solution()
    print(B.Solve(A))
