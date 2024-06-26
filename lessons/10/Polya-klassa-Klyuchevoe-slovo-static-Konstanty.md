![](../../commonmedia/header.png)

***

   

Поля класса. Ключевое слово static. Константы
=============================================

#### Поля класса

Мы уже познакомились с таким синтаксисом как поле. Оно позволяет хранить определенную информацию внутри объекта, являясь, по сути, переменной уровня класса. Сегодня мы более подробно разберемся с особенностями этого синтаксиса.

Первое, что хотелось бы отметить – **дефолтные** (по умолчанию) значения полей. Если обычные переменные мы обязаны инициализировать явно (некоторые из вас уже столкнулись с ошибкой компиляции, если этого не сделать), то с полями класса все иначе.

Если мы создали поле класса и ни на каком этапе не задаем значение этого поля, Java не увидит в этом ошибки. По той простой причине, что она неявно дала значение каждому полю сразу при его объявлении, в зависимости от его типа:

· _byte, short, int, long_ – инициализируются значением 0;

· _char_ – инициализируется символом, код которого – 0. Данный символ нечитаем, но он есть. Вы можете прочесть больше, загуглив «_\\u0000_»;

· _double, float_ – значением по умолчанию будет 0.0;

· _boolean_ – будет инициализирован значение _false_;

· Абсолютно все _ссылочные типы_, включая хорошо известный нам _String_ – инициализируются значением _null_.

Если с примитивами все просто, то с _null_ мы ранее не сталкивались. Это ключевое слово, которое означает, что переменная ссылочного типа не содержит никакой ссылки на объект. Соответственно, обращение к полям и методам такой переменной завершится с ошибкой (исключением). Поэтому при работе с ссылочными типами достаточно часто используется проверка на _null_ вида (_object != null_).

Также стоит рассмотреть способы инициализации полей класса. Мы уже знакомы с инициализацией с помощью конструктора, также в статье на [metanit](https://metanit.com/java/tutorial/3.1.php) было упоминание о блоках инициализации (они нас не интересуют, поскольку данный функционал де-факто не используется).

Кроме этого, инициализацию полей мы можем производить в методах класса, если того требует логика нашего класса или приложения. Первичная инициализация в методе – достаточно узкий случай, а вот изменять значения в методе мы даже попробовали самостоятельно в практическом задании прошлого урока.

И последним, хоть и самым очевидным, способом первичной инициализации является инициализация при объявлении. Ровно также, как мы часто делаем с переменными. Инициализировать таким образом мы можем поля и примитивных, и ссылочных типов:

  

_public class Car {_

 _public int maxSpeed = 240;_

 _public String color = "Красный";_

 _public Counter mileage = new Counter("Пробег");_

_}_

Кроме того, мы можем использовать одни поля класса при инициализации других. Главное, чтобы инициализируемое поле было расположено ниже тех, которые используются для инициализации:

  

_public class FullName {_

 _public String firstName = "Иван";_

 _public String lastName;_

 _public String fullName = firstName + " " + lastName;_

}

  

При этом нет разницы, инициализированы использованные поля явно или нет. В нашем примере поле _fullName_ будет инициализировано значением "_Иван null_".

В любом случае, я не советую использовать инициализацию поля при объявлении, по крайней мере, на данном этапе. Зачастую такая логика приводит к излишней запутанности и неожиданным **багам**. Исключением являются **константы**, но об этом ниже.

#### Ключевое слово static

Мы уже встречались со _static’ом_ ранее, при знакомстве с методами, но использовали его без понимания того, что он делает и для чего нужен.

Данное ключевое слово можно применить к полю и методу (еще к **вложенному классу**, но не трогайте, это на Новый Год).

В обоих случаях данное ключевое слово будет означать, что поле/метод относится не к объекту класса, а непосредственно к классу. Т.е. нам не нужно создавать объект, чтобы использовать данное поле/метод.

Ярким примером _static_\-поля может быть поле _out_ класса _System_: _System.out_ – мы обращаемся к нему, не создавая объект класса _System_. Общий синтаксис обращения к статическому полю: _имя\_класса.имя\_поля_.

Наиболее распространенное применение статических полей – константы. В следующем подразделе мы разберем их подробнее.

Статические методы, в свою очередь, хорошо демонстрирует уже известный нам класс _Math_. Например: _Math.pow(2, 3)_. Здесь мы вызываем метод, не создавая объект класса _Math_. Общий синстаксис: _имя\_класса.имя\_метода(\[аргументы метода\])_.

Наиболее распространенное (и, практически, единственное) применение _static_\-методов – утилитарные методы, в которых объект не нужен. Например, математические операции, простейшие конвертеры и пр.

На самом деле, тема использования _static_\-методов намного глубже, чем кажется на первый взгляд и допустимость их использования тесно связано как с концепцией _ООП_, так и с особенностями реализации этой концепции в Java. Поэтому если с _static_\-полями мы почти полностью разберемся уже сегодня, то к _static_\-методам еще будем возвращаться несколько раз.

Немного о нюансах использования. С методами это не так критично (разберем чуть ниже), но с полями неграмотное использование _static_ может сыграть злую шутку. Рассмотрим на примере:

  

_public class Counter {_

 _public static int counter;_

_}_

_public static void main(String… args) {_

 _Counter counter1 = new Counter();_

 _Counter counter2 = new Counter();_

 _counter1.counter++;_

 _counter2.counter++;_

 _System.out.println(counter1.counter + " " counter2.counter);_

_}_

Вывод на консоль:

_2 2_

Поскольку _static_\-поля относятся именно к классу, а не объекту, значение такого поля будет общим на весь класс. По сути, код выше равноценен следующему:

  

_public class Counter {_

 _public static int counter;_

_}_

_public static void main(String… args) {_

 _Counter.counter++;_

 _Counter.counter++;_

 _System.out.println(Counter.counter + " " Counter.counter);_

_}_

Использование _static_\-методов имеет свои ограничения: мы не можем внутри статического метода обратиться к не статическому полю/методу, не создав экземпляр класса (использовать _this_ – тоже не можем). Т.е:

_public class SthClass {_

_public static void doSth() {_

 _doSth1();_

_}_

 _public void doSth1() {_

 _//Какая-то логика_

_}_

_}_

Приведет к ошибке компиляции. Чтобы подобный код заработал, нужно сделать следующее:

_public class SthClass {_

_public static void doSth() {_

 _SthClass sthObject = new SthClass();_

 _sthObject.doSth1();_

_}_

 _public void doSth1() {_

 _//Какая-то логика_

_}_

_}_

К слову, именно поэтому при первом знакомстве с методами я рекомендовал помечать их как _static_ – чтобы мы могли их использовать в статическом методе _main()_ до того, как изучим конструкторы.

Однако если вы в рамках статического метода создаете объект того же класса – почти гарантированно вы где-то свернули не туда. Исключения есть, но к моменту, когда они вас коснутся, использование _static_ вряд ли будет вызывать у вас какие-либо вопросы.

#### Константы

Мы уже знакомы с тем, как объявить переменную-константу внутри метода. Константы уровня класса достаточно похожи, для их объявления также используется ключевое слово _final_. Но есть и отличия.

Первое из них заключается в том, что инициализировать константное поле мы можем не только при объявлении, но также и в конструкторе, и в, упаси Господи, в блоке инициализации. Но для одной константы может быть использован только один способ инициализации. Не инициализировать константу вовсе – нельзя, это будет ошибкой компиляции.

Однако под константными полями обычно подразумеваются не просто _final_\-поля (в каком-то смысле, их можно назвать константами уровня объекта и они тоже имеют право на жизнь), а поля, помеченные как _static final_ – константы уровня класса.

В такие поля часто выносят литералы, которые не будут изменяться в ходе программы. Это могут быть какие-то строки, особенно, если одно строковое значение используется в рамках класса (или приложения) несколько раз, числа, особенно, если это какие-либо коэффициенты для расчетов и т.д.

Примером такой константы может быть

_public static final double PI = 3.14159265358979323846;_

в классе _Math_. Обратите внимание на нейминг: константы называют прописными буквами, слова разделяются символом ' \_'. Например: _SOMETHING\_CONSTANT_. Это сделано для того, чтобы отличать константные поля от обычных.

Если мы вспомним [Задачу 3](https://github.com/KFalcon2022/practical-tasks/blob/master/src/lesson4_cycles/Task3.java) (рисование прямоугольника) из урока про [циклы](/Cikly-11-13), в константы стоило бы вынести ' -', '|', ' '. Ведь если мы захотим нарисовать прямоугольник другими символами, заменить их будет проще в одном месте, чем искать по коду, особенно, если он разделен на методы.

Обращение к константе уровня класса ничем не отличается от обращения к обычному статическому полю. Кроме того, что изменить значение такого поля мы не сможем.

К слову, _final_\-методы тоже существуют, но в них смысл слова _final_ уже иной. Мы можем даже создавать _final-static_\-методы. Другой вопрос, что такое объявление избыточно, почему – разберем в уроке, посвященном **наследованию** в Java.

С теорией на сегодня все!

![](../../commonmedia/footer.png)

  

Переходим к практике:

#### Задача 1:

_Используя кодовую базу из задачи_ [https://github.com/KFalcon2022/practical-tasks/blob/master/src/com/walking/lesson6\_methods/Task3.java](https://github.com/KFalcon2022/practical-tasks/blob/master/src/com/walking/lesson6_methods/Task3.java) _вынести строковые и символьные литералы в константы. Попробуйте нарисовать прямоугольник, используя "==" для каждой единицы длины и "||" – для каждой единицы ширины._

_Также попробуйте записать в константу переменную scanner. Упростится ли использование сканера внутри методов чтения с клавиатуры?_

  

#### Задача 2:

_Для задачи_ [https://github.com/KFalcon2022/practical-tasks/tree/master/src/com/walking/lesson8\_classes\_objects](https://github.com/KFalcon2022/practical-tasks/tree/master/src/com/walking/lesson8_classes_objects) _реализуйте неизменность поля названия у класса Counter. Ведь очень странно, если мы можем менять название счетчика по ходу выполнения программы, не так ли?_

#### Задача 3:

_Используя задачу_ [https://github.com/KFalcon2022/practical-tasks/blob/master/src/com/walking/lesson7\_varargs\_overloading/Task5.java](https://github.com/KFalcon2022/practical-tasks/blob/master/src/com/walking/lesson7_varargs_overloading/Task5.java) _(можете сделать на основе своего решения, но для наглядности удобства новых возможностей рекомендую взять за основу решение по ссылке):_

_1\. Вынесите поиск простых чисел в отдельный класс._

_2\. Реализуйте возможность вывода на экран суммы N первых простых чисел, где N – число, введенное пользователем с клавиатуры;_

_3\. Вынесите нужные вам переменные в поля класса. Если необходимо – сделайте их константами уровня класса или объекта. Помните, константа ссылочного типа гарантирует неизменность ссылки, а не содержимого объекта. Массив – ссылочный тип._

_Примечание: это одна задача, а не различные варианты:)_

  

Если что-то непонятно или не получается – welcome в комменты к посту или в лс:)

Канал: [https://t.me/+relA0-qlUYAxZjI6](https://t.me/+relA0-qlUYAxZjI6)

Мой тг: [https://t.me/ironicMotherfucker](https://t.me/ironicMotherfucker)

_Дорогу осилит идущий!_

[Next Lesson](../11/OOP-Pervoe-znakomstvo-Ponyatie-abstrakcii-Vidy-otnoshenij-mezhdu-obektami.md)
