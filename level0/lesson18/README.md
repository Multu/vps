Хакер Эллиот (Мистер Робот) подбирает код для проникновения в хранилище данных "Стальная гора". Он собирается взломать систему климат-контроля, чтобы уничтожить все магнитные ленты Корпорации Зла. Помогите Эллиоту подобрать подходящий смарт-контроллер, который бы допускал потенциальную возможность взлома.

Для анализа поступает массив, в котором случайно перемешаны числа от 1 до N (без пропусков), N > 4.
Например, N=7 [1,3,4,5,6,2,7]

Хакерская утилита может делать только одну операцию: брать любые три идущие подряд элемента массива, и сдвигать их по кругу влево произвольное количество раз. Но эту операцию она может выполнять неограниченное количество раз.

Например:

[1,3,4,5,6,2,7] [5,6,2] -> [6,2,5] -> [2,5,6]

[1,3,4,2,5,6,7] [3,4,2] -> [4,2,3] -> [2,3,4]

[1,2,3,4,5,6,7] OK

Задача: определить, можно ли с помощью этой операции превратить массив в упорядоченный по возрастанию. Программа должна работать быстро (укладываться в 1 секунду при N ~= 10).

Функция

bool MisterRobot(int N, int [] data)
 
получает значение N и сам массив, и возвращает true, если этот массив возможно упорядочить вышеописанным способом.