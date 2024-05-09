class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        self.mask_unit_size = 32
        self.filter_mask = 0

    # внутренние команды:

    # предусловие: индекс pos больше нуля и меньше длины битовой маскиы
    # постусловие: возвращается бит из битовой маски по заданному индексу
    # так как эта функция внутренняя, то предполагается, что её будет всегда передаваться корректный индекс
    # поэтому мы не создаем отдельного статуса выполнения get_bitmask, а потенциально некорректную ситуацию 
    # оборачиваем в assert  
    def get_bitmask(self, pos):
        assert (0 <= pos) and (pos < self.filter_len) , 'Position is outside of bitfield bounds'
        bitMask = 1 << pos
        return bitMask
    
    # постусловие: заданый бит в битовой маске выставлен в единицу
    def set_bit(self, pos):
        bitMask = self.get_bitmask(pos)        
        self.filter_mask = self.filter_mask | bitMask
    

    #внутренние запросы:
    # постусловие: вычислено значение хеш-функции от заданной строки и ключа
    def general_hash(self, key, val):
        res = 0
        for c in val:
            code = ord(c)
            res = (res*key + code) % self.filter_len
        return res

    # постусловие: вычислено значение хеш-функции от заданной строки
    def hash1(self, str1):
        return self.general_hash(17, str1)

    # постусловие: вычислено значение хеш-функции от заданной строки
    def hash2(self, str1):
        return self.general_hash(223, str1)

    # постусловие: истинно, если заданный бит во внутренней битовой маске выставлен в единицу
    def is_bit_set(self, pos):
        bitMask = self.get_bitmask(pos)        
        return (self.filter_mask & bitMask) != 0


    # команды: 

    # постусловие: заданное значение добавлно в таблицу
    def add(self, str1):
        p1 = self.hash1(str1)
        p2 = self.hash2(str1)
        self.set_bit(p1)
        self.set_bit(p2)

    # запросы: 

    # постусловие: True, если элемен "найден" в таблице 
    def is_value(self, str1):
        p1 = self.hash1(str1)
        p2 = self.hash2(str1)        
        return self.is_bit_set(p1) and self.is_bit_set(p2)

    # добавление команды remove не целесообразно, ввиду того, что 
    # ввиду того, что модификация битовой маски может привести к 
    # ложноотрицательным срабатываниям
