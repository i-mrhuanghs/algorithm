#
# @lc app=leetcode id=641 lang=python3
#
# [641] Design Circular Deque
#

# @lc code=start
class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.n = k+1
        self.data = [0]*self.n
        self.front = 1
        self.rear = 0

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull() == True:
            return False
        self.data[self.front] = value
        self.front = (self.front+1)%self.n
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull() == True:
            return False
        self.data[self.rear] = value
        self.rear = (self.rear-1)%self.n
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty() == True:
            return False
        self.front = (self.front-1)%self.n
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty() == True:
            return False
        self.rear = (self.rear+1)%self.n
        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.isEmpty() == True:
            return -1
        return self.data[(self.front-1)%self.n]

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.isEmpty() == True:
            return -1
        return self.data[(self.rear+1)%self.n]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        if ((self.front-1)%self.n) == self.rear:
            return True
        return False

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        if self.front == self.rear:
            return True
        return False


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
# @lc code=end

