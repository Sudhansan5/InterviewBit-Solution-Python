class Solution:
    def choose_2(self,n):
        return n*(n-1)//2

    def Solve(self,A,B):
        n=len(A)
        freq = [0 for _ in range(B)]
        for i in range(n):
            freq[A[i]%B] += 1

        total = self.choose_2(freq[0])

        if B%2 == 0:
            total += self.choose_2(freq[B//2])

        else:
            total += freq[B//2] * freq[B//2] + 1

        for i in range(1,B//2):
            total += freq[i] * freq[B-i]

        return freq,total


if __name__ == '__main__':
    A=[2,2,1,7,5,3]
    B=4
    C=Solution()
    print(C.Solve(A,B))
