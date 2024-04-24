import ctypes

class DynArray:
    GET_NIL = 0
    GET_OK = 1
    GET_ERR = 2
    
    INSERT_NIL = 0
    INSERT_OK = 1
    INSERT_ERR = 2

    DELETE_NIL = 0
    DELETE_OK = 1
    DELETE_ERR = 2

    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self._make_array(self.capacity)
        self.getitem_status = self.GET_NIL
        self.insert_status = self.INSERT_NIL
        self.delete_status = self.DELETE_NIL

    # команды:

    # внутренние команды:
    
    # предусловие: новые размер хранилища - целое положительное число
    # постусловие: создано новое хранилище в массиве
    # так как данная функция - внутренняя, для неё не вводится отдельный статус выполнения
    # подразумевается, что ей будут переданы корректные параметры
    def _make_array(self, new_capacity):
        assert new_capacity > 0, "New array capacity is less than zero"
        return (new_capacity * ctypes.py_object)()

    # предусловие: новые размер хранилища - целое положительное число, большее, чем количество элементов в массиве
    # постусловие: размер хранилища изменен на новое значение
    # так как данная функция - внутренняя, для неё не вводится отдельный статус выполнения
    # подразумевается, что ей будут переданы корректные параметры
    def _resize(self, new_capacity):
        assert new_capacity >= self.size, "New array capacity is less than elements count"

        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    # постусловие: размер внутреннего хранилища увеличивается, если оно заполнено
    def _advance_count(self):
        if (self.count + 1 <= self.capacity):
            self.count += 1
            return                
        self._resize(2 * self.capacity)
        self.count += 1

    # постусловие: размер внутреннего хранилища уменьшается, если в нем много свободного места
    def _reduce_count(self):
        self.count -= 1        
        if (self.count >= (self.capacity // 2)):
            return
        
        new_capacity = int(self.capacity / 1.5)
        if new_capacity < 16:
            new_capacity = 16            
        self._resize(new_capacity)
 
    
    #внешние команды:

    # постусловие: в массив добавлен элемент itm в качестве последнего элемента
    def append(self, itm):
        if self.count == self.capacity:
            self._resize(2 * self.capacity)
        self.array[self.count] = itm
        self.count += 1
    
    # предусловие: индекс i больше или равен 0 и меньше количества элементов в массиве
    # постусловие: в массив на i-ю позицию  вставлен элемент itm
    def insert(self, i, itm):
        if (i < 0 or i > self.count ):
            self.insert_status = self.INSERT_ERR
            return 
        
        self.insert_status = self.INSERT_OK

        self._advance_count()
        lastIndex = self.count - 1
        
        for j in range(lastIndex, i, -1):            
            self.array[j] = self.array[j-1]            
        
        self.array[i] = itm        

        
    # предусловие: индекс i больше или равен 0 и меньше количества элементов в массиве
    # постусловие: i-й элемент удален из массива, элементы, находившиеся правее, смещены влево
    def delete(self, i):
        if (i < 0 or i >= self.count ):
            self.delete_status = self.DELETE_ERR
            return 
        
        self.delete_status = self.DELETE_OK
        lastIndex = self.count - 1        
        if (i == lastIndex):
            self._reduce_count()
            return            
        
        for j in range(i, lastIndex):            
            self.array[j] = self.array[j+1]
            
        self._reduce_count()


    # запросы: 
    
    #постусловие: возвращает количество элементов в массиве
    def __len__(self):
        return self.count
    
    #предусловие: индекс больше или равен нулю и меньше количества элементов в массиве
    #постусловие: возвращает элемент массива, с на заданной позиции
    def getitem(self, i):
        if i < 0 or i >= self.count:
            self.getitem_status = self.GET_ERR
            return None
        
        self.getitem_status = self.GET_OK
        return self.array[i]

    def get_getitem_status(self):
        return self.getitem_status
    
    def get_insert_status(self):
        return self.insert_status

    def get_delete_status(self):
        return self.delete_status
