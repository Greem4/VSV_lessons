![](../../commonmedia/header.png)

***

   

Многопоточность. Класс Thread. Способы создания потока
======================================================

### Класс Thread

Класс _Thread_ является основной точкой входа в многопоточное выполнение в Java. Именно на базе него (и его наследников) строится любое взаимодействие с потоками операционной системы, с которыми мы познакомились в рамках прошлого урока.

В него помещается логика, которая должна выполниться в новом потоке, через него же можно управлять состоянием потока – через статические (для управления текущим потоком) и нестатические (для управления другими потоками из текущего) методы.

Инструментарий данного класса мы разберем в одном из ближайших уроков, пока ограничимся вышесказанным и постараемся понять, как это использовать на практике.

Предлагаю для ознакомления следующие две статьи на metanit:

[https://metanit.com/java/tutorial/8.1.php](https://metanit.com/java/tutorial/8.1.php) - данная статья содержит краткое описание методов _Thread_. Но мы к ним еще вернемся позже и разберем более подробно. [https://metanit.com/java/tutorial/8.2.php](https://metanit.com/java/tutorial/8.2.php)

  

Из статей выше необходимо почерпнуть как минимум следующую информацию:

1\. _Thread_ реализует функциональный интерфейс _Runnable_;

2\. Логика (инструкции), которые должен выполнить поток, должны быть помещены в метод _run()_ интерфейса _Runnable_;

3\. Из пп. 1 и 2 следует, что _Runnable_ может быть описан лямбда-выражением, которое описывает ожидаемое поведение потока;

4\. Запустить новый поток можно посредством вызова метода _start()_ у объекта _Thread_;

5\. _Thread_ имеет конструктор, принимающий _Runnable_;

6\. Можно потребовать от текущего потока дождаться выполнения другого потока, если есть доступ к соответствующему объекту _Thread_. Для этого у _Thread_ существует метод _join()_;

> Учтите, что поток, **в котором** был вызван **join()** будет заблокирован, т.е. его выполнение приостановится, пока не завершится поток, **для которого** **join()** был вызван. Это очевидно, но, почему-то, об этом регулярно забывают.

7\. Получить объект, ассоциированный с текущим потоком выполнения можно с помощью статического метода _Thread.currentThread()_.

Безусловно, статьи содержат больше полезной информации: о том, как «усыпить» поток на время, как получить имя потока и, главное, содержат ряд различных примеров применения, что на данном этапе крайне важно.

### InterruptedException

Вы могли заметить в примерах статей выше массу _try-catch_, обрабатывающих _InterruptedException_.

Он срабатывает в ситуациях, когда поток, с которым происходит взаимодействие, был прерван, т.е. больше недоступен. Обычно данный эксепшн, как и большинство других checked-исключений, не срабатывает, но его обработка обязательна.

Поскольку на данном этапе наши задачи будут достаточно простыми и не будут предполагать обработку прерванного потока – не вижу ничего плохого в том, чтобы пробрасывать данное исключение в throws-блоке на самый верх программы, включая _main()_.

С теорией на сегодня все!

![](../../commonmedia/footer.png)

Переходим к практике:

### Задача 1

Напишите программу, отдельный (не main) поток которой пишет в консоль текущее время каждый две секунды, пока программа запущена.

### Задача 2

Опишите интерфейс, декларирующий метод, заполняющий двумерный массив заданных размеров случайными числами от 1 до 10. Создайте три реализации данного интерфейса:

1\. Заполняющую массив в однопоточном режиме;

2\. Заполняющую каждый одномерный массив отдельным потоком;

3\. Заполняющую каждую секцию каждого одномерного массива отдельным потоком. Оптимальный размер секции рекомендую определить опытным путем или сделать динамически-определяемым в зависимости от размера массива\*.

> Помните, что слишком большое количество потоков может привести с падению производительности – процессор будет тратить на переключение потоков больше времени, чем выполнять полезную работу в рамках потока.

Постарайтесь определить опытным путем, на каких размерах массива разница во времени выполнения становится существенной, а на каких объемах данных какая из реализаций показывает лучшие результаты.

### Задача 3(\*)

Уже на текущем этапе мы можем распараллелить какие-то действия с помощью многопоточности. Но иногда требуется выполнить определенную операцию в другом потоке и получить ее результат. Поскольку _Runnable_ не позволяет вернуть что-либо из метода – реализуйте класс/классы, которые позволят получать некий результат операции, выполненной в другом потоке.

Рекомендую использовать интерфейс _Callable_ для описания операции. Его метод имеет возвращаемое значение.

P.S. Ожидается собственный велосипед, а не использование _Future_ или _ExecutorService_. Пусть даже этот велосипед будет похож (или нет) на упомянутые механизмы. Если данные классы вам не знакомы - попытайтесь решить задачу прежде, чем гуглить, что за они.

### Задача 4(\*\*)

Решите [Задачу 3](#%D0%97%D0%B0%D0%B4%D0%B0%D1%87%D0%B0-3(*)), не используя _Thread.join()_.

P.S. Все еще ожидается велосипед.

  

Если что-то непонятно или не получается – welcome в комменты к посту или в лс:)

Канал: [https://t.me/+relA0-qlUYAxZjI6](https://t.me/+relA0-qlUYAxZjI6)

Мой тг: [https://t.me/ironicMotherfucker](https://t.me/ironicMotherfucker)

_Дорогу осилит идущий!_

[Next Lesson](../61/Mnogopotochnost-Sinhronizaciya-potokov-Ponyatie-monitora-Klyuchevoe-slovo-synchronized.md)
