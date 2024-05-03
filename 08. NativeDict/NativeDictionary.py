class NativeDictionary:
    SEEK_SLOT_NIL = 0
    SEEK_SLOT_OK  = 1
    SEEK_SLOT_ERR = 2

    FIND_NIL = 0
    FIND_OK  = 1
    FIND_ERR = 2

    PUT_NIL = 0
    PUT_OK  = 1
    PUT_ERR = 2

    GET_NIL = 0
    GET_OK  = 1
    GET_ERR = 2


    def __init__(self, size):
        self.size = size
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.step = 1
        
        self.seek_slot_status = self.SEEK_SLOT_NIL
        self.get_status = self.GET_NIL
        self.put_status = self.PUT_NIL
        self.find_status = self.FIND_NIL

    #внутренние запросы:
    def hash_fun(self, key):
        hash = 0
        for s in key:
            hash = (hash + ord(s)) % self.size
        return hash
    
    #предусловие: в хранилище есть свободное место
    #постусловие: найден индекс свободного элемента в хранилище 
    def __seek_slot(self, key):
        slot = None        
        slot = self.hash_fun(key)
        initialSlot = slot
        while self.slots[slot] is not None:
            if self.slots[slot] == key:
                self.seek_slot_status = self.SEEK_SLOT_OK
                return slot
            slot = (slot + self.step) % self.size
            if slot == initialSlot:
                self.seek_slot_status = self.SEEK_SLOT_ERR
                return None
            
        self.seek_slot_status = self.SEEK_SLOT_OK
        return slot

    def __get_seel_slot_status(self):
        return self.seek_slot_status
    
    
    #команды:

    #предусловие: в хранилище есть свободное место
    #постусловие: ключ и значение  помещено в словарь
    def put(self, key, value):
        slot = self.__seek_slot(key)
        if self.__get_seel_slot_status() != self.SEEK_SLOT_OK:
            self.put_status = self.PUT_ERR
            return
        
        self.put_status = self.PUT_OK
        self.slots[slot] = key
        self.values[slot] = value


    #предусловие: в словаре есть элемент с заданным ключом
    #постусловие: найден индекс элемента с заданным ключом
    def find(self, key):
        slot = self.hash_fun(key)
        initialSlot = slot
        while self.slots[slot] is not None:
            if self.slots[slot] == key:
                self.find_status = self.FIND_OK
                return slot
            
            slot = (slot + self.step) % self.size
            if slot == initialSlot:
                break
        
        self.find_status = self.FIND_ERR
           

    #предусловие: в словаре есть элемент с заданным ключом
    #постусловие: возврашено значение элемента с заданным ключом
    def get(self, key):
        slot = self.find(key)
        if self.get_find_status() == self.FIND_OK:
            self.get_status = self.GET_OK
            return self.values[slot]

        self.get_status = self.GET_ERR
    
    
    # запросы:
    
    # постусловие: возвращает True, если заданный ключ присутствует в словаре    
    def is_key(self, key):
        self.find(key)
        return self.get_find_status() == self.FIND_OK
    
    def get_get_status(self):
        return self.get_status
    
    def get_find_status(self):
        return self.find_status
    
    def get_put_status(self):
        return self.put_status
    
