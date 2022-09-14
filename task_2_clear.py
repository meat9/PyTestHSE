"""
Собственная реализация очереди. 
Поддерживаются операции добавления, удаления, получения элемента, определение текущего размера очереди, и метод, показывающий, пуста ли очередь или нет. 
Структура данных реализована на основе массива.
"""

from typing import Any


class Queue:
    def __init__(self):
        """
        начало очереди - слева (первый индекс списка)
        конец очереди - справа (последний индекс списка)
        """
        self.queue = []

    def empty(self):
        """Проверка очереди на пустоту"""
        return self.queue == []

    def enqueue(self, elem: Any) -> None:
        """
        Операция добавления элемента в конец очереди.
        :param elem: элемент, который следует добавить в очередь
        :return: None
        """
        self.queue.append(elem)
        return None

    def dequeue(self) -> Any:
        """
        Вернуть элемент с начала очереди. Следует вернуть None, если элемента нет.
        :return: Снятый с начала очереди элемент
        """
        if self.empty():
            return None
        return self.queue.pop(0)

    def peek(self, ind: int = 0) -> Any:
        """
        Метод позволяет вам увидеть элемент в очереди, не удаляя его из очереди
        :param ind: индекс элемента с начала очереди
        :return: Просмотренный элемент
        """
        if ind < 0 or ind > self.size()-1:
            return None
        return self.queue[ind]

    def clear(self) -> None:
        """ Очистить очередь. """
        self.queue.clear()
        return None

    def size(self):
        """ Размер очереди """
        return len(self.queue)
