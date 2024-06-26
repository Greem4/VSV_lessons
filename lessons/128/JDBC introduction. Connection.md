# Что такое JDBC. Подключение к БД. Connection

Эта статья открывает раздел, посвященный взаимодействию с БД через Java-приложение. Так, в ближайших уроках мы 
рассмотрим основной механизм работы с реляционными базами данных через Java, познакомимся с основными инструментами, 
используемыми при взаимодействии с БД. 

Практическая ценность этой информации в коммерческой разработке не слишком высока - шанс, что вы будете использовать 
именно этот API в реальных проектах невелик. Но именно на базе изученной библиотеки работает абсолютное большинство 
более высокоуровневых решений, с некоторыми из которых мы познакомимся в следующих разделах. А значит - сталкиваются 
с теми же ограничениями и используют те же инструменты, которые мы будем изучать.

Основной целью раздела мне видится не столько знакомство с отдельными классами и методами, сколько разъяснение основ 
взаимодействия с базами данных и ряда других специфических аспектов. Наконец, я надеюсь помочь вам избежать 
магического мышления и сформировать фундамент, который позволит подходить к более продвинутым инструментам системно - 
именно этого не хватает большинству junior-специалистов.

## JDBC

При работе с базами данных через Java можно заметить ту же тенденцию, что и при работе с БД через любой другой 
клиент: существует единый API для взаимодействия с реляционными базами данных (его же поддерживают и некоторые 
NoSQL БД), а вот большинство реализаций NoSQL предоставляют собственные API и клиенты, которые обычно сильно 
отличаются друг от друга.

Это является логичным следствием того, что механизмом взаимодействия с реляционными БД является SQL, в то время как 
практически каждая реализация NoSQL предоставляет собственное API, не всегда оформленное в виде языка в привычном 
понимании.

В основном курсе мы не будем углубляться в детали работы с NoSQL БД, вместо этого сфокусируемся на реляционных базах 
данных.

**JDBC** - _Java DataBase Connectivity_ - часть стандартной библиотеки Java, предоставляющие единый стандарт и, 
одновременно, публичный API для работы с реляционными базами данных. Кодовая база JDBC содержится в пакете `java.sql`.

Сам по себе JDBC не умеет работать ни с одной из БД. Она лишь предоставляет основные интерфейсы*, которые 
будет использовать Java-разработчик для взаимодействия с базами данных.

> *Рекомендую открыть содержимое пакета `java.sql` посмотреть хотя бы список файлов в нем.
> 
> Конечно, кроме интерфейсов там есть и классы. Но они несут общее или вспомогательное назначение: классы исключений,
> констант (в т.ч. енамы) и подобное. Если не ошибаюсь, там есть единственный значимый класс с собственным 
> поведением, но о нем позже.

В свою очередь реальные механизмы взаимодействия с конкретной базой данных предоставлены в **драйверах** - библиотеках 
с имплементациями интерфейсов из `java.sql`, которые будут учитывать специфику конкретной СУБД, содержать механизм 
доставки запросов к ней и прочее. Как правило, драйверы поставляются разработчиками самой СУБД. 

При этом Java-разработчик практически никогда не работает с драйвером напрямую - лишь добавляет его в свой проект. Т.
е., по сути, лишь указывает нужную зависимость в Maven- или Gradle-конфигурации. А взаимодействие на уровне кода 
сводится к использованию интерфейсов JDBC, чьи имплементации из драйвера будут использованы во время выполнения 
программы.

В этом и заключается основное различие во взаимодействии с РСУБД и NoSQL, драйверы* которого обычно не имплементируют 
JDBC. В результате чего работа с каждой новой NoSQL БД требует еще и изучения новой Java-библиотеки со своим API и 
своими ограничениями.

> *Обычно такие библиотеки называют клиентами, но я не вижу смысла объяснять разницу этих терминов в обзорной статье.

Подводя краткий итог, ближайшие статьи будут посвящены ключевым интерфейсам JDBC и правилам их использования. 
Конечные реализации этих интерфейсов мы затрагивать не будем - их особенности никак не влияют на наш код.

## Подключение к БД из Java-приложения

Пришло время вспомнить нашу тестовую базу данных, развернутую в PostgreSQL. Именно ее мы возьмем за основу для 
дальнейших примеров и практических задач. Разница лишь в том, что теперь мы будем обращаться к ней из Java-приложения.

Из этого логично следует, что нам требуется Java-приложение и драйвер для работы с PostgreSQL.

Для демонстрации и практики будем использовать этот репозиторий: 
[ссылка](https://github.com/KFalcon2022/jdbc-practical-tasks).

Подключить драйвер достаточно просто. Ищем JDBC-драйвер для PostgreSQL и используем свежую версию:

```groovy
runtimeOnly 'org.postgresql:postgresql:42.7.1'
```

Обратите внимание, что использована конфигурация `runtimeOnly`.
[mvnrepository](https://mvnrepository.com/artifact/org.postgresql/postgresql/42.7.1), вероятно, предложит вам 
стандартную конфигурацию `implementation`, но для драйвера в ней нет необходимости - на этапе компиляции нам 
достаточно интерфейсов JDBC, а сама реализация нужна только для этапа выполнения. Это справедливо вне зависимости от 
СУБД, с которой вы будете работать. По крайней мере, пока вы используете JDBC*.

> *JDBC предоставляет единый интерфейс для доступа к РСУБД. Единый, но не единственный.
> 
> Распространенным примерам альтернативного подхода может быть, например R2DBC - это альтернативная спецификация для 
> работы с базами данных, актуальная для проектов с реактивным стеком. Детали нас интересуют мало, главное - работа 
> даже с реляционными базами данных не всегда завязана на JDBC, хоть он и остается решением по-умолчанию.
> 
> И, например, R2DBC-драйвер для PostgreSQL обычно добавляют в проект как `implementation`, не отделяя драйвер от 
> спецификации (поставляется транзитивно). Этого можно избежать, но углубляться в эту тему не будем.
 
По сути, сразу после этого мы имеем на руках приложение, которое может взаимодействовать с базой данных. Осталось 
разобраться, каким образом.

## Connection

Ключевым интерфейсом при работе с JDBC является `Connection`. Он представляет собой отражение пользовательской 
сессии к БД.

Так или иначе, все взаимодействие с БД будет сводиться к работе с объектом (или объектами) `Connection` - он 
инкапсулирует все API для отправки SQL-запросов, работы с транзакциями, содержит настройки самого подключения. Все 
остальные интерфейсы, которые нам потребуются, будут предоставляться именно через `Connection`.

Единственная проблема - нельзя просто взять, и создать объект `Connection` вручную. Хотя бы потому что это интерфейс,
а его имплементация будет доступна лишь во время выполнения. А значит, нам нужен некий класс, который будет отвечать 
за создание `Connection`.

JDBC предоставляет такой класс - `DriverManager`. Это тот единственный класс с собственным поведением, о котором 
упоминалось выше. 

Через механизмы Java Reflection (мы кратко упоминали его в прошлом уроке) этот класс получит доступы к драйверам и 
реализациям `Connection` во время выполнения и сможет создать интересующие нас объекты. На этапе написания код нам 
остается лишь использовать методы самого `DriverManager`.

Опуская ряд вспомогательных методов для настройки `DriverManager`, его API сводится к нескольким перегрузкам метода 
`getConnection()`.

Проще всего нам будет работать с тем, который принимает адрес СУБД (мы с ним сталкивались при работе с БД 
через другие клиенты), логин и пароль пользователя.

Так, получение объекта `Connection` в коде сводится к примерно такой записи:

```java
try (Connection connection = DriverManager.getConnection(
            "jdbc:postgresql://localhost:5432/test_db",
            "postgres",
            "postgres")) {
    // Дальнейшая работа с БД через connection
} catch (SQLException e) {
    log.error(e);
}
```

Полагаю, логин и пароль вопросов не вызывают. Но стоит разобраться с `url` (имя первого параметра 
`DriverManager.getConnection`) и почему-то появившимся `try-with-resources`.

С URL все просто. Стандартная для JDBC маска выглядит примерно так: `jdbc:%subprotocol%:%subname%`.

`%subprotocol%` - по сути, это указание драйвера, который будет использован. В зависимости от него могут быть 
различные правила к формированию `%subname%`. В случае с PostgreSQL - драйвер обозначается как `postgresql`.

`%subname%` - эта часть может содержать различные данные в различном формате - в зависимости от СУБД и способа 
подключения. Так или иначе, здесь должна содержаться "ссылка" - адрес БД с сети. В разделе, посвященном Web, мы 
будем чуть детальнее разбирать тему адресации. В нашем случае это адрес СУБД: `localhost:5432/` и путь до 
интересующей нас БД: `test_db`. Последний можно не указывать - тогда Connection будет создан для СУБД, без четкой 
привязки к определенной базе данных.

Теперь, почему `try-with-resources`. Поскольку `Connection` отражает физическое подключение к СУБД, он, как и любой 
объект, отражающий подключение к внешнему ресурсу, реализует `AutoCloseable`. А значит требует закрытия. 
Соответственно, должен либо создаваться в `try-with-resources`, либо потребуется явно вызывать `close()` после 
завершения работы с ним.

И, наконец, catch-блок. В нем содержится обработка `SQLException` - базового исключения при работе с БД. Опять же, в 
силу того, что мы пытаемся получить доступ к внешнему ресурсу - нам нужен механизм оповещения на случай, если не 
удалось достучаться до самого ресурса, или возникли какие-то проблемы при дальнейшем взаимодействии. Стандартным для 
Java инструментом в подобных ситуациях выступает checked-исключение.

По сути, `SQLException` - аналог известного нам `IOException`, но для работы с БД*.

> *Обратите внимание: `SQLException` НЕ наследует `IOException`, как можно было бы подумать. Каждый из них дает 
> начало своей иерархии исключений, но сами по себе они являются прямыми наследниками `Exception`.

На этом завершаем обзорное знакомство с JDBC. Конкретные инструменты для работы с БД будем разбирать в следующих 
статьях. Там же будет и практика.


#### На сегодня все!

Практика так же будет в следующей статье.

![img.png](../../../commonmedia/justTheoryFooter.png)

> Если что-то непонятно или не получается – welcome в комменты к посту или в лс:)
>
> Канал: https://t.me/ViamSupervadetVadens
>
> Мой тг: https://t.me/ironicMotherfucker
>
> **Дорогу осилит идущий!**


[Next Lesson](../129/Statement.%20DDL.%20ResultSet.md)
