class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def size(self):
        return len(self.items)

# Пример использования
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
print(queue.dequeue())  # Вывод: 1

### Пример 1: Проверка пустой очереди
queue = Queue()
print(queue.is_empty())  # Вывод: True
queue.enqueue(10)
print(queue.is_empty())  # Вывод: False

### Пример 2: Добавление и удаление нескольких элементов
queue = Queue()
queue.enqueue('a')
queue.enqueue('b')
queue.enqueue('c')
print(queue.dequeue())  # Вывод: 'a'
print(queue.dequeue())  # Вывод: 'b'
print(queue.dequeue())  # Вывод: 'c'

### Пример 3: Работа с размером очереди
queue = Queue()
print(queue.size())  # Вывод: 0
queue.enqueue(5)
queue.enqueue(10)
print(queue.size())  # Вывод: 2
queue.dequeue()
print(queue.size())  # Вывод: 1

### Пример 4: Обработка попытки удаления из пустой очереди
queue = Queue()
print(queue.dequeue())  # Вывод: None (очередь пуста)
queue.enqueue(1)
queue.dequeue()
print(queue.dequeue())  # Вывод: None (очередь снова пуста)

