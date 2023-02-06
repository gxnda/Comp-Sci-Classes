

class LinearQueue(object): 

    def __init__(self, qSize): #Parameters go into __init__
        #__VarName makes the variable invisible to the user (protection modifier)
        self.__q = [None] * qSize
        self.__front = 0
        self.__rear = -1 #enQueue is never called for -1, as it increases by 1 before calling it
        self.__size = 0
        self.__maxSize = qSize

    def enQueue(self, item):
        if self.isFull():
            return False
        else:
            self.__rear += 1
            self.__q[self.__rear] = item
            self.__size += 1
            return True

    def deQueue(self):
        if self.isEmpty():
            return None
        else:
            self.__size -= 1
            item = self.__q[self.__front]
            self.__front += 1
            return item
            

    def isFull(self):
        return self.__rear >= self.__maxSize-1 #Returns boolean

    def isEmpty(self):
        return self.__size == 0 #Returns boolean

    def __str__(self):
        output = ""
        for index in range(self.__front, self.__rear + 1):
            output += str(self.__q[index]) + " "
        return output[:-1]
        


class CircularQueue(object): 

    def __init__(self, qSize): #Parameters go into __init__
        #__VarName makes the variable invisible to the user (protection modifier)
        self.__q = [None] * qSize
        self.__front = 0
        self.__rear = -1 #enQueue is never called for -1, as it increases by 1 before calling it
        self.__size = 0
        self.__maxSize = qSize

    def enQueue(self, item):
        if self.isFull():
            return False
        else:
            self.__rear = (self.__rear + 1) % self.__maxSize
            self.__q[self.__rear] = item
            self.__size += 1
            return True

    def deQueue(self):
        if self.isEmpty():
            return None
        else:
            self.__size -= 1
            item = self.__q[self.__front]
            self.__front = (self.__front + 1) % self.__maxSize
            return item
            

    def isFull(self):
        return self.__size >= self.__maxSize #Returns boolean

    def isEmpty(self):
        return self.__size == 0 #Returns boolean

    def __str__(self):
        output = ""
        if self.__front <= self.__rear:
            for index in range(self.__front, self.__rear + 1):
                output += str(self.__q[index]) + " "
        else:
            for index in range(self.__front, self.__maxSize):
                output += str(self.__q[index]) + " "
            for index in range(0, self.__rear + 1):
                output += str(self.__q[index]) + " "
        return output[:-1]

BusStop = CircularQueue(5)


