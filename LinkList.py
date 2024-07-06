class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
    

class LinkedList:
    def __init__(self):
        self.head = None 
    

    def is_list_empty(self):
        return True if self.head is None else False
    
    def insert_at_the_begining(self, data):
        self.head = Node(data, self.head)
    
    def print_list(self):
        if self.is_list_empty():
            print("Empty List")
            return 
        itr = self.head
        llstr = ''
        while itr:
            llstr += f'{itr.data} --> '
            itr = itr.next
        print(llstr)
    
    def insert_at_end(self, data):
        if self.is_list_empty():
            self.insert_at_the_begining(data)
            return 
        
        # find the last element
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)
    

    def insert_values(self, *data_list):
        for data in data_list:
            self.insert_at_end(data)


    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        
        return count
    
    def remove_from_begining(self):
        if not self.is_list_empty():
            self.head = self.head.next
        else:
            print("Can't Remove From Empty List")
    

    def remove_from_end(self):
        if self.get_length() <= 1:
            self.remove_from_begining()
            return 
        
        itr = self.head
        while itr.next.next:
            itr = itr.next
    
        itr.next = None
        
    def remove_at(self, index):
        if index < 0  or index >= self.get_length():
            print("Invalid Index, ... ERROR")
            return 
        

        if index == 0:
            self.remove_from_begining()
            return 
        
    
        count = 0
        itr = self.head
        while count < index - 1:
            itr = itr.next
            count += 1
        itr.next = itr.next.next

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            print("Invalid Index Error")
            return 
        
        if index == 0:
            self.insert_at_the_begining(data)
            return 
    
        count = 0
        itr = self.head
        while count < index - 1:
            itr = itr.next
            count += 1
        
        itr.next = Node(data, itr.next)


    def remove_by_value(self, data):
        if self.is_list_empty():
            print("Can't Remove from empty list")
            return 

        if self.head.data == data:
            self.remove_from_begining()
            return 
        
        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                return 
            itr = itr.next
        print("Value Not Found")
    




def print_kth_node_data_of_ll(ll:LinkedList, k):
    size = ll.get_length()
    if k <= 0 or k > size:
        print("Invalid Kth Index, ERROR!!!")
        return 
    
    itr = ll.head
    idx = 0
    while idx < size - k: 
        itr = itr.next
        idx += 1
    
    print(f'Data of {k}th node = {itr.data}')

    
    














if __name__ == '__main__':
    ll = LinkedList()
    # # ll.insert_at_the_begining(40)
    # # ll.insert_at_the_begining(30)
    # # ll.insert_at_the_begining(20)
    # # ll.insert_at_end(10)
    # # ll.insert_at_end(20)
    # # ll.insert_at_end(30)
    # # ll.insert_at_end(40)
    # ll.insert_values(10, 20, 30, 40, 50, 60, 70, 80)
    # ll.print_list()
    # print(f"length of the list: {ll.get_length()}")
    # ll.remove_from_begining()
    # ll.print_list()
    # print(f"length of the list: {ll.get_length()}")
    # ll.remove_from_end()
    # ll.print_list()
    # ll.remove_at(5)
    # ll.print_list()
    # print("--"*10)
    # ll.insert_at(2, 35)
    # ll.print_list()
    # print("--"*10)
    # ll.remove_by_value(603)
    # ll.print_list()
    ll.insert_values(10, 20, 30, 40, 50, 60, 70)
    print_kth_node_data_of_ll(ll, 3)





    

