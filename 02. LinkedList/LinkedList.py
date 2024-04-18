class LinkedList:
    
    # данный статус устанавливается при успешном смещении курсора к следующему элементу 
    # т.е. курсор указывл на не последний элемент
    RIGHT_DONE = 0
    # данный статус устанавливается если 
    # т.е. курсор указывал на не последний элемент при операции right
    RIGHT_ERR = 1

    # устанаваливается при успешном удалении элемента
    REMOVE_DONE = 0
    # устанаваливается при попытке удаления элемента из пустого списка
    REMOVE_ERR = 1

    # устанаваливается при успешном поиске элемента с заданным значением
    FIND_OK = 0
    # устанаваливается при если не удалось найти элемент с заданным значением
    FIND_ERR = 1

    # устанаваливается при успешном выполнении put_left 
    PUT_LEFT_OK = 0
    # устанаваливается при если не удалось выполнить put_left 
    PUT_LEFT_ERR = 1

    # конструктор
    # постусловие: возвращает созданный пустой односвязный список    
    def __init__(self):
        pass
    

    # команды

    # постусловие: курсор указывает на  первый элемент списка
    def head(self):
        pass

    # постусловие: курсор указывает на последний элемент списка
    def tail(self):
        pass

    # предусловие: курсор указывает на любой элемент списка, кроме последнего
    # постусловие: курсор указывает на следующий от первоначального положения курсора элемент 
    def right(self):
        pass

    # постусловие: в список добавлен элемент со значением value, следующий по отношению к положению курсора 
    def put_right(self, value):
        pass

    # предусловие: список непуст
    # постусловие: в список добавлен элемент со значением value, предыдущий по отношению к положению курсора 
    def put_left(self, value):
        pass

    # предусловие: список непуст
    # постусловие: узел, на который указывал курсор удален. курсор установлен на следующий элемент, при его наличии.
    # если удаленный элемент был последним, курсор устанавливается на предыдущий элемент
    def remove(self):
        pass

    # постусловие: список пуст, курсор не установлен ни на какой узел 
    def clear(self):
        pass

    # постусловие: в конец списка добавлен элемент со значением value
    def add_tail(self, value):
        pass

    # постусловие: значение элемента, на который указывает курсор, заменено на value
    def replace(self, value):
        pass

    # предусловие: в списке имеется хотя бы один элемент со значением value, находящийся справа от курсора
    # постусловие: курсор установлен на первый узел, находящийся справа от текущего узла и имеющий значение value
    def find(self, value):
        pass
    
    # постусловие: в списке отсутствуют элементы значением value
    def remove_all(self, value):
        pass


    # запросы

    # предусловие: список не пуст
    def get(self):
        pass

    def is_head(self):
        pass

    def is_tail(self):
        pass

    def is_value(self):
        pass

    def size(self):
        pass

    
    def get_remove_status(self):
        return self.remove_status

    def get_right_status(self):
        return self.right_status

    def get_find_status(self):
        return self.find_status

    def get_put_left_status(self):
        return self.put_left_status