import heapq
class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None

class Solution:
    def Solve(self,A):
        n=len(A)
        data=[]
        for i in range(n):
            tmp=[]
            count=0
            while A[i]:
                tmp.append((A[i].val,i,count))
                count+=1
                A[i]=A[i].next
            data.append(tmp)
        m=len(data)
        heap=[]
        for i in range(m):
            if data[i]:
                heapq.heappush(heap,data[i][0])

        tmp = dummy = ListNode(0)
        for i in range(m):
            while heap:
                p,q,r=heapq.heappop(heap)
                tmp.next=ListNode(p)
                tmp=tmp.next
                if r < len(data[r])-1:
                    heapq.heappush(heap, data[q][r+1])
        return dummy.next

    def print_node(self,A):
        if A:
            print(A.val)
            self.print_node(A.next)

root1=ListNode(1)
root1.next=ListNode(10)
root1.next.next=ListNode(20)

root2=ListNode(4)
root2.next=ListNode(11)
root2.next.next=ListNode(13)

root3=ListNode(3)
root3.next=ListNode(8)
root3.next.next=ListNode(9)

A=[root1,root2,root3]
B=Solution()
C=B.Solve(A)
B.print_node(C)
