from collections import deque
# deque: 类似列表的容器，支持在两端快速的追加和删除元素


class Stack:
    def __init__(self) -> None:
        self.stack = deque()
        
    def push(self, data):
        """
        入栈
        :param data:
        :return:
        """
        # self.stack.append(data)
        self.stack.extend(data)
        
    def pop(self):
        """
        出栈
        :return:
        """
        return self.stack.pop()
    
    def size(self):
        """
        栈大小
        :return:
        """
        return len(self.stack)
    
    def is_empty(self):
        """
        判断是否是空栈
        """
        return self.size() == 0
    def clear(self):
        """
        清空栈
        """
        self.stack.clear()
    
class Stack2(Stack):
    def __init__(self) -> None:
        super().__init__()
    
    def pop(self):
        """
        出栈
        """
        super().pop()
        return self.stack.popleft()
    
    
if __name__ == '__main__':
    stack_FILO = Stack()
    
    stack_FILO.push(4)
    stack_FILO.push(3)
    stack_FILO.push(2)
    stack_FILO.push(1)
    
    print(stack_FILO.pop())
    print(stack_FILO.size())
    
    stack_FIFO = Stack2()
    stack_FIFO.push()
    