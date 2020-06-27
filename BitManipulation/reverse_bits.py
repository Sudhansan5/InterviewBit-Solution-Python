class Solution:
    def Solve(self,A):
        bit=32
        binary = bin(A)
        binary = binary.replace('0b','')
        reverse = binary[::-1]
        reverse += (bit-len(reverse)) * '0'
        return int(reverse,2)

if __name__ == '__main__':
    A=3
    B=Solution()
    print(B.Solve(A))
