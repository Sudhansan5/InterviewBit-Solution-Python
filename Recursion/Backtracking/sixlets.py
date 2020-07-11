class Solution:
    def subseq(self,A,B,index,sum_, cnt):
        if index == len(A):
            if cnt == B:
                if sum_ <= 1000:
                    self.ans += 1
            return

        take = self.subseq(A,B,index+1, sum_+A[index], cnt+1)
        dont = self.subseq(A,B,index+1, sum_, cnt)
        return take and dont

    def Solve(self,A,B):
        self.ans = 0
        self.subseq(A,B,0,0,0)
        return self.ans


if __name__ == '__main__':
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    B = 5
    C = Solution()
    print(C.Solve(A,B))
