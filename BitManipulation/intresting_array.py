class Solution:
    def Solve(self,A):
        count=0
        for i in A:
            if i%2 != 0:
                count +=1

        if count % 2 != 0:
            return 'No'
        else:
            return 'Yes'

if __name__ == '__main__':
    A = [9, 17]
    B = Solution()
    print(B.Solve(A))
