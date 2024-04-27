
class ParentQueue:
    REMOVE_FRONT_NIL = 0
    REMOVE_FRONT_OK = 1
    REMOVE_FRONT_ERR = 2

    GET_FRONT_NIL = 0
    GET_FRONT_OK = 1
    GET_FRONT_ERR = 2

    def __init__(self):
        self.container = []
        self.remove_front_status = self.REMOVE_FRONT_NIL
        self.get_front_status = self.GET_FRONT_NIL

    #команды:

    #постусловие: в очередь добавлен последний элемент
    def add_tail(self, item):
        self.container.append(item)

    #предусловие: хранилище непусто
    #постусловие: из хранилища удален первый элемент
    def remove_front(self):
        if self.size() == 0:
            self.remove_front_status = self.REMOVE_FRONT_ERR
            return 
        
        self.remove_front_status = self.REMOVE_FRONT_OK
        del self.container[0]
        return

    #предусловие: хранилище непусто
    #постусловие: функция вернула значение первого элемента из хранилища
    def get_front(self):
        if self.size() == 0:
            self.get_front_status = self.GET_FRONT_ERR
            return
        
        self.get_front_status = self.GET_FRONT_OK
        return self.container[0]


    #запросы:
    def size(self):
        return len(self.container)
    
    def get_get_front_status(self):
        return self.get_front_status
    
    def get_remove_front_status(self):
        return self.remove_front_status
        


class Queue(ParentQueue):
    pass


class Deque(ParentQueue):
    REMOVE_TAIL_NIL = 0
    REMOVE_TAIL_OK  = 1
    REMOVE_TAIL_ERR = 2

    GET_TAIL_NIL = 0
    GET_TAIL_OK  = 1
    GET_TAIL_ERR = 2

    def __init__(self):
        super().__init__()
        self.remove_tail_status = self.REMOVE_TAIL_NIL
        self.get_tail_status = self.GET_TAIL_NIL


    #команды:
    
    #постусловие: в очередь добавлен первый элемент
    def add_front(self, item):
        self.container.insert(0, item)

    #предусловие: хранилище непусто
    #постусловие: из хранилища удален последний элемент
    def remove_tail(self):
        if self.size() == 0:
            self.remove_tail_status = self.REMOVE_TAIL_ERR
            return
        self.remove_tail_status = self.REMOVE_TAIL_OK
        self.container.pop()

    #запросы:
    #предусловие: хранилище непусто
    #постусловие: возвращен последний элемент хранилища
    def get_tail(self):
        if self.size() == 0:
            self.get_tail_status = self.GET_TAIL_ERR
            return
        
        self.get_tail_status = self.GET_TAIL_OK
        return self.container[0]

    
    def get_get_tail_status (self):
        return self.get_tail_status

    def  get_remove_tail_status(self):
        return self.remove_tail_status
