# PyTestHSE
Тестовое задание

## Задание 1 (task_1.py)
Решить задание. Описание задания представлено в файле.  
Ограничений на решение задания нет.


## Задание 2 (task_2.py)
Студенту необходимо реализовать очередь. Ему дан следующий шаблон:
```python
from typing import Any


class Queue:
    def __init__(self):
        """
        начало очереди - слева (первый индекс списка)
        конец очереди - справа (последний индекс списка)
        """
        ...

    def enqueue(self, elem: Any) -> None:
        """
        Операция добавления элемента в конец очереди.
        :param elem: элемент, который следует добавить в очередь
        :return: None
        """
        ...

    def dequeue(self) -> Any:
        """
        Вернуть элемент с начала очереди. Следует вернуть None, если элемента нет.
        :return: Снятый с начала очереди элемент
        """
        ...

    def peek(self, ind: int = 0) -> Any:
        """
        Метод позволяет вам увидеть элемент в очереди, не удаляя его из очереди
        :param ind: индекс элемента с начала очереди
        :return: Просмотренный элемент
        """
        ...

    def clear(self) -> None:
        """ Очистить очередь. """
        ...
```
Дано решение студента в файле `task_2.py`.  
В задании студентом были допущены ошибки и он оказался в ступоре по решению задания :(  
Для проверки есть файл с тестами - `test_task_2.py`

От лица проверяющего необходимо:
1. В решении студента дать комментарии для самостоятельного исправления ошибок. 
2. Приложить комментарии, хорошие практики по рефакторингу кода (исправление кода без изменения функциональности)
3. Дать своё, эталонное решение текущей задачи.
