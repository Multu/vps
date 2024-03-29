#  Очереди

Очереди потому и называются очереди, что они работают как очереди: вход (добавление) происходит в хвост очереди, а выход (удаление) -- из её головы.

FIFO, first-in first-out -- первым пришёл, первым вышел
Очередь очевидно моделируется либо стандартным списком Python, либо изученным ранее связанным списком, так как мы можем добавлять в него элементы в нулевую позицию (в условный хвост) -- это стандартный метод enqueue(). Удаление элемента из головы, и его выдача, происходит методом dequeue().

```
qu = Queue()
qu.enqueue(1)
qu.enqueue(2)
qu.enqueue(3)
while qu.size() > 0:
    print(qu.dequeue())
```

### Задания.

6.1. В классе Queue нам понадобятся три метода: size() (количество элементов в очереди), enqueue(item) -- добавить элемент в хвост очереди, и dequeue(), которая возвращает элемент из головы очереди, удаляя его.

6.2. Оцените меру сложности для операций enqueue() и dequeue().

6.3. Напишите функцию, которая "вращает" очередь по кругу на N элементов.

6.4. Попробуйте реализовать очередь с помощью двух стеков.
