![](../../commonmedia/header.png)

***

   

DDL. Primary key и Foreign key. Каскадное удаление
==================================================

В последних уроках мы достаточно часто затрагивали тему связанных таблиц и способы взаимодействия с ними. Пришло время разобраться, какие средства дает сам SQL для обеспечения подобных связей.

Но начнем мы не с этого.

  

### Primary Key

Как и в случае с сущностями уровня приложения (скажем, пресловутые объекты класса Car из практики предыдущих уроков), записи в рамках таблицы часто (строго говоря, почти всегда) требуют некого идентификатора - это позволяет намного более прозрачно и легко взаимодействовать с отдельными записями - как при их поиске, так и при необходимости изменения или связывания с другими сущностями.

В общем-то, даже в рамках нашей БД таблицы имеют колонку _id_, которая используется в т.ч. для связи таблиц (например, _ticket.passenger\_id_ логически связан с _passenger.id_).

Идентификатор не всегда необходимо предоставлять в качестве самостоятельной колонки - иногда он может быть представлен как несколько колонок. Но об этом чуть ниже.

Главное требование к идентификатору, которое логично ожидать - он должен обеспечивать однозначное определение объекта (сущности, записи) среди множества других. А значит - должен быть уникальным хотя бы в рамках этого множества (например, таблицы).

SQL имеет несколько механизмов (достаточно родственных) для обеспечения уникальности значения колонки или нескольких колонок. Сегодня мы разберем наиболее верхнеуровневый и популярный из них - **Primary Key**.

Primary Key (он же **PK**, он же (редко) **первичный ключ**) - уникальный идентификатор записи в рамках таблицы. Как правило, именно он используется для связи таблиц друг с другом.

В наиболее распространенном сценарии, PK представлен на базе одной колонки (чаще всего - с говорящим названием _id_) и представляет собой числовой (зачастую, автоинкрементящийся) или uuid идентификатор. Последний, в зависимости от СУБД и предпочтений разработчика, может быть представлен как с использованием соответствующего типа (UUID), так и в строковом эквиваленте.

Возможны и другие варианты, когда PK формируется каким-то иным образом - скажем, жестко задается разработчиком для каждой записи при ее формировании или иные варианты, зависящие от требований конкретной задачи и принятых в команде практик.

Кроме того, PK может быть составным - представлять собой совокупность нескольких колонок, которые и будут давать уникальную идентификацию записи. При этом значения в рамках колонки могут быть не уникальны - значение будет иметь лишь совокупность значений всех составляющих PK колонок. Такой подход не слишком популярен и, откровенно говоря, неудобен в большинстве случаев. Но может иметь право на жизнь. Например, для все тех же промежуточных таблиц в M2M. Впрочем, там обычно используются иные инструменты для обеспечения уникальности записей.

Теперь, когда концепция понятна, разберемся с синтаксисом. В конце концов, в наших таблицах есть колонки с названием _id_. Можно ли их считать Primary Key?

К сожалению, нет. Хоть колонки и заявлены с характерных названием и даже имеют собственный алгоритм заполнения, в текущем виде они не гарантируют уникальности значения - мы всегда можем в ручном режиме вставить туда запись с уже существующим id.

Также, PK не может быть заполнен NULL’ом. Если PK состоит более, чем из одной колонки - ни одна из них не может быть NULL. Помните, в SQL невозможно сопоставление NULL-значений через “=”.

_NULL != NULL_

Итак, прежде чем перейдем к синтаксису, попробуем подвести итог.

Primary Key - одна или несколько колонок, которые не могут содержать _NULL_, дающих уникальное значение в рамках таблицы, которые позволяют однозначно идентифицировать конкретную запись.

Как же добавить PK в таблицу?

Проще всего добавить первичный ключ при создании таблицы (да и наименее затратно). Это тоже можно сделать несколькими способами (с некоторыми из них вы познакомимся лишь в следующем уроке).

Наиболее лаконичный способ, подходящий, если PK представляет из себя одну колонку:

```java
create table t1 (
  col1 bigserial primary key
);
```

После типа данных указываем предложение _PRIMARY KEY_. Теперь колонка является первичным ключом. Остальные колонки в таблице могут идти через запятую, как и если бы предложения _PRIMARY KEY_ не было. В этом смысле оно ничем не отличается от других - например, знакомого нам _DEFAULT_.

Но что, если ключ составной? Для этого тоже есть достаточно лаконичная форма записи:

```java
create table t2 (
  col1 bigserial,
  col2 timestamp,
  primary key (col1, col2)
);
```

Здесь _PRIMARY KEY_ упоминается наравне с колонками через запятую. В скобках же предложения указаны колонки, которые входят в PK. Такая форма записи может быть использована и при одноколоночном ключе - это дело вкуса и принятых в команде стандартов.

Наиболее, наверно, канонический (но не популярный) способ указания PK мы разберем в следующем уроке - он раскроет суть, более “низкоуровневый” (исключительно с логической точки зрения) механизм, синтаксическим сахаром над которым является PK.

Но что, если мы уже создали таблицу без _PRIMARY KEY_ и теперь хотим его добавить?

Тут, в первую очередь, стоит помнить о том, что для добавления PK в существующую таблицу нужно, чтобы данные в ней соответствовали требованиям к PK - уникальность и _NOT NULL_.

Само же добавление ключа элементарно (опять же, более канонический вариант рассмотрим в следующем уроке):

```java
create table t3 (
  col1 bigserial,
  col2 timestamp
);

alter table t3 add primary key (col1, col2);
```

Привожу пример для нескольких колонок. Если PK состоит из одной колонки - просто указываем лишь ее. Например:

```java
alter table t3 add primary key (col1);
```

Помните, в таблице может быть лишь один первичный ключ.

Также можно поступить хитрее (если это возможно) - добавить в таблицу новую колонку, которую и сделать PK:

```java
alter table t3 add column p3 bigserial primary key;
```

К слову, первичный ключ можно удалить при выполнении некоторых условий. Каких - разберем чуть ниже, как - в следующем уроке, поскольку для этого нужно понимать, чем PK является на самом деле:)

  

### Foreign key

Теперь, когда мы разобрались с PK, пришло время посмотреть, как он может помочь в оформлении связи между таблица.

Для этого нам понадобится ключ другого рода - **_FOREIGN KEY_** (**FK**, **внешний ключ**).

FK - ключ в таблице, который ссылается на другую таблицу, гарантируя согласованность значений в колонках, которые входят в FK и колонках PK в таблице, с которой этот FK связан.

В нашей тестовой БД эрзац-FK (не оформленным, но выполняющем функцию связи между записями таблиц) была колонка _passenger\_id_ в таблице _ticket_.

FK, в свою очередь, гарантирует, что он не может содержать значение, которое не существует в PK таблицы, на которую он ссылается. Кроме того, он гарантирует, что значения в колонках, образующих PK у связанной таблицы не будут изменены (если на них есть “ссылки” из других таблиц) или сами записи, не будут удалены, если нах них есть ссылки из других таблиц. А также гарантирует, что сам PRIMARY KEY не будет удален из таблицы (или изменен), пока на него есть хоть один FK.

Таким образом достигается согласованность данных - FK всегда содержит актуальное значение соответствующего первичного ключа. Первичный ключ не может быть изменен или удален, если это приведет к потере согласованности (она же - консистентность) данных.

Что же до синтаксиса?

Тут тоже есть варианты и снова канонический вариант от нас ускользнет.

Итак, если необходимо добавить FK при создании таблицы (PK в запросе не обязателен, просто привыкайте, что он должен быть):

```java
create table t4 (
  col1 bigserial primary key,
  col2 bigint references t1(col1)
);
```

Обратите внимание: хоть PK в t1 и _bigserial_, FK на него в _t4_ \- _bigint_, поскольку нам не нужен автоинкремент. Для типов данных без автоинкрементации это не критично.

Для указания самого FK здесь использовано предложение **_REFERENCE_**, после него указана таблица, на которую ссылаемся и в скобках - PK указанной таблицы.

Колонок в PK было более одной? Тоже не проблема:

```java
create table t5 (
  col1 bigserial primary key,
  col2 bigint,
  col3 timestamp,
  foreign key(col2, col3) references t2(col1, col2)
);
```

И, наконец, добавление FK в существующую таблицу:

```java
create table t6 (
  col1 bigserial primary key,
  col2 bigint,
  col3 timestamp
);

alter table t6 add foreign key (col2, col3) references t2(col1, col2);
```

Или же, если _col2_ и _col3_ не были указаны при создании:

```java
alter table t6
  add column col2 bigint,
  add column col3 timestamp,
  add foreign key (col2, col3) references t2(col1, col2);
```

Для одноколоночного FK можно было бы чуть проще:

```java
alter table t5 add column col2 bigint references t1(col1);
```

В целом, синтаксис не сложный и, во многом, однотипный.

Помните, что связь PK-FK не регламентирует условие связи таблиц через _JOIN_. На практике, в большинстве случае _JOIN_ будет происходить именно через эту связь в силу естественности такого условия, но при необходимости его можно строить каким угодно иным образом. Задача FK - лишь гарантия согласованности данных и маркер связи на уровне структуры.

  

### Каскадное удаление

FK хороши всем, кроме одного: они делают удаление записей в таблице со связанным PK очень неудобным - требуется так или иначе убрать все связанные записи. Переназначением на другую, не удаляемую запись, удалением или каким-то иным способом - не суть важно.

Безусловно, в этом неудобстве нет ничего плохого - СУБД лишь заботится о согласованности данных через предоставленный для этого механизм. Но это может нести неудобства. Особенно, когда цепочка связей длинная и удалять приходится записи во множестве разных таблиц.

PostgreSQL предоставляет синтаксис каскадного удаления. Он позволяет указать при формировании FK, что записи должны удаляться автоматически, если удаляется запись с соответствующим PK в связанной таблице.

Безусловно, такой механизм подходит далеко не для всех ситуаций и часто его использование может стать фатальным для системы. Поэтому использовать его рекомендую только в случае реальной необходимости - когда связанные записи не имеют смысла без ключевой. Скажем, история покупок пользователя онлайн-магазина может быть не нужна, если сам пользователь был удален.

> **Основная мысль**: допустимость (или даже необходимость) каскадного удаления диктуется требованиями к конкретной сущности и связям. Если подобного требования нет или допустимость этого решения вызывает сомнения - не стоит им злоупотреблять.

Как же выглядит каскадное удаление?

По сути, это просто модификатор к FK. Например, таблица _t4_, приведенная выше, могла бы формироваться следующим запросом, если бы требовалось каскадное удаление:

```java
create table t4 (
  col1 bigserial primary key,
  col2 bigint references t1(col1) on delete cascade
);
```

В таком случае, как только удалялась запись, например, с _col1 = 1_ в таблице _t1_, в таблице _t4_ сразу удалялись бы все записи, для которых _col2 = 1_.

Как видите, в данном механизме нет ничего сложного. Но он требует аккуратности при использовании. И хорошего DBA, который не забывает регулярно создавать дампы БД на случай, если вашей аккуратности оказалось недостаточно:)

  

С теорией на сегодня все!

![](../../commonmedia/footer.png)

Переходим к практике:

### Задача

Для таблиц, созданных в рамках практики к [Уроку 99](/DDL-CREATE-Sozdanie-tablic-08-12) добавьте PK и FK. Также добавьте их для остальных таблиц в рамках тестовой БД. Включая _passenger_ и _ticket_.

  

Если что-то непонятно или не получается – welcome в комменты к посту или в лс:)

Канал: [https://t.me/ViamSupervadetVadens](https://t.me/ViamSupervadetVadens)

Мой тг: [https://t.me/ironicMotherfucker](https://t.me/ironicMotherfucker)

_Дорогу осилит идущий!_

[Next Lesson](../102/DDL-CONSTRAINT.md)
