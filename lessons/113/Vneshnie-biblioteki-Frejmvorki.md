![](../../commonmedia/header.png)

***

   

Внешние библиотеки. Фреймворки
==============================

В рамках данной статьи мы познакомимся с понятием **библиотека** в Java (и в разработке в целом) и разберемся, что может содержать в себе библиотека.

Более глобально этот раздел - [Внешние библиотеки и знакомство с системами сборок](/Java-Road-Map-04-30#%D0%92%D0%BD%D0%B5%D1%88%D0%BD%D0%B8%D0%B5-%D0%B1%D0%B8%D0%B1%D0%BB%D0%B8%D0%BE%D1%82%D0%B5%D0%BA%D0%B8-%D0%B8-%D0%B7%D0%BD%D0%B0%D0%BA%D0%BE%D0%BC%D1%81%D1%82%D0%B2%D0%BE-%D1%81-%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0%D0%BC%D0%B8-%D1%81%D0%B1%D0%BE%D1%80%D0%BE%D0%BA) - призван как познакомить с понятием библиотеки, так и продемонстрировать инструменты, которые используются в реальных проектах для подключения библиотек, сборки (это понятие разберем позже) и запуска проекта. В конечном итоге, это будет знакомство с технологиями, которые вам придется использовать (и изучать глубже) как практикующему Java-разработчику.

  

### Библиотеки

Полагаю, даже на начальном уровне вы сталкивались с ситуациями, когда приходилось тратить время на типовой код - он же **boilerplate**. Этот код решал определенную задачу/проблему, но не менялся от задания к заданию и, в сущности, не относился к решаемой вами проблеме напрямую.

Даже если лично вам с таким столкнуться не пришлось, представить подобное будет легко.

Кроме того, если в каждом проекте писать такой код, решающий типовую проблему, заново - каждый раз есть шанс подцепить какие-то ошибки, на решение которых тоже придется тратить время.

Если утрировать, эти два фактора привели к логичному результату: вместо того, чтобы каждый раз изобретать велосипед, подобный код стали выносить в отдельные проекты - библиотеки - которые можно подключить к собственному проекту и использовать для решения соответствующих задач.

Собственно, почти весь дальнейший курс и посвящен знакомству с библиотеками в том виде, в котором они описаны выше.

В завершение подраздела отмечу, что некоторые библиотеки в том или ином виде могут со временем войти в стандарт языка, став частью его ядра. В нашем случае - частью Java Core.

Ярким примером может быть библиотека для работы с датой и временем, популярная до Java 8 - Joda Time. В Java 8 появился пакет _java.time_, который представляет собой творчески доработанную версию Joda Time. Если интересно - можете сравнить основные классы и их функциональность: [https://www.joda.org/joda-time/](https://www.joda.org/joda-time/)

  

### Что может быть внутри

Классифицировать библиотеки можно по-разному. С точки зрения содержимого или назначения я бы предложил следующий вариант:

*   Библиотеки, решающие свою узкую задачу;

1.  Утилиты. Например, дополнительная функциональности для работы с коллекциями, строками или чем-либо еще. Здесь и ниже, примеры ориентированы на Java, чтобы не распылятся. В целом же это актуально почти для любого языка. Примеры: Apache Commons, Guava;
2.  Адаптеры. Работа с конкретной БД, брокером сообщений или иным внешним ресурсом. Пример: Kafka Client - библиотека для работы с брокером сообщений Apache Kafka, различные HTTP-клиенты для отправки запросов через HTTP, адаптеры для СУБД и иных ресурсов;

*   **Спецификации**. Эти библиотеки могут не предоставлять функциональность как таковую, но давать API, которое будут реализовывать другие библиотеки. Мы еще не раз с таким столкнемся в дальнейшем. Это имеет смысл для ситуаций, когда мы работаем на высоком (относительно библиотеки) уровне абстракции. Например, каждая СУБД может иметь свои нюансы в работе через Java. Но нас эти нюансы мало волнуют, для нас достаточно общего интерфейса, а детали работы с СУБД будут скрыты за этим интерфейсом и его реализации под конкретную СУБД.  
    Данный пример - отсылка на JDBC, с которым мы будем знакомиться достаточно скоро. Строго говоря, в этом спецификация не является отдельной библиотекой, но такой пример близок к нашим реалиям.  
    Кроме того, это может быть более верхнеуровневая абстракция, имеющая несколько реализаций. Каждая делает примерно одно и то же, но может отличаться в деталях, производительности конкретных функций или фичах, выходящих за пределы спецификации.  
    В качестве примера можно привести JPA - намного более высокоуровневый интерфейс для взаимодействия с БД. Ни он, ни его реализации (мы будем знакомиться с наиболее популярной из них - Hibernate) не работают с БД напрямую (а используют JDBC), что позволяет использовать JPA в качестве примера к этому пункту.
*   **Фреймворки**. Этот пункт можно относить к библиотекам, в контексте подключаемости извне, однако обычно эти термины разделяют. Ключевое различие фреймворка от библиотеки в том, что фреймворк предоставляет скелет приложения, во многом определяя его архитектуру. Как и библиотека, он может предоставлять (и обычно предоставляет) дополнительную функциональность, но это не его основная задача. Пример фреймворка, с которым нам предстоит познакомиться - Spring.

Также важно понимать несколько моментов, когда речь идет о библиотеках (и фреймворках):

1.  Библиотеки тоже развиваются, из чего следует необходимость их **версионирования**. В библиотеку могут быть добавлены новые возможности, удалена устаревшая функциональность или исправлены какие-либо ошибки и уязвимости;
2.  В новой версии могут быть удалены или изменены классы и методы, с помощью которых мы работаем с данной библиотекой - **публичное API**. Это называется нарушением (или отсутствием) **обратной совместимости**\*;
3.  Одни библиотеки (и фреймворки) могут использовать другие библиотеки. Как через инструменты наследования (не обязательно в узком смысле - использования _extends_ и _implements_) в спецификациях, так и с точки зрения обеспечения работы самой библиотеки. Со временем станет очевидно, насколько верхнеуровневые библиотеки зависят от менее высокоуровневых и утилитных библиотек;
4.  В рамках одного приложения может работать только одна версия конкретной библиотеки. Это связано с особенностями загрузки и обращения классов в Java;
5.  Исходя из пунктов 3-5 может возникнуть ситуация, когда двум разным библиотекам требуется одновременно несколько активных версий третьей библиотеки из-за отсутствия обратной совместимости в этих версиях. Такая ситуация будет катастрофической в моменте (приложение не сможет запуститься или не сможет работать корректно) и неприятной в целом - придется искать или версии библиотек, в которых подобного конфликта нет, или искать иные способы решения - вплоть до отказа от использования конкретной библиотеки.

> **\*Обратная совместимость** - наличие в новой версии библиотеки интерфейсов (публичного API), присутствующих в старой версии.

На практике такие ситуации возникают не слишком часто, но исключить их полностью нельзя. Особенно если ваш продукт использует непопулярные (например, специфичные для узкой доменной области) или не поддерживаемые - те, которые разработчики перестали развивать - библиотеки.

  

  

### Библиотека в Java

Перейдем от абстрактных концепций к их материальному воплощению. В разных языках программирования библиотеки могут выглядеть по-разному, как и процесс их подключения.

В Java библиотека представляет из себя **JAR-файл** (в простонародье - JARник). JAR - сокращение от **_J_**_ava_ **_AR_**_chive_. По сути, это ZIP-архив, содержащий в себе библиотечные компоненты - классы и другие ресурсы, если необходимо. На самом деле, такие архивы используются не только для поставки библиотек, но об этом мы поговорим позже.

По факту, иногда библиотека разбивается на несколько JAR-файлов, которые могут использоваться друг друга. Так, например, популярный конвертер JSON (популярный формат для передачи данных) в Java-объекты - Jackson, является единой библиотекой, но поставляется в виде трех JAR-файлов.

При подключении библиотеки может быть несколько вариантов поиска конкретного JAR-файла:

1.  Найти и скачать вручную. После этого прописать путь к библиотеке в **_CLASSPATH_** (мы вернемся к этому моменту в следующем уроке). После этого при запуске приложения JVM будет искать библиотечные классы в указанном JAR-файле (-ах).
2.  С поправкой на использование IDE, мы проделаем подобное в следующем уроке;
3.  Использовать систему сборки. Эти системы, среди прочего, произведут автоматический поиск и загрузку указанных библиотек из своих (или дополнительно указанных) репозиториев. От нас требуется только указать нужную библиотеку и ее версию. Могут быть доступны и другие опции, вроде автоматической загрузки библиотек, используемых транзитивно (неявно, через использование их другими библиотеками), автоматического определения их версий и пр.
4.  Не говоря о возможностях таких систем за пределами работы с библиотеками. Системам сборки мы также посвятим несколько уроков и будем использовать их в рамках курса.

  

### Заключение

Роль библиотек в Java, как и почти в любом современном языке программирования, невозможно переоценить. Именно они делают разработку более быстрой, комфортной и безопасной.

Какими-то библиотеками и фреймворками придется овладеть обязательно, какие-то могут применяться по мере необходимости без плотного изучения, а какие-то будут зависеть от специфики проекта и их придется изучать по мере использования, иногда без шанса на то, что они понадобятся за пределами отдельно взятого проекта.

Более того, с определенной вероятностью вам предстоит поучаствовать в разработке собственных библиотек - для нужд проекта, компаний или чего-то более глобального.

Как бы там ни было, понимание того, что представляет из себя библиотека, как их подключать и какие общие проблемы (вроде конфликта версий) могут возникнуть - необходимо. И чем раньше вы с этим разберетесь, тем лучше.

  

На сегодня все!

![](../../commonmedia/footer.png)

Если что-то непонятно или не получается – welcome в комменты к посту или в лс:)

Канал: [https://t.me/ViamSupervadetVadens](https://t.me/ViamSupervadetVadens)

Мой тг: [https://t.me/ironicMotherfucker](https://t.me/ironicMotherfucker)

_Дорогу осилит идущий!_

[Next Lesson](../114/Logger-Podklyuchenie-Loggera.md)
