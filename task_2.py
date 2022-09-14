# Общие рекомендации:
# Системные методы python лучше вынести в отдельные функции:
#   метод для проверки на пустоту if len(self.queue) == 0
#   метод определения размеров очереди len(self.queue)
# Для лаконичности кода конструкции типа:
#   value = "test"
#   return value
# можно заменить на:
#   return "test"
# Общее описание "My little Queue" можно заменить на подробное описание доступного фнкционала очереди


"""
My little Queue
"""
from typing import Any


class Queue:
    def __init__(self):
        """
        начало очереди - слева (первый индекс списка)
        конец очереди - справа (последний индекс списка)
        """
        self.queue = []

    def enqueue(self, elem: Any) -> None:
        """
        Операция добавления элемента в конец очереди.
        :param elem: элемент, который следует добавить в очередь
        :return: None
        """
        # Существует другой системный метод, который просто вставляет элемент в конец списка
        self.queue.insert(0, elem)
        return None

    def dequeue(self) -> Any:
        """
        Вернуть элемент с начала очереди. Следует вернуть None, если элемента нет.
        :return: Снятый с начала очереди элемент
        """
        if len(self.queue) == 0:
            return None

        # Для корректной реализации данного метода необходимо извлекать первый элемент, а не последний
        value = self.queue.pop(len(self.queue)-1)
        return value

    def peek(self, ind: int = 0) -> Any:
        """
        Метод позволяет вам увидеть элемент в очереди, не удаляя его из очереди
        :param ind: индекс элемента с начала очереди
        :return: Просмотренный элемент
        """

        # Подсчет индексов начинается с 0, а количество элементов считается с 1.
        # например:
        #   list=["test"]
        #   len(list) будет равно 1
        # но при попытке извлечь list[1] получится ошибка, т.к нет элемента с индексом 1

        if ind < 0 or ind > len(self.queue):
            return None

        value = self.queue[ind]
        return value

    def clear(self) -> None:
        """ Очистить очередь. """
        if len(self.queue) == 0:
            return None

        self.queue.clear()
        return None
