class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data): 
        node = Node(data)
        if head==None :
            return node
        else :
            currentNode=head;
            while currentNode.next != None :
                currentNode=currentNode.next;
            currentNode.next=node
            return head

mylist= Solution()