Распарсить json файлы, преобразовав их в одну таблицу, которая имеет поля:
1.	Item 
2.	SalePriceBeforePromo
3.	SalePriceTimePromo
4.	DatePriceBeforePromo
5.	ObjCode
6.	DiscountType
7.	DiscountValue
8.	DateBegin
9.	DateEnd
10.	PWCcode
11.	Value
12.	FirstValue
13.	LessOrEqual
14.	File (имя json файла, из которого представлена строчка данных)

Результатом выполнения скрипта должна быть таблица эксель

Комментарий: 
1.	Скрипт должен быть написан на языке python, можно использовать любые библиотеки
2.	Необходимо обработать исключения, если в json-структуре нет указанного поля, вставив в таблицу значение None
3.	Результат необходимо экспортировать в эксель файл result.xlsx
4.	Будут проверяться как script.py, так и result.xlsx
