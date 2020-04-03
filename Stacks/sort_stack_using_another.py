class Solution:
    # @param A : list of integers
    # @return a list of integers
    def top(self,A):
        n=len(A)
        return A[n-1]

    def isEmpty(self,A):
        return len(A)==0

    def pop(self,A):
        if self.isEmpty(A):
            return
        else:
            return A.pop()

    def solve(self, A):
        stack=[]
        while not self.isEmpty(A):
            tmp=self.top(A)
            self.pop(A)
            while not self.isEmpty(stack) and self.top(stack) > tmp:
                A.append(self.top(stack))
                self.pop(stack)
            stack.append(tmp)
        return stack
