class HashTable:    
    PUT_NIL = 0
    PUT_OK = 1
    PUT_ERR = 2

    def __init__(self, size, step):
        self.size = size
        self.step = step
        self.slots = [None] * self.size
        self.put_status = self.PUT_NIL

    
    #внутренние запросы:
    
    #возвращает значение хеш-функции
    def _hash_fun(self, value):
        hash = 0
        for s in value:
            hash = (hash + ord(s)) % self.size
        return hash


    #команды:
    
    #предусловие: ячейка для значения value свободна
    #постусловие: в таблицу помещено значение value
    def put(self, value):
        slot = self._hash_fun(value)
        if self.slots[slot] is not None:
            self.put_status = self.PUT_ERR
            return

        self.put_status = self.PUT_OK
        self.slots[slot] = value
         


    #запросы:
    #постусловие: возвращает True, если значение находится в таблице и False в противном случае    
    def is_in_table(self, value):
        slot = self._hash_fun(value)
        return self.slots[slot] == value
    
    def get_put_status(self):
        return self.put_status
