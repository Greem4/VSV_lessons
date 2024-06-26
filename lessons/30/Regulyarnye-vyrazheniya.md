![](../../commonmedia/header.png)

***

   

Регулярные выражения
====================

**Регулярные выражения** (**regex**, **regexp**) – инструмент, по сути, практически отдельный язык, предназначенный для работы работы с текстовой информацией. Regex позволяет крайне гибко обрабатывать текстовые (строковые) данные в целях валидации, поиска подстрок, разделения строк на подстроки и массы других операций. Все эти действия строятся на проверке соответствия строки или какой-то ее части определенному шаблону, который и является регулярным выражением.

До того, как мы перейдем к основному материалу, стоит отметить, что regex представлен в большинстве современных языков программирования и базовые правила написания шаблонов практически идентичны в различных ЯП. Однако каждый язык может иметь свои надстройки, делающие использование регулярных выражений более гибким и удобным.

Кроме того, данный инструмент, в конечном итоге, оказывается нужен практически каждому разработчику. На каких-то проектах вы можете не найти регулярных выражений вообще (по крайней мере, в явном виде), в каких-то будете сталкиваться с ними практически ежедневно. Но автор, например, не знает ни одного Java-разработчика, которому regex не понадобились хотя бы несколько раз за карьеру.

Основную информацию в рамках данного урока мы получим из двух статей (прежде, чем к ним переходить, прочтите несколько абзацев ниже):

· Metanit: [https://metanit.com/java/tutorial/7.4.php](https://metanit.com/java/tutorial/7.4.php) - не считаю статью удачной, но пойдет в качестве первичного знакомства и просто в дань уважения блогу, который хорошо разжевал многие базовые темы;

· Javarush: [https://javarush.com/groups/posts/regulyarnye-vyrazheniya-v-java](https://javarush.com/groups/posts/regulyarnye-vyrazheniya-v-java) - действительно хороший материал, к которому иногда можно возвращаться в т.ч. как к базовому справочнику по regex.

Регулярные выражения, особенно с использованием классов _Pattern_ и _Matcher_, могут очень многое. Но и материал с учетом возможностей этих классов получится крайне объемным, особенно для неподготовленного человека. При этом большинство типовых задач с регулярными выражениями ограничиваются использованием методов _String_, поддерживающими regex: _split()_, _replaceAll()_, _matches()_ и пр.

В рамках первого знакомства я рекомендую лишь ознакомиться с основным синтаксисом самих регулярных выражений.

А именно **метасимволами**:

· Границ строки/подстроки. В первую очередь – ‘^’ и ‘$’;

· Символьных классов. Их немного и они легко запоминаются;

· Группировки. Хотя бы первые три из статьи на Javarush, остальное придет со временем;

· Квантификаторов. Их все, в целом, вполне реально запомнить, особенно немного попрактиковавшись.

Также стоит убедиться, что понимаете актуальность экранирования символов по итогам прочтения статей.

На основе описанных выше пунктов можно решить абсолютное большинство типовых задач. А поискав подходящие методы в _Matcher_ – и остальные задачи не станут непреодолимой преградой. Однако попытавшись охватить все сразу есть риск возникновения каши и дальнейшей настороженности по отношению к регулярным выражениям в целом.

На этом рекомендую, наконец, перейти к ссылкам выше.

  

Также рекомендую найти ресурс для проверки regex на свой вкус, их достаточно много, например:

· [https://regex101.com/](https://regex101.com/)

· [https://regexr.com/](https://regexr.com/)

· Любые другие, которые вы сможете нагуглить

Такие сервисы могут быть удобны для проверки как синтаксической корректности ваших регулярных выражений, так и для тестирования. Они, преимущественно, просты в использовании, особенно если потратить несколько минут на освоение функциональности конкретного сервиса. И являются отличным подспорьем на начальном этапе.

#### В качестве итога

Тема является не самой простой и на ней спотыкаются многие разработчики. Преимущественно из-за страхов и непонимания, развившихся на ранних этапах обучения, а также из-за недостатка практики. Помните, что это всего лишь очередной инструмент, который не является чем-то непостижимым. И при должном усердии у вас обязательно получиться в нем разобраться. Не отчаивайтесь, если этого не произойдет с первой попытки. Не пугайтесь, если для каждого нового выражения вам придется возвращаться к статье или лезть в гугл. Это нормально, через это проходит каждый разработчик. И у вас обязательно получится.

С теорией на сегодня все!

![](../../commonmedia/footer.png)

  

Переходим к практике:

#### Задача 1:

Реализуйте _boolean_\-метод, валидирующий входящую строку. Метод должен возвращать _true_, если строка соответствует номеру мобильного телефона (в качестве примера привожу номер для РФ, вы можете выбрать любой другой, но со схожей маской).

Маска корректного номера: _+7 (XXX) XXX-XX-XX_, где "X" – цифра от 0 до 9. Обратите внимание на наличие скобок и пробелов.

Вариант с усложнением (\*): решите ту же задачу, но символы скобок, дефиса и пробелов – опциональны (каждый из них может или присутствовать, как на оригинальной маске, так и отсутствовать вовсе, возможность частичного использования или использования символов-разделителей в другом порядке считаем невалидным).

#### Задача 2:

Реализуйте метод для работы с ФИО. Входным параметром должна являться строка, содержащая русскоязычное ФИО. Фамилия, имя и отчество должны начинаться с прописной буквы и быть разделены пробелами. Фамилия может быть двойной и писаться через дефис (каждая часть фамилии начинается с прописной буквы). Если строка валидна – верните ФИО, обернутое в класс «Полное имя», содержащий фамилию, имя и отчество. Если невалидна – бросьте из метода исключение, указывающее на ошибку валидации.

#### Задача 3:

Реализуйте задачу [https://github.com/KFalcon2022/practical-tasks/blob/master/src/com/walking/lesson26\_string\_types/task2/Main.java](https://github.com/KFalcon2022/practical-tasks/blob/master/src/com/walking/lesson26_string_types/task2/Main.java)

Теперь слова в исходном массиве могут быть разделены несколькими пробелами, а также знаками табуляции и иными пробельными символами. Словами считаются лишь подстроки, состоящие из буквенных символов или содержащие в середине слова один или несколько дефисов, но не более одного подряд. При наличии в исходной строке невалидных символов или некорректном использовании допустимых, должно быть выброшено исключение.

#### Задача 4(\*\*):

Реализуйте программу, разбивающую исходный текст на составные части. Текст – на абзацы (разделены _‘\\n’_), абзацы на предложения (разделены _"."/ "?"/ "?!"/ "!"/ "…"_). Предложения на слова (разделены пробелами, но также могут использоваться знаки препинания _","/ "-", ":"_).

После этого выведите на экран исходный текст. Предложения допустимо разделить точками, слова – пробелами без сохранения знаков пунктуации внутри предложения. Сохранение изначальной пунктуации, на мой взгляд, излишне усложнит задачу и сдвинет акцент с практики регулярных выражений.

Подумайте, как наиболее корректно декомпозировать ваше решение.

В качестве совета: попробуйте разные подходы для решения задачи, нет необходимости реализовать наиболее оптимальным способом. Например, одним из вариантов упрощения исходной задачи может стать избавление от лишних символов или их замена одним определенным через метод replaceAll() класса String.

  

Если что-то непонятно или не получается – welcome в комменты к посту или в лс:)

Канал: [https://t.me/+relA0-qlUYAxZjI6](https://t.me/+relA0-qlUYAxZjI6)

Мой тг: [https://t.me/ironicMotherfucker](https://t.me/ironicMotherfucker)

_Дорогу осилит идущий!_

[Next Lesson](../31/Klassy-resursov-IO-Streams.md)
