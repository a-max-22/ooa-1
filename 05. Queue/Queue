class Queue:
    DEQUEUE_NIL = 0
    DEQUEUE_OK = 1
    DEQUEUE_ERR = 2
    
    def __init__(self):
        self.container = []
        self.dequeue_status = self.DEQUEUE_NIL

    #команды: 

    #постусловие: элемент помещён в очередь 
    def enqueue(self, item):
        self.container.append(item)

    #предусловие: очередь непуста
    #постусловие: элемент помещён в очередь
    def dequeue(self):
        if self.size() == 0:
            self.dequeue_status = self.DEQUEUE_ERR
            return None
        
        self.dequeue_status = self.DEQUEUE_OK
        result = self.container[0]
        del self.container[0]
        return result

    #запросы: 
    #возвращает количество элементов в очереди
    def size(self):
        return len(self.container)

    def get_dequeue_status(self):
        return self.dequeue_status
