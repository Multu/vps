# Поиск пути в графе (обход в ширину)

Теперь рассмотрим второй алгоритм -- это обход графа в ширину. Этому алгоритму теперь потребуется не стек, а очередь (можно воспользоваться наработками из соответствующего задания).

Алгоритм Breadth-first search (bfs) работает так:

0) Очищаем все дополнительные структуры данных: делаем очередь пустой, а все вершины графа отмечаем как непосещённые.

1) Выбираем текущую вершину X. Для начала работы это будет исходная вершина А. Фиксируем вершину А как посещённую.

2) Из всех смежных с X вершин выбираем любую (например первую) непосещённую.
Если выбранная вершина равна искомой, значит цель найдена, заканчиваем работу (остаётся только сформировать до неё путь, если это требуется).
Если таких вершин нету, проверяем очередь:
Если очередь пуста, заканчиваем работу (путь до цели не найден).
Иначе извлекаем из очереди очередной элемент, делаем его текущим X, и переходим обратно к данному п.2.

3) Помечаем найденную смежную вершину как посещённую, помещаем в очередь. Переходим к п.2.

Таким образом, данный алгоритм сперва заносит все ближайшие к текущему узлу вершины в очередь, а потом выбирает их по одной, и дальше также сканирует смежные с ними. В очереди у нас просто хранятся вершины, смежные с которыми вершины ещё не исследованы до конца.

Проблема данного подхода в том, что он не хранит, в отличие от поиска в глубину, текущий маршрут из исходной вершины к текущей.

Реализуйте поиск в ширину и придумайте способ хранения текущего пути.
В таком случае поиск в ширину будет гарантировать, что найденный путь будет оптимальным (минимальным) -- ведь мы, согласно концепции очереди, сначала сканируем все без исключения вершины, ближайшие к исходной вершине, затем -- удалённые на два ребра, затем -- на три, и т. д.

Расширьте класс SimpleGraph из прошлого занятия методом BreadthFirstSearch(), который получает в качестве параметров индексы в массиве vertex двух узлов (начальный и конечный) и возвращает список узлов, представляющий собой путь из начального узла в конечный, либо пустой список, если пути не существует.

На практике нередко используется модифицированная версия поиска в ширину на графе с весами. Это например случай, когда граф задаёт связи на карте между городами, и тут правильно задавать каждому ребру свой вес (расстояние в километрах). Ведь вполне может получиться так, что путь из трёх рёбер окажется в километрах экономнее, чем путь из одного ребра.

В таком случае мы берём не просто все узлы по порядку, а переупорядочиваем их по значениям весов. Тогда получить надо путь, пусть и не самый короткий в плане количества рёбер, а минимальный по сумме весов.

То есть на каждом уровне мы выбираем узлы способом, похожим на выбор в ширину, а сам поиск выполняем способом, похожим на поиск в глубину. В таком случае надо хранить текущий найденный путь с его оценкой, не прекращать процесс поиска, и при нахождении очередного пути, проверяем, не лучше ли он по своей оценки текущего.