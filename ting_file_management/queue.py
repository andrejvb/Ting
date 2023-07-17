from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self.__items = []

    def __len__(self):
        return len(self.__items)

    def enqueue(self, value):
        self.__items.append(value)

    def dequeue(self):
        if (self.__items) == 0:
            return None
        return self.__items.pop(0)
    
    def search(self, index):
        if index < 0 or index >= len(self.__items):
            raise IndexError('Índice Inválido ou Inexistente')
        return self.__items[index]
