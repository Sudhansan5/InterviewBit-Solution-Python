class Solution:
    def Solve(self,A,B,C,D,E,F,G,H):
        if H <= B or F >= D or G <= A or E >= C:
            return 0
        else:
            return 1

if __name__ == '__main__':
    A = 0
    B = 0
    C = 4
    D = 4
    E = 2
    F = 2
    G = 6
    H = 6
    I=Solution()
    print(I.Solve(A,B,C,D,E,F,G,H))
