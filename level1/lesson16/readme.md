# Плохие комментарии

Плохие комментарии ещё вреднее, чем полное отсутствие комментариев. Они обманывают и сбивают с толку. Они формируют невыполнимые ожидания. Они подчас устанавливают устаревшие правила, которые не могут (или не должны) соблюдаться в будущем.

### 1. Неочевидные комментарии

Связь между комментарием и кодом, который он описывает, должна быть очевидной.

### 2. Бормотание

Не стоит лепить комментарии "на скорую руку" только потому, что вам кажется, что это уместно или этого требует процесс. Если уж вы решаете написать комментарий, не жалейте времени и напишите лучший из всех возможных комментариев.

### 3. Недостоверные комментарии

Иногда с самыми лучшими намерениями программист делает в комментариях заявления, неточные и не соответствующие истине

### 4. Шум

Также в программах нередко встречаются комментарии, не содержащие ничего, кроме "шума". Они лишь утверждают очевидное, не предоставляя никакой новой информации.

### 5. Неочевидные комментарии

### б. Позиционные маркеры

Некоторые программисты любят отмечать определенные позиции в исходных файлах.

```
//////////////
```

Но в общем случае они составляют балласт, от которого следует избавиться -- особенно от назойливой серии косых черт в конце. Взгляните на дело под таким углом: заголовки привлекают внимание только в том случае, если они встречаются не слишком часто. Используйте их умеренно и только тогда, когда они приносят ощутимую пользу.

### 7. Комментарии за закрывающей фигурной скобкой

Если у вас возникает желание прокомментировать закрывающие фигурные скобки, лучше постарайтесь укоротить свои функции.

```
} // завершение третьего вложенного цикла
```

### 8. Избыточные комментарии

Подчас даже простым функциям добавляются совершенно излишние длинные заголовочные комментарии, чтение которых займёт больше времени, чем чтение самого кода.

Избыточный комментарий не объясняет код, не раскрывает намерений, читается не проще, чем сам код. Более того, комментарий всегда уступает коду в точности и навязывает свою эту неточность взамен истинного формального понимания.

### 9. Слишком много информации

Не включайте в комментарии исторические дискуссии или описания подробностей, не относящиеся к делу.

### 10. Нелокальная информация

Комментарий должен описывать непосредственно находящийся поблизости код. Не излагайте информацию системного уровня в контексте локального комментария.

### 11. Обязательные комментарии

Правила стиля, требующие, чтобы каждая функция имела комментарий в формате фреймворка, или что каждая переменная должна быть помечена поясняющим её комментарием -- глупость. Такие комментарии только загромождают код, часто распространяют недостоверную информацию и вызывают общую путаницу и дезориентацию.

### 12. Закомментированный код

В программировании редко встречаются привычки более отвратительные, чем закрытие комментариями неиспользуемого кода. Никогда не делайте этого! Уже давно доступны хорошие системы контроля исходного кода, которые запоминают изменения в коде за нас. Вам уже не нужно закрывать их комментариями. Просто удалите ненужный код. Он никуда не исчезнет, честное слово.

### 13. Не используйте комментарии там, где можно использовать функцию или переменную

Короткие функции не нуждаются в долгих описаниях. Хорошо выбранное имя компактной функции, которая выполняет одну операцию, всегда лучше заголовка с подробным комментарием.

### 14. Задания

Найдите 15 своих плохих комментариев, и напишите по каждому, что вы сделали для их улучшения с указанием соответствующего пункта из занятия.