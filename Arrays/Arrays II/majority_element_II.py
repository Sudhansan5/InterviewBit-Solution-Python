class Solution:  # > n/3
    def Solve(self,A):
        n=len(A)
        n1,n2=0,0
        c1,c2=0,0
        for i in range(n):
            n3=A[i]
            if c1 > 0 and c2 > 0:
                if n3 != n1 and n3 != n2:
                    c1-=1
                    c2-=1
                elif n3 == n1:
                    c1 += 1
                else:
                    c2 += 1
            elif c1 > 0:
                if n3 == n1:
                    c1 += 1
                else:
                    n2=n3
                    c2 += 1
            elif c2 > 0:
                if n2 == n3:
                    c2 += 1
                else:
                    n1 = n3
                    c1 += 1
            else:
                n1 = n3
                c1 += 1

        req_cnt = n//3 + 1
        c1=c2=0
        ans=[]
        for i in range(n):
            if A[i] == n1:
                c1 += 1
            if A[i] == n2:
                c2 += 1
        if c1 >= req_cnt:
            ans.append(n1)
        if c2 >= req_cnt:
            ans.append(n2)

        return ans

    def solve(self,A):
        m=len(A)
        n1,n2=0,1
        c1,c2=0,0
        for i in A:
            if i == n1:
                c1+=1
            elif i == n2:
                c2 += 1
            elif c1 == 0:
                n1= i
                c1=1
            elif c2 == 0:
                n2=i
                c2=1
            else:
                c1 -= 1
                c2 -= 1
        return [n for n in (n1,n2) if A.count(n) >= m//3+1]

if __name__ == '__main__':
    A=[1,1,1,3,3,2,2,2]
    B=Solution()
    print(B.Solve(A))
    print(B.solve(A))
