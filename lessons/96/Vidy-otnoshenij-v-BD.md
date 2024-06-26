![](../../commonmedia/header.png)

***

   

Виды отношений в БД
===================

Виды отношений в БД

С сегодняшнего урока мы начинаем погружение в DDL - статьи по DML опубликованы почти в полном объеме - осталось всего несколько статей..

В данной статье речь пойдет не об SQL, а о концепции, которую средствами SQL можно обеспечить - связи между таблицами и том, какие они бывают.

По сути, сама идея связанных таблиц достаточно проста - поскольку одна таблица, как правило, обозначает одну сущность, вполне логично, что между разными сущностями одной системы могут и должны быть связи.

  

Всего в рамках реляционных БД можно выделить 4 типа связей:

1.  **Многие-к-одному**. Она же **Many-to-One**, **M2O**;
2.  **Один-к-одному**. Она же **One-to-One**, **O2O**;
3.  **Один-ко-многим**. Она же **One-to-Many**, **O2M**;
4.  **Многие-ко-многим**. Она же **Many-to-Many**, **M2M**.

  

### Many-to-One

Вероятно, самый популярный тип связи. Им можно описать отношение квартир к многоквартирному дому, например: каждая из записей в уcловной таблице “квартиры” имеет связь с одним определенным домом.

Также сюда попадает отношение в древовидной структуре: несколько дочерних элементов имеют связь с одним родительским элементом. Это может быть актуально, когда связь записей происходит не между несколькими таблицами, а в рамках одной. Например, так можно было бы представить связи генеалогического древа в рамках таблицы “люди”.

  

### One-to-One

На первый взгляд может показаться, что это лишь частный случай Many-to-One. Но на самом деле это не так.

Связь O2O подразумевает, что один элемент имеет связь только с одним элементом. Тем самым закладывая контракт: больше одной связи быть не может. В случае с SQL есть механизм “ограничений” (**_constraint_**’ов), с помощью которого можно гарантировать: в рамках колонки (колонок), отвечающих за связь, будет лишь одно уникальное значение на всю таблицу, чтобы не было неявного превращения в M2O.

Также может показаться, что такая связь очень распространена - человек и паспорт (или идентификатор в паспорте), например.

Однако на практике такая связь не рекомендуется и используется достаточно редко. Еще реже (вероятно, почти никогда) такая связь обоснована, а не является ошибкой проектирования.

Причин у этого две:

1.  Логическая. Если сущность имеет в рамках системы только одну связь - такие сущности стоит объединить. В данном случае я говорю строго о проектировании в рамках реляционных БД - скажем, в Java-приложении O2O тоже встречается относительно нечасто, но там это может иметь смысл;
2.  Физическая. Связывание таблиц при SELECT-запросе требует вычислительных ресурсов на сопоставление записей. И для О2О связи гораздо выгоднее представить две связанные записи в качестве записи одной таблицы, чем при каждом запросе производить подобное сопоставление.

Однако у O2O есть и плюс, который может быть не очевидным: только этот тип связи позволяет сделать саму связь двусторонней: запись в первой таблице ссылается на запись во второй, а запись во второй - на запись в первой. Все остальные связи являются односторонними, так или иначе.

  

### One-to-Many

Эта связь, в свою очередь, является зеркальной к M2O.

Разница между ними исключительно логическая, поэтому отмечу лишь один момент: таблица, записи которой выступают в роли One никак не обозначают свою связь с записями из таблицы Many. Что может усложнить изучение зоны ответственности сущности исключительно по заданной таблице.

В качестве примера можно взять те же примеры, что и в M2O:

*   Отношение дома к квартирам, которые в нем расположены;
*   Отношение родительского элемента в древовидной иерархии к дочерним.

  

Помните: наличие частных случаев, когда в M2O или O2M связи записи связываются по принципу одна-к-одной - не делает такую связь O2O. Однако если все записи сводятся к этому принципу и логически невозможна ситуация, в которой одна запись получит более одной связи - стоит пересмотреть текущее решение, вероятно, была допущена ошибка проектирования.

  

### Many-to-Many

Достаточно тяжелый в обработке способ связи. Благо, не слишком частый.

Как можно догадаться, описывает ситуации, когда запись в первой таблице может иметь несколько связей с записями в второй, а запись во второй - несколько связей с записями в первой.

Пример: таблица “владельцы квартир” и таблица “квартиры”. Одной квартирой может владеть несколько человек, но и каждый человек может владеть более чем одной квартирой.

На практике такая связь реализуется через промежуточную таблицу, задача которой - хранить сами связи.

В таком случае связка выглядит так: первая таблица - промежуточная таблица, имеющая M2O связь с первой таблицей и M2O связь со второй - вторая таблица.

Необходимость построения связи через промежуточную таблицу делает саму связь достаточно дорогой - ведь при каждом запросе с участием связанной по М2М сущности нам нужно производить сопоставление (упомянутое в О2О) дважды. Однако, в отличии от О2О, это необходимое зло, поэтому подобные связи хоть и не слишком часты (просто в силу необходимости в них), но существуют.

  

На сегодня все!

В ближайших уроках мы разберем, как указывать связь между таблицами на уровне самих таблиц, а также изучим синтаксис, позволяющий связывать таблицы при получении данных.

![](../../commonmedia/footer.png)

Если что-то непонятно или не получается – welcome в комменты к посту или в лс:)

Канал: [https://t.me/ViamSupervadetVadens](https://t.me/ViamSupervadetVadens)

Мой тг: [https://t.me/ironicMotherfucker](https://t.me/ironicMotherfucker)

_Дорогу осилит идущий!_

[Next Lesson](../97/DML-JOIN.md)
