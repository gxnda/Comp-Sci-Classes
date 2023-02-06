# Stack object to implement LIFO ADT (Last in first out advanced data type)
# Author: Gabriel Lancaster-West
# Date: 10.1.23


class Stack:

    def __init__(self,maxSize):
        self.__stack = []
        self.__size = 0
        self.__maxSize = maxSize

    def isEmpty(self) -> bool:
        return self.__size == 0

    def isFull(self) -> bool:
        return self.__size == self.__maxSize

    def push(self, item) -> bool:
        '''Adds an item to the top of the stack.
        Returns boolean indicating success/fail.'''
        if self.isFull() == False:
            self.__stack.insert(0, item) #Can't use append()
            #when adding an item to a stack they are added to the front
            self.__size += 1
            return True
        else:
            return False

    def pop(self):
        '''Returns the top item from the stack. \nReturns None if empty.'''
        if self.isEmpty() == False:
            self.__size -= 1
            return self.__stack.pop(0)
        else:
            return None

    def peek(self):
        '''Returns top value of stack\nIf empty, returns None.'''
        if self.isEmpty() == False:
            return self.__stack[0]
        else:
            return None

    def size(self):
        """Returns size of stack"""
        return len(self.__stack)

    def __str__(self):
        output = ""
        for item in self.__stack:
            output += str(item) + "\n"
        return output

