from math import sqrt
class Solution:
    def gcd(self,A,B):
        if A == 0:
            return B
        elif B == 0:
            return A
        elif A == 1 or B == 1:
            return 1
        else:
            return self.gcd(B%A,A)

    def Solve(self,A):
        n=len(A)
        A.sort(reverse=True)
        freq=[0 for _ in range(A[0]+1)]
        for i in range(n):
            freq[A[i]] += 1
        B=[0 for _ in range(n)]
        l=0
        for i in range(n):
            if freq[A[i]] != 0:
                for j in range(l):
                    x = self.gcd(A[i],B[j])
                    freq[x] -= 2
                B[l] = A[i]
                freq[B[l]] -= 1
                l += 1
            if freq[A[i]] > 0:
                i -= 1
        return B[:int(sqrt(n))]

if __name__ == '__main__':
    A = [2, 2, 2, 2, 8, 2, 2, 2, 10]
    B = Solution()
    print(B.Solve(A))
