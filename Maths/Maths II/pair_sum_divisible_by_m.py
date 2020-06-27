class Solution:
    def choose_2(self,n,mod):
        return (n*(n-1)//2)%mod

    def Solve(self,A,B):
        n=len(A)
        mod=1000000007
        freq=[0 for _ in range(B)]

        #create a bucket of remainders
        for i in range(n):
            freq[A[i]%B] += 1

        # index 0 pair with itself
        ans = self.choose_2(freq[0],mod)
        i = 1
        j = B-1

        while i <= j:
            if i == j:
                ans += self.choose_2(freq[i],mod)
            else:
                ans += (freq[i] * freq[j]) % mod
            i += 1
            j -= 1
        return ans%mod


if __name__ == '__main__':
    A = [1, 2, 3, 4, 5]
    B = 2
    C = Solution()
    print(C.Solve(A,B))
