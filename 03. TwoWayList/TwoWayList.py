class Node:
    def __init__(self, prev, next, value):
        self.prev = prev
        self.next = next
        self.value = value


class ParentList:
    HEAD_OK  = 0
    HEAD_ERR = 1

    TAIL_OK  = 0
    TAIL_ERR = 1

    RIGHT_DONE = 0
    RIGHT_ERR = 1

    PUT_RIGHT_DONE = 0
    PUT_RIGHT_ERR = 1

    PUT_LEFT_DONE = 0
    PUT_LEFT_ERR = 1

    REMOVE_DONE = 0
    REMOVE_ERR = 1

    FIND_OK = 0
    FIND_ERR = 1

    PUT_LEFT_OK = 0
    PUT_LEFT_ERR = 1

    REPLACE_OK = 0
    REPLACE_ERR = 1

    GET_OK = 0
    GET_ERR = 1

    # конструктор
    # постусловие: возвращает созданный пустой односвязный список    
    def __init__(self):
        self.head = None
        self.tail = None
        self.node = None

        self.get_status = None
        self.replace_status = None
        self.find_status = None
        self.put_left_status = None
        self.put_right_status = None
        self.tail_status = None
        self.head_status = None
        self.right_status = None
        self.remove_status = None

    

    # команды

    # предусловие: список не пуст
    # постусловие: курсор указывает на  первый элемент списка
    def head(self):
        if self.is_value():
            self.node = self.head
            self.head_status = self.HEAD_OK
        else:
            self.head_status = self.HEAD_ERR

    
    # предусловие: список не пуст
    # постусловие: курсор указывает на последний элемент списка
    def tail(self):
        if self.is_value():
            self.node = self.tail
            self.tail_status = self.TAIL_OK
        else:
            self.tail_status = self.TAIL_ERR


    # предусловие: курсор указывает на любой элемент списка, кроме последнего
    # постусловие: курсор указывает на следующий от первоначального положения курсора элемент 
    def right(self):
        if not self.is_value():
            self.right_status = self.RIGHT_ERR
            return 
        
        if self.node == self.tail:
            self.right_status = self.RIGHT_ERR
            return 

        self.node = self.next
        self.right_status = self.RIGHT_OK

    # предусловие: список не пуст;
    # постусловие: в список добавлен элемент со значением value, следующий по отношению к положению курсора 
    def put_right(self, value):
        if not self.is_value():
            self.put_right_status = self.PUT_RIGHT_ERR
            return 
        
        newNode = Node(prev = self.node, next = self.node.next, value = value)
        self.node.next = newNode
        if self.is_tail():
            self.tail = newNode
        self.put_right_status = self.PUT_RIGHT_DONE

    # предусловие: список непуст
    # постусловие: в список добавлен элемент со значением value, предыдущий по отношению к положению курсора 
    def put_left(self, value):
        if not self.is_value():
            self.put_left_status = self.PUT_LEFT_ERR
            return 

        newNode = Node(prev = self.node.prev, next = self.node, value = value)
        self.node.prev.next = newNode
        self.node.prev = newNode
        
        if self.is_head():
            self.head = newNode

        self.put_right_status = self.PUT_LEFT_DONE

    
    # предусловие: список непуст
    # постусловие: узел, на который указывал курсор удален. курсор установлен на следующий элемент, при его наличии.
    # если удаленный элемент был последним, курсор устанавливается на предыдущий элемент
    def remove(self):
        if not self.is_value():
            self.remove_status = self.REMOVE_ERR
            return

        self.remove_status = self.REMOVE_DONE

        if self.is_head():
            self.clear()
            return
        
        if self.is_head():
            newCurrentNode = self.node.prev
            newCurrentNode.next = self.node.next
            self.tail = newCurrentNode
            self.node = newCurrentNode
            return

        newCurrentNode = self.node.next
        newCurrentNode.prev = self.node.prev
        self.node.prev.next = newCurrentNode

        return


    # постусловие: список пуст, курсор не установлен ни на какой узел 
    def clear(self):
        self.head = None
        self.node = None
        self.tail = None

    # постусловие: в конец списка добавлен элемент со значением value
    def add_tail(self, value):
        if not self.is_value():
            newNode = Node(None, None, value)
            self.head = newNode
            self.tail = newNode
            self.node = newNode
            return
        
        newNode = Node(prev = self.tail, next = self.tail.next, value = value)
        self.tail.next = newNode
        self.tail = newNode
        

    # предусловие: список непуст
    # постусловие: значение элемента, на который указывает курсор, заменено на value
    def replace(self, value):
        if not self.is_value():
            self.replace_status = self.REPLACE_ERR
            return
        
        self.node.value = value

    # предусловие: в списке имеется хотя бы один элемент со значением value, находящийся справа от курсора
    # постусловие: курсор установлен на первый узел, находящийся справа от текущего узла и имеющий значение value
    def find(self, value):
        if not self.is_value():
            self.find_status = self.FIND_ERR
            return
        
        node = self.node
        while (node != self.node.prev):
            if (node.value != value):
                node = node.next if node.next is not None else self.head                
                continue
            
            self.find_status = self.FIND_OK
            self.node = node
            return

        self.find_status = self.FIND_ERR
    
    # постусловие: в списке отсутствуют элементы значением value
    def remove_all(self, value):
        self.find(value)
        while (self.get_find_status() == self.FIND_OK):
            self.remove()


    # запросы

    # предусловие: список не пуст
    def get(self):
        if not self.is_value():
            self.get_status = self.GET_ERR 
            return None
        
        self.get_status = self.GET_OK
        return self.node.value 
        

    def is_head(self):
        return self.head == self.node

    def is_tail(self):
        return self.tail == self.node

    def is_value(self):
        return self.head is not None

    def size(self):
        node = self.head
        size = 0
        while node is not None:
            size += 1
        return size


    def get_head_status(self):
        return self.head_status

    def get_tail_status(self):
        return self.tail_status
    
    def get_right_status(self):
        return self.right_status

    def get_put_right_status(self):
        return self.put_right_status
    
    def get_put_left_status(self):
        return self.put_left_status

    def get_get_status(self):
        return self.get_get_status

    def get_remove_status(self):
        return self.remove_status

    def get_right_status(self):
        return self.right_status

    def get_find_status(self):
        return self.find_status

    def get_replace_status(self):
        return self.get_replace_status

    def get_put_left_status(self):
        return self.put_left_status

    def  get_find_status(self):
        return self.find_status


class LinkedList(ParentList):
    pass

class TwoWayList(ParentList):
    LEFT_DONE = 0
    LEFT_ERR = 1

    def __init__(self):
        super().__init__()
        self.left_status = None
    
    # предусловие: список непуст и курсор не находится в начале списка
    # постусловие: курсор перемещен к предыдущему элементу по отношению к текущему
    def left(self):
        if self.is_head():
            self.left_status = self.LEFT_ERR
            return

        self.node = self.node.prev
        self.left_status = self.LEFT_DONE


    def get_left_status(self):
        return self.left_status
