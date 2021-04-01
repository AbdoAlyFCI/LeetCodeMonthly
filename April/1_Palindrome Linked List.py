# 234. Palindrome Linked List (Easy)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
        
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        currentNode = head
        nodeValuesList = []

        while currentNode != None:
            nodeValuesList.append(currentNode.val);
            currentNode = currentNode.next

        while head !=None:
            top = nodeValuesList.pop()

            if head.val != top :
                return False

            head = head.next

        return True


