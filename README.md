# hello-world
Let's get started!


Я расскажу историю о том, как я и прекрасная Катя сделали вот это: 35.184.0.99 (это IP-адрес)

1. Я написала программу, которая говорит нам, что мы ввели: число или нет. Писала на python3. Думала, что написать анализ данных - самая трудная задача всей работы.


2. Нужно было вносить разрешаемые заголовки, разрешаемые методы запроса... Вкратце, нужно было вносить изменения в программу, чтобы сделать её сервером. Использовала фреймворк bottle. Поняла, что первая часть работы - цветочки. 


3. Нужно было написать веб-страничку, которая связывает пользователя, вводящего данные, и программу, которая обрабатывает данные и даёт пользователю ответ. Внутри этой странички прописывается ajax-запрос, вот с этим было трудновато, но в итоге, с помощью подключения библиотеки jQuery, удалось отправить ajax-запрос на наш сервер. 


4. Нужно было проверить, принимает ли сервер запросы. Для этого мы отправляли запрос из командной строки. В командной строке мы поняли, в каком формате нужно отправлять данные, чтобы сервер смог с ними работать. Нам нужно было это понять, чтобы потом так же прописать отправку входных данных в коде веб-странички.


5. Нужно было разместить нашу готовую страничку на веб-сервере, чтобы увидеть, может ли она отправлять запросы серверу python. Мы воспользовались веб-сервером Apache. С помощью командной строки мы поменяли путь, из которого Apache берёт файлик для показа, и по этому пути вставили написанную нами веб-страничку.

ВАЖНЫЙ МОМЕНТ: страничка, которую показывает Apach, по умолчанию находится по адресу 'localhost'. Соответственно, в программе-сервере мы сначала указывали, что слушаем localhost (на порте 8080). Страничка отправляла данные по тому же адресу, который слушает сервер.

6. После проверки взаимодействия сервера и страницы нужно было выложить их в открытый доступ. Веб-страничка должна быть доступна по какому-то адресу, а программа-сервер должна быть запущена всегда, чтобы всегда отвечать. Был скромный бюджет (точнее, его счёт был нулевой :)), поэтому мы решили воспользоваться Google Cloud Platform. Нужно зайти в консоль гугл (поймёте, что это оно, по синей шапке страницы). Там есть раздел Compute Engine, где можно создать свою виртуальную машину (VM). Это мы и сделали. Затем мы зашли внутрь машины (открыли в браузере), загрузили туда файлы (содержимое здешней папки folder). 


7. Нужен был веб-сервер, где бы лежала наша веб-страничка. На виртуальную машину мы установили веб-сервер Apache, посмотрели путь, по которому он выбирает файл для показа, и вставили туда свой index.html. На этом работа с веб-частью закончилась. 

8. Нужно было, чтобы программа-сервер работала постоянно, а не только тогда, когда её вручную запускаешь. 
Мы это делали командой python3 serverok.py, потом закрывали машину, и какое-то время страничка действительно работала. Мы провели эксперимент: запустили программу-сервер в виртуальной машине вечером, закрыли машину, поигрались, поняли, что сервер отвечает. На утро попробовали поиграться, а сервер уже не захотел нам отвечать:(( Грустно, конечно, но что поделаешь, надо было ему помочь быть всегда на связи с нами.
Мы это сделали с помощью команды "sudo nohup python3 serverok.py &". 


Забавная деталь: такая команда у нас всегда срабатывала со 2-го раза. В первый раз нам отказывали (проверяли серьёзность наших намерений :D), а во второй раз команда выполнялась. 

Эта команда заставляла программу работать, так сказать, в фоновом режиме, не зависеть от наличия человека-запускальщика.
При доработке запущенной программы приходилось останавливать её работу, это достигалось двумя командами: 

a) находим PID процесса с помощью команды ps axu | grep <имя программы> 
b) kill <PID процесса> (Может пригодиться sudo).


9. Готово! Сервер запущен, страничка доступна. Решила ради интереса создать файлик (тот самый list.txt), чтобы видеть запросы. Данные она получает, взаимодействуя с питоновской программой.


Вот она - краткая история наших увлекательных приключений) На самом деле было много пней, с которыми приходилось справлятья, чтобы всё работало как надо, но думаю, что для краткой истории вышесказанного вполне достаточно)

Буду рада, если этот рассказ и файлики папки "folder" помогут кому-то сделать что-то похожее или даже круче)
