class Solution:
    def Solve(self,A):
        n=len(A)
        pos_pdt=0
        neg_pdt=0
        ans=0
        for i in range(n):
            pre_pos_pdt=pos_pdt
            pre_neg_pdt=neg_pdt
            if A[i] == 0:
                pos_pdt=0
                neg_pdt=0

            if A[i] < 0:
                if pos_pdt:
                    neg_pdt = pre_pos_pdt * A[i]
                else:
                    neg_pdt = A[i]

                if neg_pdt:
                    pos_pdt = pre_neg_pdt * A[i]

            if A[i] > 0:
                if neg_pdt:
                    neg_pdt = pre_neg_pdt * A[i]

                if pos_pdt:
                    pos_pdt = pre_pos_pdt * A[i]
                else:
                    pos_pdt = A[i]

            ans = max(ans, pos_pdt)
        return ans if ans else max(A)



A=[4,2,-5,1]
B=Solution()
print(B.Solve(A))
