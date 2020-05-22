class Solution:
    def Solve(self,A,B):
        tmp=[]
        for i in A:
            tmp.append(i)
        n=len(tmp)
        ans=0
        for i in range(n):
            if tmp[i] == '0':
                if i+B-1 < n:
                    for j in range(i,i+B):
                        if tmp[j]=='0':
                            tmp[j]='1'
                        else:
                            tmp[j]='0'
                    ans += 1
                else:
                    break

        for i in tmp:
            if i=='0':
                return -1
        return ans

A = "00010110"
B = 3
C = Solution()
print(C.Solve(A,B))
