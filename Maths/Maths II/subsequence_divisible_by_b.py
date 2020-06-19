class Solution:
    def Solve(self,A,B):
        mod = 1000000007
        n=len(A)
        freq=[0 for _ in range(B)]
        for i in range(n):
            A[i] %= B
            freq[A[i]] += 1
        ans = 0

        for i in range(B):
            for j in range(i,B):
                rem = (B - (i+j)%B)%B

                if rem < j:
                    continue

                if i == j and rem == j:
                    ans += freq[i] * (freq[i] - 1) * (freq[i] - 2) // 6

                elif i == j:
                    ans += freq[i] * (freq[i]-1) * freq[rem] // 2

                elif i == rem:
                    ans + freq[i] * (freq[i] - 1) * freq[j] // 2

                elif j == rem:
                    ans += freq[j] * (freq[j] - 1) * freq[i] // 2

                else:
                    ans += freq[i] * freq[j] * freq[rem]

        return ans%mod

if __name__ == '__main__':
    A = [6, 1, 1, 4, 1, 5, 3]
    B = 2
    C=Solution()
    print(C.Solve(A,B))
