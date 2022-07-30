# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return constructList(readList(l1) + readList(l2))

def constructList(num):
    numList = []
    while num > 0:
        val = num % 10
        num = num // 10
        numList.append(val)
        
    prev = None
    head = ListNode()
    numList.reverse()
    for x in numList:
        head = ListNode(x, prev)
        prev = head

    return head

def readList(head):
    cur = head
    stopCondition = False
    sum = 0
    index = 0
    while not stopCondition:
        sum = cur.val * (10 ** index) + sum
        stopCondition = cur.next is None
        cur = cur.next
        index += 1 
    print(sum)
    return sum;

def printList(head):
    cur = head
    stopCondition = False
    while not stopCondition:
        print(cur.val)
        cur = cur.next
        stopCondition = cur.next is None

sol = Solution()
printList(sol.addTwoNumbers(constructList(342), constructList(465)))