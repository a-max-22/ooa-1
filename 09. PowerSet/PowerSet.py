class HashTable:    
    PUT_NIL = 0
    PUT_OK = 1
    PUT_ERR = 2

    REMOVE_NIL = 0
    REMOVE_OK = 1
    REMOVE_ERR = 2

    def __init__(self, size):
        self.size = size
        self.slots = [None] * self.size
        self.put_status = self.PUT_NIL
        self.remove_status = self.REMOVE_NIL
    
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
         
    #предусловие: в таблице имеется значение value
    #постусловие: из таблицы удалено значение value
    def remove(self, value):
        slot = self._hash_fun(value)
        if self.slots[slot] != value:
            self.put_status = self.REMOVE_ERR
            return

        self.put_status = self.REMOVE_OK
        self.slots[slot] = None


    #запросы:
    #постусловие: возвращает True, если значение находится в таблице и False в противном случае    
    def is_in_table(self, value):
        slot = self._hash_fun(value)
        return self.slots[slot] == value
    
    def get_put_status(self):
        return self.put_status

    def get_remove_status(self):
        return self.remove_status

    def size(self):
        size = 0
        for val in self.slots:
            if val != None: size += 1
        return size
    

class PowerSet(HashTable):
    UNION_NIL = 0
    UNION_OK = 0
    UNION_ERR = 0

    def __init__(self, max_size):
        super.__init__(max_size)
        self.max_size = max_size
        self.union_status = self.UNION_NIL
        self.last_intersection = PowerSet(max_size)
        self.last_union = PowerSet(max_size)
        self.last_difference = PowerSet(max_size)


    # команды: 

    # постусловие: создано новое множество, являющееся пересечением текущего и заданного множеств  
    def intersection(self, set2):
        self.last_intersection = PowerSet(self.max_size)
        for e in self.slots:
            if not set2.is_in_set(e): continue            
            self.last_intersection.put(e)
            if self.last_intersection.get_put_status() == self.PUT_OK: continue

    # предусловие: итоговый размер объединения не превышает максимальный размер текущего множества
    # постусловие: создано новое множество, являющееся объединением текущего и заданного множеств  
    def union(self, set2):
        self.last_union = PowerSet(self.max_size)
        for e in self.slots:
            self.last_union.put(e)
              
        for e in set2.slots:
            self.last_union.put(e)
            if self.last_union.get_put_status() == self.PUT_OK: 
                continue
            self.union_status = self.UNION_ERR
            return

        self.union_status = self.UNION_OK


    # постусловие: создано новое множество, являющееся разностью текущего и заданного множеств  
    def difference(self, set2):
        self.last_difference = PowerSet(self.max_size)
        for e in self.slots:
            if set2.is_in_set(e): continue
            self.last_difference.put(e)

    
    # запросы:

    # возвращает True, если set2 являтся подмножеством заданного множества    
    def issubset(self, set2):
        for e in set2.slots:
            if not self.is_in_set(e): 
                return False                
        return True

    # возвращает True, если элемент находится во множестве
    def is_in_set(self, value):
        return self.is_in_table(value) 

    def get_union_status(self):
        return self.union_status


    # возвращает множество, полученное в результате последней операции пересечения
    def get_intersection(self):
        return self.last_intersection
    
    # возвращает множество, полученное в результате последней операции объединения
    def get_union(self):
        return self.last_union

    # возвращает множество, полученное в результате последней операции разности
    def get_difference(self):
        return self.last_difference
