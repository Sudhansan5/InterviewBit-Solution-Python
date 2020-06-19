class Solution:
    def isOverlap(self,A,B,C,D,E,F,G,H):
        if H <= B or F >= D or G <= A or E >= C:
            return False
        else:
            return True

    def Solve(self,A,B,C,D,E,F,G,H):
        area=0
        if self.isOverlap(A,B,C,D,E,F,G,H):
            area = (min(C,G) - max(A,E)) * (min(D,H) - max(B,F))
        return area

if __name__ == '__main__':
    A = 0
    B = 0
    C = 4
    D = 4
    E = 2
    F = 2
    G = 6
    H = 6
    I = Solution()
    print(I.Solve(A, B, C, D, E, F, G, H))
