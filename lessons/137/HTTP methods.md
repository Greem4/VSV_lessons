# HTTP. Методы HTTP

В прошлой статье мы уже столкнулись с понятием "**метод HTTP**" при разборе запроса на составляющие. Сегодня мы
подробнее разберем эту тему, а также познакомимся с рядом связанных терминов.

## Обзор

В HTTP под методами понимают стандартные маркеры запроса, один из которых должен быть указан при обращении к
конкретному ресурсу. Это позволяет создать несколько различных запросов для одного и того же URL, каждый - со своим
методом и собственной логикой обработки.

Всего HTTP предоставляет 9 методов (ниже мы разберем каждый). Для каждого из их существуют рекомендации по
использованию и ряд правил, в т.ч. ограничивающих содержимое запроса (или ответа) в зависимости от выбранного метода.

> **!NB**: Выше метод неспроста назван маркером. Сам по себе протокол HTTP не имеет строгих физических ограничения ни
> для содержимого запроса, ни тем более для поведения при его обработке сервером. И в этом отношении метод
> действительно является некой стандартной пометкой для сервера.
>
> Однако спецификации протокола определяют рекомендации по использованию конкретных методов. И уже эти рекомендации
> могут восприниматься как строгие правила конкретным сервером или даже конкретной библиотекой/фреймворком.
> Следствием становится наличие реальных ограничений в использовании для тех или иных методов HTTP.
>
> Отсюда вытекает ряд заблуждений и недопониманий, связанных с зонами ответственности в отношении подобных ограничений.
> Сюда же относится расхождение в теории, которую обычно изучают при первом знакомстве с протоколом, и практиками,
> применяемыми в различных системах.
>
> Поскольку курс направлен на новичков, я не буду сильно углубляться в эти нюансы, по крайней мере, в текущем
> разделе. Но их дополнительное изучение может оказаться полезным как при прохождении собеседований, так и в
> нестандартных рабочих ситуациях вне зависимости от уровня специалиста.

Определение метода выше может быть непонятным, прежде чем приступить к разбору конкретных методов, рассмотрим
небольшой пример.

### Пример

Допустим, у нас есть ресурс, доступный по URL `http://aviaticket.com/passenger`. Будем считать, что это та самая
система, для которой мы сначала проектировали БД, а потом работали с ее БД через Java-приложение. Теперь же она
доступна как клиент-серверное приложение.

И в этой системе нужно сделать функциональность по добавлению пассажиров, получению списка пассажиров и т.д. Чтобы
не завязывать каждое из этих действий на отдельный URL, мы можем использовать методы HTTP.

```http request
GET /passenger HTTP/1.1
Host: aviaticket.com
```

Метод `GET` мы будем использовать для получения списка пассажиров. Этот метод мы уже видели в предыдущей статье.

```http request
POST /passenger HTTP/1.1
Host: aviaticket.com
```

Метода `POST` будем использовать для добавления нового пассажира. Как видите, хост и путь к ресурсу остались
прежними, но за счет использования другого метода мы можем использовать иной обработчик на сервере.

```http request
DELETE /passenger HTTP/1.1
Host: aviaticket.com
```

Метод `DELETE` - очевидно, для удаления пассажира. И т.д.

### Список HTTP-методов

В отличие от Java, в HTTP нет возможности создавать собственные методы* - эти термины имеют разное значение, хоть и
обозначаются одним и тем же словом. Вместо этого HTTP предоставляет набор из 9 методов, которые могут быть
использованы в запросе. При этом обработка запроса с конкретным методом по конкретному URL - ответственность сервера
и логика обработки остается на усмотрение программиста.

> *Если быть точным, сам HTTP не запрещает создавать собственные методы. По сути, это просто строка, которая сама по
> себе не несет никакой логики.
>
> Но с большой долей вероятности возникнут проблемы при использовании таких методов. Как на инфраструктурном уровне
> (файерволы, серверы и т.д.), так и на программном (фреймворки и библиотеки). Поэтому в общепринятом значении
> список HTTP-методов определен спецификацией протокола и не расширяем.

Итак, 9 методов. Ниже рассмотрим их, их ограничения на уровне спецификации и ожидаемое (опять же, на уровне
спецификации) поведение.

> Приведенное ниже описание семантики (поведения) HTTP-методов местами неточное. Это связано с тем, что в данном
> разделе хочется рассказать именно про HTTP и особенности, которые регламентирует протокол. Но сама спецификация 
> менялась и расширялась со временем, в результате чего подходы, декларируемые в изначальной спецификации HTTP/1.1, 
> могут быть неактуальны в текущих реалиях. Кроме того, некоторые принципы работы с HTTP вытекают из более 
> высокоуровневых концепций. И, наконец, цель данной статьи - дать понимание протокола с точки зрения Back-end 
> разработчика. А значит ряд сценариев использования HTTP окажется за пределами зоны нашего интереса.
>
> В силу этого приведенное описание - попытка найти золотую середину, не идя против буквы спецификаций, не входя в 
> противоречие с тем, что вы увидите на практике и, при этом, не перегружая статью бесполезными деталями.
>
> Если хочется ознакомиться с оригинальными рекомендациями - рекомендую посмотреть в соответствующих RFC, они
> написаны достаточно понятным языком:
> 
> 1. [ссылка 1](https://datatracker.ietf.org/doc/html/rfc2068). пп. 9.2-9.8. Де-юре устаревшая, но все еще 
> используемая спецификация. На мой взгляд, она проще для восприятия новичками;
> 2. [ссылка 2](https://datatracker.ietf.org/doc/html/rfc9110). п. 9.3, актуальная спецификация. 
> 
> И отдельно для `PATCH`: еще [одна ссылка](https://datatracker.ietf.org/doc/html/rfc5789).

#### OPTIONS

Один из вспомогательных методов. Он не выполняет полезной работы на сервере, но позволяет клиенту получить информацию о 
том, какие существуют особенности при работе с ресурсом или сервером в целом. Также может использоваться для 
проверки доступности сервера со стороны клиента.

Ответ сервера на такой запрос обычно содержит следующую информацию:

1. Какие методы доступны для текущего ресурса. Как правило, для одного URL не реализуются обработчики под все 9 
   методов HTTP - в этом просто нет практической необходимости. Таким образом, `OPTIONS` может дать понимание, какие из 
   них все-таки доступны;
2. Поддерживаемые форматы данных, спецификаций и пр.

В целом, back-end разработчик редко сталкивается с этим методом в своих повседневных задачах.

#### TRACE

Еще один вспомогательный метод. Он отправляет в ответе содержимое запроса обратно клиенту.

На первый взгляд, это бессмысленно. Но этот метод необходим для тестирования API - он позволяет увидеть любые 
изменения, которые были добавлены во всей цепочке коммуникации между клиентом и конечным сервером*.

> *Практика, зачастую, хитрее, чем базовые теоретические представления. Поэтому современная сетевая инфраструктура
> достаточно сложная, в ней есть множество компонентов, о которых не рассказывают новичкам.
>
> Так, для обеспечения безопасности, легкости масштабирования, роста производительности или иных целей запросы редко
> идут по простому пути "клиент-сервер". В этой цепочке может быть один или несколько прокси-серверов, различных
> балансировщиков и т.д. Все они выполняют свои функции, которые важны для эффективной работы продукта. Но для
> детального рассказа о них придется дать много теоретической информации, которая не имеет прямого отношения к
> рассматриваемой теме. Суть же заключается в том, что промежуточные серверы могут изменять запрос - добавлять или 
> удалять какие-либо заголовки или иным образом изменять содержимое запроса.

#### CONNECT

Третий вспомогательный метод. Он необходим для конфигурации условно-прямого соединения между клиентом и сервером в 
ситуациях, когда де-факто их разделяет один или несколько прокси-серверов. В детали углубляться не будем, в силу того, 
что для них необходимо рассказать о многих нюансах устройства сети, которые на данном этапе будут избыточны. Пока 
ограничимся тем, что подобное прямое соединение может быть более безопасным.

Ниже представлены методы, с которыми вам придется сталкиваться на практике намного чаще.

#### GET

Один из наиболее популярных методов HTTP. Предназначен для получения содержимого ресурса в определенном формате. Или, 
иными словами, для получения данных.

В силу своего назначения, считается, что GET-запросы не могут содержать тела*. Если необходимо передать какие-то
параметры - это можно сделать в URL через параметры запроса.

В соответствии со спецификацией, этот метод не может менять состояние сервера. Но, как и в остальных случаях, это
является лишь рекомендацией и не защищает от технической возможности реализовать обработчик, который не будет
следовать этому правилу.

> *В современных представления это условие было смягчено, но большинство инструментов все еще не допускают присутствия 
> тела запроса у `GET`.

#### HEAD

Еще один метод, предназначенный для получения информации. В реальных приложениях используется достаточно редко.
Отличается от `GET` тем, что его ответ не может содержать тела - т.е. вся полезная нагрузка может содержаться
только в заголовках ответа.

В силу указанных ограничений, его рекомендуется использовать для получения метаинформации для ресурса.

#### POST

Метод, предназначенный для передачи данных ресурсу. Передаваемые данные помещаются в тело запроса.

Приведенный выше пример, в котором добавлялись пассажиры с помощью POST-запроса неплохо демонстрируют логику
данного метода в частном случае. В более общем представлении он может использоваться для различных сценариев, от 
создания или обновления ресурса до передачи данных из форм ввода. Конечные правила использования определяются 
конкретным ресурсом.

Наравне с `GET`, является одним из наиболее популярных методов HTTP.

#### PUT

Метод, предназначенный для создания* или полного обновления (замену) содержимого ресурса. Через него, например, 
можно было бы обновить существующего пассажира, заменив все поля значениями, из тела PUT-запроса.

> Специфика создания ресурса плохо сочетается с тем, как мы будем работать с запросами в Java-приложении, поэтому
> эту деталь пока оставим за скобками. Возможно, позже рассмотрим трактовку этого пункта в 
> [REST](https://ru.wikipedia.org/wiki/REST).

Теоретически, если сразу после получения ответа от `PUT` отправить GET-запрос на тот же ресурс - его ответ должен 
быть эквивалентен тому, что было отправлено в теле PUT-запроса. На это не стоит опираться на практике, но это 
позволяет чуть лучше понять специфику PUT-запроса.

Как и в случае с `POST`, полезная нагрузка должна передавать в теле запроса. Но если специфика обработки тела 
POST-запроса определяется ресурсом, то тело PUT-запроса регламентируется как "данные для замены" ресурса, что делает 
его более узконаправленным.

#### PATCH

Еще один метод для изменения содержимого ресурса. В данном случае - для частичного обновления существующего ресурса.
Скажем, для добавления любимого аэропорта существующему пассажиру или обновления даты последней покупки.

#### DELETE

Метод, предназначенный для удаления ресурса. Примером может выступать запрос на удаление пассажира.

## Безопасность и Идемпотентность

Безопасность и идемпотентность - две характеристики методов HTTP. В этом пункте разберемся с обеими.

Безопасность методов выражается в том, что они не изменяют состояние сервера. На практике это выражается в том, что
безопасными считаются методы, ответственные за чтение в том или ином виде. Т.е. `GET` и `HEAD`. В более поздней 
редакции спецификации к безопасным добавили методы `OPTION` и `TRACE` по тем же самым причинам.

Под идемпотентностью понимают характеристику метода, которая означает, что повторные вызовы метода с теми же
значениями (в параметрах запроса, теле запроса и т.д.) не изменяют состояние сервера. Т.е. если вызвать идемпотентный
метод 2, 3, 10 раз подряд с одинаковыми параметрами - состояние сервера будет тем же, как и если бы этот метод был
вызван лишь единожды.

Это позволяет оптимизировать работу клиент-серверных приложений, в т.ч. через кэширование результатов запроса на
сервере. Но, как и в других случаях, стоит понимать, что идемпотентность методов определяется спецификацией HTTP и на
практике всегда остается возможность реализовать на стороне сервера не идемпотентное поведение для
идемпотентных методов. Но это может привести к некорректному поведению, если окажется, что регламент в отношении
идемпотентности соблюден на каком-то ином уровне - скажем, каком-то прокси-сервере, находящемся в цепочке
коммуникации между клиентом и сервером, который в действительности обрабатывает отправляемые запросы.

> В силу неоднократно подсвеченной специфики с наличием рекомендаций, но отсутствием гарантий их выполнения, 
> рекомендую при разработке собственных серверных приложений следовать двум пунктам:
> 
> 1. Стоит придерживаться рекомендаций спецификации HTTP. Это поможет избежать проблем с инфраструктурой, облегчит 
> поддержу решения и сделает его более понятным для коллег;  
> 2. При знакомстве с любым новым проектом считайте, что обозначенные рекомендации не выполняются, пока не убедитесь 
> в обратном. Иначе всегда остается шанс, что ваши ожидания будут обмануты:)

В HTTP идемпотентными считаются безопасные методы (`GET`, `HEAD`, `OPTION` и `TRACE`), а также методы `PUT` и 
`DELETE`. Первые 4 идемпотентны просто в силу того, что ничего не меняют, а значит, что 1, что 10 вызовов оставят 
сервер в исходном состоянии. `PUT`и `DELETE` идемпотентны потому что каждый их вызов делает одно и то же - полностью 
объявляет ресурс до состояния, указанного в теле запроса (т.е. при одинаковом теле - обновлять будет одинаково), или 
же удаляет ресурс - повторное удаление просто ничего не сделает.

Тут стоит отметить, что идемпотентность - достаточно узкое понятие. Оно является лишь характеристикой самих методов, 
позволяющих оптимизировать работу клиента или сервера, а не какой-то гарантией результата выполнения.

Т.е. идемпотентность `GET` никак не гарантирует, что при каждом вызове будет одинаковый ответ - ведь между 
повторяющимися вызовами `GET` может быть обработан условный `DELETE` для того же ресурса, в результате чего ответ у 
повторных запросов будет различен.

Так и идемпотентность `PUT` никак не гарантирует, что второй вызов метода подряд ничего не изменит на сервере - ведь 
между этими вызовами может быть вызов `PUT`, `POST`, `DELETE` или `PATCH` от другого клиента.

На первых этапах понятия безопасности и идемпотентности важны в первую очередь для закрепления самих терминов и их 
базового понимания, а также для прохождения собеседований. Практическая ценность этих знаний в самой разработке для 
новичков сомнительна.

## Заключение

Мы шаг за шагом приближаемся к моменту, когда сможем использовать полученные знания на практике. Но помните, что 
информацию в теоретических статьях этого раздела не стоит воспринимать как истину в последней инстанции - они 
являются лишь попыткой дать понимание базовых механизмов и инструментов в виде, который будет понятен и потенциально 
полезен новичку, ранее не сталкивавшемуся с сетевой коммуникацией. 

Из-за этого сама информация в статьях подается в упрощенном виде, а какие-то нюансы просто игнорируются. Вследствие 
этого вам предстоит еще много самостоятельной работы, чтобы чувствовать себя действительно уверенно в рассматриваемых 
темах.

Но от новичков обычно и не ожидают глубокого понимания в данном направлении, что позволяет растянуть этот процесс по 
времени и подходить к темам итеративно - по мере роста опыта и закрепления ранее изученной информации.

#### На сегодня все!

![img.png](../../../commonmedia/justTheoryFooter.png)

> Если что-то непонятно или не получается – welcome в комменты к посту или в лс:)
>
> Канал: https://t.me/ViamSupervadetVadens
>
> Мой тг: https://t.me/ironicMotherfucker
>
> **Дорогу осилит идущий!**


[Next Lesson](../138/Cookies.%20Session.md)
