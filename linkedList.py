##Author: Saad Ur Rehman
##LinkedList


class ListNode:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self, newhead = None):
        #self.head = newhead
        self.head = None
        self.tail = None

    def getHead (self):
        return self.head

    def getTail (self):
        return self.tail

    def getNext (self):
        return self.nextNode
    
    def setHead (self, newhead):
        self.head = newhead

    def setTail (self, newtail):
        self.tail = newtail
    
    def setNext (self, newNext):
        self.nextNode = newNext
##########################################################
##########################################################
    '''
    Complexity of addNewAtStart is O(1)
    if(self.head is None):
            tempNode = ListNode (data, None)       1
            self.tail = self.head = tempNode       1
    In this case, the complexity would be (1+1) = O(1)


        else:
            self.head = ListNode(data, self.head)   1
    In this case, the complexity would be (1) = O(1)
    '''

    def addNewAtStart (self, data):
        if(self.head is None):
            tempNode = ListNode (data, None)       #1
            self.tail = self.head = tempNode       #1
        else:
            self.head = ListNode(data, self.head)  #1
#############################################################
#############################################################

    '''
    Complexity of addNewAtEnd is O(1)

    def addNewAtEnd (self, data):
        if (self.head is None):
            self.addNewAtEnd(data)                  1
    In this case, the complexity would be (1) = O(1)

        else:
            self.tail.next = ListNode(data, None)   1
            self.tail = self.tail.next              1
    In this case, the complexity would be (1+1) = O(1)
    '''
    def addNewAtEnd (self, data):
        if (self.head is None):
            self.addNewAtEnd(data)                 #1
        else:
            self.tail.next = ListNode(data, None)  #1
            self.tail = self.tail.next             #1
##############################################################
##############################################################


    '''
    Assuming that 'n' is the length / size of linked list
    Complexity of this function is O(n). In its worst case, the while loop will have to iterate n times.
    Complexity would be:
        = (1 + 1 + n + ....)
        = O(n)

    Constants can be ignored in big-O complexity analysis. Therefore, the complexity is O(n)

    def removeNode (self, data):
        curNode = self.head                         1
        prevNode = None                             1

        while (curNode):                            n
            if (curNode.data == data):
                if (prevNode!=None):
                    prevNode.next = curNode.next    1

                    if(curNode!=None):
                        self.tail = prevNode        1

                else:
                    if (self.head==None):
                        self.tail = None            1
                    else:
                        self.head = self.head.next  1
            prevNode = curNode                      1
            curNode = curNode.next                  1
        '''
    def removeNode (self, data):
        curNode = self.head                     
        prevNode = None

        while (curNode):
            if (curNode.data == data):
                if (prevNode!=None):
                    prevNode.next = curNode.next

                    if(curNode!=None):
                        self.tail = prevNode

                else:
                    if (self.head==None):
                        self.tail = None
                    else:
                        self.head = self.head.next
            prevNode = curNode
            curNode = curNode.next
###############################################################
###############################################################


    '''
    Assuming that 'n' is the length / size of linked list

    Complexity of this function would be O(n) because it would run n times, in its worst case, before it completes.

    Complexity:  (1 + n + 1)
                = n + 2
                = O (n) 

    def isExist (self, data):
            curNode = self.head                     1

            while (curNode):                        n
                if (curNode.data == data):          
                    print("* * * Exists! * * *")    
                    return
                curNode = curNode.next              1
                    
            print ("* * * Does Not Exist * * * ")

    '''
    def isExist (self, data):
        curNode = self.head

        while (curNode):
            if (curNode.data == data):
                print("* * * Exists! * * *")
                return
            curNode = curNode.next
                
        print ("* * * Does Not Exist * * * ")
    ##################################################
    ##################################################

    '''
    Assuming that 'n' is the length / size of linked list

    Complexity of this function would be O(n) because it would run n times, in its worst case, before it completes.
    Complexity:  ( 1 + 1 + n + 1 + 1 )
                = ( 2 + n + 2)
                = (4 + n)
                = O(n)

    def findSize (self):
        tempNode = self.head          1
        size = 0                      1
        while (tempNode):             n
            size+=1                   1
            tempNode = tempNode.next  1
        return size
    '''
    def findSize (self):
        tempNode = self.head
        size = 0
        while (tempNode):
            size+=1
            tempNode = tempNode.next
        return size

    # Complexity for this would be O(n) as well since the while loop would have to iterate over the entire length of list in worst case.
    def displayList (self):
        if self.head is None:
            print ("* * * Empty List * * * ")
            return
        
        tempNode = self.head

        while tempNode:
            print (tempNode.data, " -->")
            tempNode = tempNode.next

def main():
    L1 = LinkedList()
    '''L1.addNewAtStart(1)
    L1.addNewAtStart(2)
    L1.addNewAtStart(3)
    L1.displayList()
    print ("-------")
    L1.removeNode(1)
    L1.displayList()
    L1.isExist(4)'''

if __name__ == "__main__":
    main()