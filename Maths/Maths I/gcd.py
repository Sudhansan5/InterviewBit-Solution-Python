class Solution:
    def gcd(self,A,B):
        if A == 0:
            return B
        if B == 0:
            return A
        if A == 1 or B == 1:
            return 1
        for i in range(min(A,B),0,-1):
            if A%i == 0 and B%i == 0:
                return i

    def gcd_(self,A,B):
        if A == 0:
            return B
        elif B == 0:
            return A
        elif A == 1 or B == 1:
            return 1
        else:
            return self.gcd_(B%A,A)

if __name__ == '__main__':
    A=2
    B=3
    C=Solution()
    print(C.gcd(A,B))
    print(C.gcd_(A,B))
