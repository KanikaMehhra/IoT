# A single node of a singly linked list
class Node:
  # constructor
    def __init__(self, data , next=None): 
        self.data = data
        self.next = next
    
    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next

# A Linked List class with a single head node
class PlayerLinkedList:
    def __init__(self):  
        self.__head = None
        self.__tail=None
  
    #adds the new player to the linked list at the end.
    def insert(self, data):
        newNode = Node(data)
        if self.__head==None:
            self.__head=newNode
        else:
            self.__tail.next=newNode
        self.__tail=newNode
        self.__tail.next=self.__head
    
    def getHead(self):
        return self.__head

    #returns active player node to the game engine
    def getActivePlayerNode(self):
        if self.__head.getData().getActiveStatus():
            return self.__head
        else:            
            current = self.__head
            while(current.next):
                current = current.next
                if current.getData().getActiveStatus():
                    return current