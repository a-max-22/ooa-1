class BoundedStack:
    POP_NIL = 0
    POP_OK = 1
    POP_ERR = 2
    PEEK_NIL = 0
    PEEK_OK = 1
    PEEK_ERR = 2
    PUSH_NIL = 0
    PUSH_OK = 1
    PUSH_ERR = 2

    # внутренние вспомогательные методы
    
    # запросы:
    def _is_empty(self):
        return self.size() == 0

    # команды:
    def _set_initial_values(self):
        self.stack = []
        self.push_status = self.PUSH_NIL
        self.peek_status = self.PEEK_NIL
        self.pop_status = self.POP_NIL

    # конструктор
    # предусловие: размер стека - целое неотрицательное число
    # постусловие: возвращает созданный пустой стек    
    def __init__(self, size = 32):
        if (size <= 0):
            size = 32        
        self.stackSize = size
        self._set_initial_values()

    # метод создания стека
    # предусловие: размер стека - целое неотрицательное число
    # постусловие: возвращает созданный пустой стек    
    @classmethod
    def create_bounded_stack(bounded_stack_class, size = 32):
        if (size <= 0):
            return None
        else:
            return bounded_stack_class(size)


    # команды

    # предусловие: в стеке достаточно места для нового значения
    # постусловие: в стек добавлено новое значение     
    def push(self, value):
        if self.size() >= self.stackSize:
            self.push_status = self.PUSH_ERR 
            return
        self.stack.append(value)
        self.push_status = self.PUSH_OK 


    # предусловие: стек непуст
    # постусловие: из стека удален верхний элемент     
    def pop(self):
        if self._is_empty():
            self.pop_status = self.POP_ERR
            return
        self.pop_status = self.POP_OK
        self.stack.pop()

    # постусловие: из стека удалены все значения     
    def clear(self):
        self._set_initial_values()


    # запросы
    
    # предусловие: стек непуст
    def peek(self):
        if self._is_empty():
            self.peek_status = self.PEEK_ERR
            return
        self.peek_status = self.PEEK_OK
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def get_pop_status(self):
        return self.pop_status

    def get_peek_status(self):
        return self.peek_status
    
    def get_push_status(self):
        return self.push_status
