import pandas as pd                 # анализ данных
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html
import numpy as np                  # математика
import matplotlib.pyplot as plt     # для визуализации
import seaborn as sns               # для визуализации
# https://seaborn.pydata.org/generated/seaborn.violinplot.html
from sklearn import tree            # для обучения решающих деревьев и использовать их для предсказания, обучения моделей и т.д.


pd.set_option('display.max_columns', 20)    # далее три строки для того, что бы вывод не сжимался можно NONE
pd.set_option('display.max_rows', 1200)
pd.set_option('display.width', 200)
#plt.rcParams["figure.figsize"] = (30, 3) # (w, h) Что бы квадраты при рисовании делева не наезжали друг на друга ретина
plt.figure(figsize=(30, 3))         # еще способ тот же самый, что и выше

students_perfomance = pd.read_csv('table/StudentsPerformance.csv')
# прочитать csv так же по read можно много увиедть, что возможно прочесть
titanik_t = pd.read_csv('table/titanic.csv')
hell = pd.read_csv('table/column_hell.csv')
dota = pd.read_csv('table/dota_hero_stats.csv')
lupu = pd.read_csv('table/accountancy.csv')
concentrations = pd.read_csv('table/algae.csv')
income = pd.read_csv('table/income.csv')
dataset_209770_6 = pd.read_csv('table/dataset_209770_6.txt', sep=" ")
genome_matrix = pd.read_csv('table/genome_matrix.csv', index_col=0)
# что бы правильно расставить индексы строк (как в оригинале, не добавлять столб с нумирацией строк),
# нужно указать index_col=0
iris = pd.read_csv('table/iris.csv')
my_stat_old = pd.read_csv('table/my_stat.csv')
my_stat = pd.read_csv('table/my_stat_1.csv')
events_data = pd.read_csv('table/event_data_train.zip')     # открытие из архива
submissions_data = pd.read_csv('table/submissions_data_train.zip')
# events_train.csv - данные о действиях, которые совершают студенты со стэпами
# 1. step_id - id стэпа                         # 198
# 2. user_id - анонимизированный id юзера       # 19234
# 3. timestamp - время наступления события в формате unix date
# 4. action - событие, возможные значения:
# - discovered - пользователь перешел на стэп
# - viewed - просмотр шага,
# - started_attempt - начало попытки решить шаг, ранее нужно было явно нажать на кнопку - начать решение,
# перед тем как приступить к решению практического шага
# - passed - удачное решение практического шага

# submissions_train.csv - данные о времени и статусах сабмитов к практическим заданиям
# 1. step_id - id стэпа
# 2. timestamp - время отправки решения в формате unix date
# 3. submission_status - статус решения
# 4. user_id - анонимизированный id юзера


students_perfomance_with_names = students_perfomance.iloc[[0, 3, 4, 7, 8]]
# сделали копию таблицы в новую и именно то с чем планируем работать и оригинал останется не изменным
students_perfomance_with_names.index = ['Cersey', 'Tywin', 'Gregor', 'Joffrey', 'Lil Payene']  # назвали индексы в новой
my_series1 = pd.Series([1, 2, 3])   # создали серию
my_series1 = pd.Series([1, 2, 3], index=['Cersey', 'Tywin', 'Gregor'])
my_series2 = pd.Series([4, 5, 6], index=['Cersey', 'Tywin', 'Gregor'])
my_dataframe = pd.DataFrame({'col_name_1':my_series1, 'col name 2':my_series2})     # создали датафрейм из серий
diab = {'type' : ['A', 'A', 'B', 'B',], 'value' : [10, 14, 12, 23]}     # словарь из него легко создать датафрейм
my_data_frame = pd.DataFrame({'type' : ['A', 'A', 'B', 'B'], 'value': [10, 14, 12, 23]})
# либо сразу словарь в датафрейме

#-----



print("\n Вывод / Печать")
print(students_perfomance) # вывод всей таблицы
print(students_perfomance.head(2))   # вывод первых строчек
print(students_perfomance.tail(4))     # вывод последних строк
print(students_perfomance.head())       # пустой, значит вывод пяти строк
print(students_perfomance.iloc[0:3, 0:5])   # вывод четырех строчек и трех столбцов
print(students_perfomance.iloc[[0, 3, 10], [0, 5, -1]])     # Вывод конкретных строк и столбцов (даже последнйи с конца)
print(students_perfomance.iloc[[0, 3, 4, 7, 8]])    # вывод определенных строк
subset_1 = my_stat_old.iloc[0:10, [0, 2]]
print(students_perfomance_with_names.loc[['Cersey', 'Joffrey']])                        # вывод по новым индексам
print(students_perfomance_with_names.loc[['Cersey', 'Joffrey'], ['gender', 'lunch']])  # вывод по названию столбцов и колонок
print(students_perfomance_with_names.iloc[:, 0])    # отображение серии и первого столбца
# Выражение df.loc[:6] затронет все индексы от начала до компонента 6, включая шестерку: [0, 1, 2, 3, 4, 5, 6]
# А выражение df.iloc[:6] затронет все индексы от начала и до компонента 6, не включая шестерку: [0, 1, 2, 3, 4, 5]
print(students_perfomance_with_names['gender'])    # получим просто серию (возьми то что лежит по значению гендер)
print(students_perfomance_with_names[['gender']])  # получим датафрейм (возьми от всего датафрейма только первую колонку)
print(students_perfomance_with_names['gender'])    # будет просто пять, а тут размер списка
print(students_perfomance_with_names[['gender']].shape)     # будет 5 строчек и 1 столбец

# В переменную с именем subset_1 сохраните только первые 10 строк и только 1 и 3 колонку.
# В переменную с именем subset_2 сохраните все строки кроме 1 и 5 и только 2 и 4 колонку.
subset_1 = my_stat_old.iloc[0:10, [0, 2]]
bad_df = my_stat_old.index.isin([0, 4])      # перечесление ненужных строк
subset_2 = my_stat_old[~bad_df]             # вывод без тех двух строк указанных выше
subset_2 = subset_2.drop(['V1', 'V3'], axis=1)     # удаление не нужных столбцов

print(students_perfomance.gender)   # печать колонки Гендер (это серия)
# print(students_perfomance.writing score) через точку нельзя, так как в названии пробел
print(students_perfomance['writing score'])     # с пробелом вот так вывод колонки
print(students_perfomance.gender == 'female')   # еще одна серия где тру, где правильное значение
# отбор только тех строк, которые соответствуют
print(students_perfomance.loc[students_perfomance.gender == 'female'])  # одинаковые способы
print(students_perfomance[students_perfomance.gender == 'female'])      # одинаковые способы
print(students_perfomance.loc[students_perfomance['lunch'] == 'free/reduced'])  # вывод отсортированной таблицы
print(students_perfomance[students_perfomance['lunch'] == 'free/reduced'])      # вывод отсортированной таблицы
# отбор только тех строк и столбца, которые соответствуют
print(students_perfomance.loc[students_perfomance.gender == 'female', ['gender', 'writing score']])

# Сортировка по двум колонкам и в конце выдача количества строк (2 type)
print(students_perfomance[(students_perfomance['writing score'] > 95) & (students_perfomance.gender == 'female')])  # первый способ
print('Amount:', len(students_perfomance[(students_perfomance['writing score'] > 95) & (students_perfomance.gender == 'female')]))
# -- 2 --
print(students_perfomance.loc[(students_perfomance['writing score'] > 95) & (students_perfomance.gender == 'female')])  # второй способ
print('Amount:',len(students_perfomance.loc[(students_perfomance['writing score'] > 95) & (students_perfomance.gender == 'female')]))

print(students_perfomance.query('writing_score > 96'))      # вывод всех строк с отсортированными показателями
print(students_perfomance.query("gender == 'female'"))      # тоже вывод, и так как строка тоже в кавычки
print(students_perfomance.query("writing_score > 96 & gender == 'female'")) # комбинирование через И - &
print(students_perfomance.query("writing_score > 96 | gender == 'female'")) # комбинирование через ИЛИ - |
subset_1 = my_stat_old.query("V1 > 0 & V3 == 'A'")  # сохранить в новый датасет только подходящие значения И
subset_2 = my_stat_old.query("V2 != 10 | V4 >= 1")  # сохранить в новый датасет только подходящие значения ИЛИ
wrat_scor_quer = 99 # если с переменной, то есть @
print(students_perfomance.query("writing_score > @wrat_scor_quer & gender == 'female'"))  # если с переменной, то @

# создали список столбцов в которых есть слове score
score_columns = [i for i in list(students_perfomance) if 'score' in i]
print(students_perfomance[score_columns].head())  # вывод столбцов только с score
# 2
print(students_perfomance.filter(like='score').head())  # тоже самое просто родное и короче
print(students_perfomance.filter(like='degree', axis=0))    # axis=0 по строчкам axis=1 по столбцам (по умолчанию)
print(students_perfomance.filter(items=['reading_score']).head())   # отбор по конкретному названию
#-----


print('\n Размеры таблицы')
print(students_perfomance.shape)    # увидеть количество строк и колонок
print(students_perfomance.size)     # размер всей таблицы 8*1000
print(titanik_t.info())             # инфо о таблице
print(titanik_t.shape)    # увидеть количество строк и колонок
print(len(titanik_t))     # количество строк
print(len(titanik_t.index))  # количество строк
print(titanik_t.shape[0])    # количество строк
print(titanik_t.shape[1])    # количество столбцов
print(len(titanik_t.select_dtypes(include=['float64'])))    # количество строк float64
print(titanik_t.dtypes.value_counts())                      # количество и типы столбцов
print(titanik_t.dtypes[titanik_t.dtypes=='float64'].count())  # подсчет столбцов определенного типа
print(titanik_t.dtypes[titanik_t.dtypes=='int64'].count())    # подсчет столбцов определенного типа
print(titanik_t.dtypes[titanik_t.dtypes=='object'].count())   # подсчет столбцов определенного типа
print(dota[dota['legs'] == 8].shape[0])                     # подсчет сколько героев с восьмю ногами
print(dota['legs'].value_counts())                          # подсчет сколько героев с восьмю ногами
print(dota.aggregate({'legs': 'value_counts'}).sort_index())    # подсчет сколько героев с восьмю ногами КРАСИВО
print(dota.groupby('legs').count())                         # подсчет сколько героев с восьмю ногами
#-----



print('\n Среднее значения и показатели и типы данных')
print(students_perfomance.groupby('gender').aggregate({'writing score' : 'mean'})) # среднее значение writing score
print(students_perfomance.groupby('gender').aggregate({'math_score': 'mean', 'reading_score': 'mean'}))     # несколко значений
print(students_perfomance.groupby('gender').mean())         # среднее значение по трем предметам
# три колонки с групирующим значением, так как вариант выше сокрощает
print(students_perfomance.groupby('gender', as_index=False).aggregate({'math_score': 'mean', 'reading_score': 'mean'}))
# к варианту выше меняем название колонок Старый способ
print(students_perfomance.groupby('gender', as_index=False) \
      .aggregate({'math_score': 'mean', 'reading_score': 'mean'}) \
      .rename(columns={'math_score': 'mean_math_score', 'reading_score': 'mean_reading_score'}))
print(students_perfomance.groupby('gender', as_index=False)
      .aggregate({'math_score': ['mean', 'count', 'std'],'reading_score': ['std', 'min', 'max']})) # еще один способ
# переименовали табл прям в агрегате Рекомендуемый способ
print(students_perfomance.groupby('gender', as_index=False)
      .aggregate( mean_math_score=('math score', 'mean'), mean_reading_score=('reading score', 'mean')))
# еще можно с несколькими колонками, но тогда уже через список, и получится сортировка по грруппам и полу
print(students_perfomance.groupby(['gender', 'race/ethnicity'], as_index=False)
      .aggregate( mean_math_score=('math_score', 'mean'), mean_reading_score=('reading_score', 'mean')))

# подсчет по 5 и более столбцам среднего значений каждого из параметров
print(concentrations.groupby('genus').mean())

# задача узнать минимальное, максимальное и среднее значений для одного из аргументов колонки
print(concentrations.query('genus == "Fucus"').describe())          # вывод и среднего и меньшего и всего
# берем два показателя один в столбце, второй весь, потом берем агг, аргументы математические, роунд, цифр после запятой
print(concentrations.loc[concentrations.genus == 'Fucus', 'alanin'].agg(['min', 'mean', 'max']).round(2))
# еще одно решение
print(concentrations.groupby('genus').aggregate({'alanin' : ['mean' , 'min', 'max']}).round(2))
# Надо было узнать средие показатели по другим параметрам, при том по множеству
# создаем таблицу в которой количество, дисперсия и PTP (разница ежду мин и макс)
print(concentrations.groupby('group').aggregate(['count', 'var', np.ptp]).round(2))


# задача средние показатели по группам и вывод только нужных столбцов и убрать индексы
# 1
mean_session_value_data = my_stat.groupby("group",as_index=False).session_value.agg({'mean_session_value':'mean'})
# 2
mean_session_value_data = my_stat.groupby('group', as_index = False).agg({'session_value': 'mean'})
mean_session_value_data = mean_session_value_data.rename(columns={'session_value': 'mean_session_value'})
# 3
my_stat_1=my_stat.drop(['time', 'n_users'], axis=1)
mean_session_value_data = my_stat_1.groupby('group', as_index=False).mean()
mean_session_value_data = mean_session_value_data.rename(columns={'session_value':'mean_session_value'})



# Мультииндексы (индексы из нескольких уровней) НЕ рекомендуется
# Если в примере выше убрать аргумент as_index=False, то индекс стал бы сложным составным
mean_scores_multi = students_perfomance.groupby(['gender', 'race/ethnicity']) \
    .aggregate({'math_score': 'mean', 'reading_score': 'mean'}) \
    .rename(columns={'math_score': 'mean_math_score', 'reading_score': 'mean_reading_score'})
print(mean_scores_multi)
# вот так выглядит обращение к ним, мнгоуровневое
print(mean_scores_multi.loc[[('female', 'group A'), ('female', 'group B')]])
# К series можно применять методы, вывести все уникальные значения при помощи метода unique().
print(students_perfomance.math_score.unique())  # просто уникальные значения
print(students_perfomance.math_score.nunique()) # число уникальных значений
# Результат - сгруппированная серия - одномерный массив с информацией о группировке по двум переменным

print(events_data.groupby('day').user_id.nunique().head())      # сколько уникальных пользователей в день
events_data.groupby('day').user_id.nunique().plot(figsize=(20,10))  # что бы не смотреть в таблице рисуем график просто заменив head() на plot() а figsize=(20,10) что бы размер адекватным был

print(students_perfomance.groupby(['gender', 'race/ethnicity']).math_score.nunique())
# топ пять девушек по матемматике
print(students_perfomance.sort_values(['gender', 'math_score']))    # сортировка pandas от меньшего к большему
# сортировка pandas от большего к меньшему
print(students_perfomance.sort_values(['gender', 'math_score'], ascending=False))
# сортировка pandas от большего к меньшему по парням и девушкам топ 5 (вывод 10)
print(students_perfomance.sort_values(['gender', 'math_score'], ascending=False).groupby('gender').head())
# узнаем больший показатель и показываем кто больше заработал в категории 5 способов ниже
print(lupu.groupby(['Type', 'Executor']).mean())      # узнать в какой категории у кого больше показатели повторяются
# красивый способ в какой категории и у кого больше + сортировка
print(lupu.drop('Unnamed: 0', axis=1).groupby(['Type', 'Executor'], as_index=False)
      .mean().sort_values(['Type', 'Salary'], ascending=[True, False]).groupby('Type').head(1))
print(lupu.groupby(['Type','Executor']).mean().unstack())
print(lupu.pivot_table(values="Salary", index="Executor", columns="Type"))
print(lupu.groupby(['Executor', 'Type']).aggregate({'Salary': 'mean'}))

# Сортировка по нескольким значениям, что бы найти большее совпадение по двум колонкам
print('\n1\n', dota.groupby(['attack_type', 'primary_attr']).nunique())
print('\n2\n', dota.groupby(['attack_type','primary_attr']).size())
print('\n3\n', dota.filter(items=['attack_type','primary_attr']).mode())

print(students_perfomance.dtypes)   # что за типы данных в таблице (object (строки) int64 цифры)
# (мера того, насколько широко разбросаны точки данных относительно их среднего)
print(students_perfomance.describe())   # скорректированное стандартное отклонение выборки

print(students_perfomance['writing score'].mean())      # вывод среднего значения в колонке
# сортируем и выводим строки в которых выше среднего значений writing score
print(students_perfomance['writing score'].mean())      # вывод среднего значения в колонкее
mean_writitng_score = students_perfomance['writing score'].mean()   # среднее значение в переменную
print(students_perfomance.loc[students_perfomance['writing score'] > mean_writitng_score]) # первый способ с переменной
# второй без переменной
print(students_perfomance.loc[students_perfomance['writing score'] > students_perfomance['writing score'].mean()])
# объеденили два условия по сортировке
query_female = (students_perfomance.gender == 'female') & (students_perfomance['writing score'] > students_perfomance['writing score'].mean())
print((students_perfomance.gender == 'female') & (students_perfomance['writing score'] > students_perfomance['writing score'].mean()))
print(students_perfomance.loc[query_female])    # вывод отсортированной таблицы
# У какой доли студентов в колонке lunch указано free/reduced? СРЕДНЕЕ ЗНАЧЕНИЕ ПО ОБЩЕЙ
print(len(students_perfomance[students_perfomance['lunch'] == 'free/reduced']) / len(students_perfomance))
# среднее и дисперсия оценок по предметам у групп
print('--mean-- Среднее значение')
print(students_perfomance[students_perfomance['lunch'] == 'free/reduced'].mean())
print(students_perfomance[students_perfomance['lunch'] == 'standard'].mean())
print('--var-- Дисперсия')
print(students_perfomance[students_perfomance['lunch'] == 'free/reduced'].var())
print(students_perfomance[students_perfomance['lunch'] == 'standard'].var())
print('--light-- Легкие чужие версии')
print(students_perfomance.groupby('lunch').mean())  # что и выше, более аккуратный ввод
print(students_perfomance.groupby('lunch').var())   # что и выше, более аккуратный ввод
print(students_perfomance.groupby('lunch').agg(['mean', 'var']))
print('--describe-- Вывод всей инфы по данным параметрам')
print(students_perfomance[students_perfomance['lunch'] == 'free/reduced'].describe())
print(students_perfomance[students_perfomance['lunch'] == 'standard'].describe())

# подсчет размера повторяющихся ролей в строчке, в одном столбце
print(dota.roles.str.split(',').apply(len).mode())
print(dota['roles'].apply(lambda v: len(eval(v))).value_counts().head(1).index)
print((dota.roles.str.count(',') + 1).value_counts().idxmax())
print(dota.roles.str.split().str.len().hist())


# посчитаем количество степов на пользователя (passed тест сдан)
# 1 способ, не верный (так как пропустили студентов с нулями, около 2к)
# проходим по степу у которого решение тест сдал
# групируем по юзеру и скидываем индекс
# посчитаем число степов у которых был тест сдан
# переименоуем еще, что бы не было id а было колво
print(events_data[events_data.action == 'passed'] \
      .groupby('user_id', as_index=False) \
      .agg({'step_id': 'count'}) \
      .rename(columns={'step_id':'passed_steps'}).head())
# Вывод графика
events_data[events_data.action == 'passed'] \
    .groupby('user_id', as_index=False) \
    .agg({'step_id': 'count'}) \
    .rename(columns={'step_id':'passed_steps'}).passed_steps.hist()
# Вот тут видим, что потерлось значение НОЛЬ хотя по идее должны быть пользователи, которые не решили не единого степа
print(events_data[events_data.action == 'passed'] \
      .groupby('user_id', as_index=False) \
      .agg({'step_id': 'count'}) \
      .rename(columns={'step_id':'passed_steps'}).min())

# 2 способ если без решений ставим ноль, а не пропускаем
print(events_data.pivot_table(index='user_id', columns='action', values='step_id', aggfunc='count', fill_value=0).reset_index().head())
# index='user_id' в результате каждая строчка будет информацией о каждом уникальном index (в индексе мы указываем для кого будем вести счет)
# columns='action', столбцы будут отвеать за уникальные значения columns (колонка, в которой строки следует сделать столбцами)
# values='step_id', в ячейках будет находиться информация по values (указывается, что будем считать, в нашем случае это степы)( у шага step_id есть статус (viewed/passed/discovered/start.))
# aggfunc='count',  сгруппированная по aggfunc (указываем функцию, которая будет обрабатывать данные колонки step_id и распределять их по viewed/passed/discovered/start.)
# fill_value - если у человека нету степа, заполняет значение нулем.
# в таблице мы увидим для каждого user id есть countы stepов которые были с значением экшен дискауерд


# подсчитаем для кадого юзера сколько у него было анных для которого правильно ответ
# для каждого юзера узнали сколько правильных и сколько не правильных
users_scores = submissions_data.pivot_table(index='user_id',
                                            columns='submission_status',
                                            values='step_id',
                                            aggfunc='count',
                                            fill_value=0).reset_index().head()



#-----



print('\n Форматирование')
# Изменение названия столбцов, что бы без пробелов
students_perfomance = students_perfomance.rename(columns=
                                                 {'parental level of education': 'parental_level_of_education',
                                                  'test preparation course': 'test_preparation_course',
                                                  'math score': 'math_score', 'reading score': 'reading_score',
                                                  'writing score': 'writing_score'})
# просто изменение названий вот
my_stat_old = my_stat_old.rename(columns={'V1': 'session_value', 'V2': 'group', 'V3': 'time', 'V4': 'n_users'})
# еще одно, но медленнее
my_stat_old.columns = ['session_value', 'group', 'time', 'n_users']
# самое быстрое изменение названий
my_stat_old.columns = {'session_value': 'V1', 'group': 'V2', 'time': 'V3', 'n_users': 'V4'}

my_stat = my_stat.fillna(0)     # замена пропущеных значений на нули
# 1 способ замена отрицательных чисел на медиан
my_stat.loc[my_stat.n_users < 0, 'n_users'] = my_stat.query("n_users >= 0").n_users.median()
# замена всех отрицат знач на медианное  ДФ форматируем [все меньше нуля] = все значения меньше или равно нулю в медиану
# 2 способ замена отрицательных чисел на медиан
my_stat.loc[my_stat.n_users < 0, 'n_users'] = my_stat[my_stat.n_users >= 0].n_users.median()
# 3 способ замена отрицательных чисел на медиан
my_stat.n_users.where(my_stat.n_users >= 0, my_stat.n_users[my_stat.n_users >= 0].median(), inplace=True)
# 4 способ замена отрицательных чисел на медиан
my_stat_2 = my_stat.query('n_users >= 0')
med = my_stat_2['n_users'].median()
my_stat.loc[my_stat['n_users'] < 0, 'n_users'] = med


# Создание и добавление новых колонок
# Первый способ в ЛОБ сумма всех трех предметов
# название старого датафрейма['название новой колонки'] = Любое значение
students_perfomance['total_score'] = students_perfomance.math_score + students_perfomance.reading_score + students_perfomance.writing_score
print(students_perfomance.head())
my_stat_old['V5'] = my_stat_old.V1 + my_stat_old.V4     # в новой колонке сумма двух других
my_stat_old['V6'] = np.log(my_stat_old.V2)          # натуральный логарифм переменной V2
# тоже самое что и выше В5 и В6
my_stat_old=my_stat_old.assign(V5 =my_stat_old.V1 + my_stat_old.V4, V6 = np.log(my_stat_old.V2))

# Второй способ, в котором можно несколько колонок создать, применяем логорифм к тоталскор
students_perfomance = students_perfomance.assign(total_score_log=np.log(students_perfomance.total_score))
print(students_perfomance.head())
# Удаление колонок, так можно и несоклько через запятую
students_perfomance = students_perfomance.drop(['total_score_log'], axis=1) # axis не название строчек, а название колонки что бы
print(students_perfomance.head())

# Удаление и столбцов и строк 1ый способ
bad_df = my_stat_old.index.isin([0, 4])      # перечесление ненужных строк
subset_2 = my_stat_old[~bad_df]             # вывод без тех двух строк указанных выше
subset_2 = subset_2.drop(['V1', 'V3'], axis=1)     # удаление не нужных столбцов
# 2 способ
subset_2= my_stat_old.iloc[:, [1, 3]].drop([0, 4])
# 3 способ
subset_2 = my_stat_old[['V2', 'V4']].drop(my_stat_old.index[[0, 4]])
# 4 способ
subset_2 = my_stat_old.iloc[:, [1, 3]].query('index != 0 and index != 4')


# Работа с временем timestamp(колво секунд с 70ого года)
events_data['date'] = pd.to_datetime(events_data.timestamp, unit='s')
# to_datetime - превращение норм время, unit = s то что в секундах, делаем новый столб с нормальным временем
events_data['day'] = events_data.date.dt.date           # добавили колонку только с датой

submissions_data['date'] = pd.to_datetime(submissions_data.timestamp, unit = 's')
submissions_data['day'] = submissions_data.date.dt.date
events_data['month'] = events_data['date'].dt.month     #из даты берем месяц, аналогично year, можно их же и объединить


# подсчитаем для кадого юзера сколько у него было анных для которого правильно ответ
users_scores = submissions_data.pivot_table(index='user_id',
                                            columns='submission_status',
                                            values='step_id',
                                            aggfunc='count',
                                            fill_value=0).reset_index().head()

print(users_scores.head())      # для каждого юзера узнали сколько правильных и сколько не правильных


# теперь надо рассчитать какие были промежутки между решениями
# посмотрим какие перерывы в среднем у юзеров и исходя из данных, какой промежуток, порог до дропа
# какие перерывы в днях между прохождением курсов
# drop_duplicates() убирает повторы если пусто в скобках убирает все повторы и может оставить очень мало
print(events_data[['user_id', 'day', 'timestamp']].drop_duplicates(subset=['user_id', 'day'])) # такая команда оставит для одного юзера один день когда он был онлайн
# соберем все таймстемпы в которые он был на курсе и посмотрим перерывы между ними
# c групируем по userID отберем колонку таймстемп применим apply(list) и получится список для каждого пользователя с его таймстемпом
# Для каждого пользователя находим уникальные таймстемпы
print(events_data[['user_id', 'day', 'timestamp']].drop_duplicates(subset=['user_id', 'day']) \
      .groupby('user_id')['timestamp'].apply(list).head())
# apply(np.diff) разница между наблюдениями и получается у 1 пользователя пусто, у второго у него два дня и между ними разница, а у третьего очень много
print(events_data[['user_id', 'day', 'timestamp']].drop_duplicates(subset=['user_id', 'day']) \
      .groupby('user_id')['timestamp'].apply(list) \
      .apply(np.diff).head())
# Для каждого пользователя находим разницу по времени между степами, получится эрэй эрээев
gap_data = events_data[['user_id', 'day', 'timestamp']].drop_duplicates(subset=['user_id', 'day']) \
    .groupby('user_id')['timestamp'].apply(list) \
    .apply(np.diff).values
# теперь взять эрэй эрээев и в один эрэй
# concatenate (передаем массив и даем ось (строки))
# вроде устарело gap_data = np.concatenate(gap_data, axis=0)
gap_data = pd.Series(np.hstack(gap_data))
# теперь в пандовской серии сохранены для каждого пользователя значения разницы двумя захода на курс


#-----



print('\n Визуализация')
# cоздаем гистограмму распределения по math_score стандартным методом hist(), в модуле пандас
print(students_perfomance.math_score.hist())
sns.set(rc={'figure.figsize': (9, 6)})      # что бы график был адекватного размера

# создание гистограммы, по самой повторяющейся строчке в столбце (roles)
sns.distplot([x.count(',')+1 for x in dota.roles], bins=15)
dota['roles'].agg(lambda x: len(x.split(','))).hist()
# 1 способ ОДИНАКОВЫЙ с следющим
sns.distplot([len(n.split(',')) for n in dota.roles])
# 2 способ ОДИНАКОВЫЙ с пердыдущим
roles = [len(i.split(', ')) for i in dota['roles']]
sns.distplot(roles)
# Краткий и понятный
(dota.roles.str.count(',') + 1).plot(kind='hist')
dota.roles.str.split().str.len().hist()
# Размер графика figsize=(20,10)
events_data.groupby('day').user_id.nunique().plot(figsize=(20, 10))

# несколько способов увидеть зависимость между несколькими столбцами на одном графике
# унимодальное - с одним горбом на линии тренда
# бимодальное - с двумя
# размах - дельта от минимального до максимального значения
sns.distplot(iris['petal width'], color="blue")
sns.distplot(iris['petal length'], color="green")
sns.distplot(iris['sepal width'], color="yellow")
sns.distplot(iris['sepal length'], color="orange")



for name in iris.filter(like='al').columns:
    sns.distplot(iris[name], label=name, hist=False)


# нариусем скотерклот? много точек на гарфике
students_perfomance.plot.scatter(x='math_score', y='reading_score')
dataset_209770_6.plot.scatter(x='x', y='y')
# нарисуем тоже самое, только более красивое и через библиотеку seaborn
sns.lmplot(x='math_score', y='reading_score', data=students_perfomance)
# Можно добавить на наш график группирующую переменную, например gender,
# и тогда мы покрасим наши точки в зависимости от значения переменной gender;
# добавим легенду на график и внутри каждй из групп добавим регресионную прямую.
sns.lmplot(x='math_score', y='reading_score', hue='gender', data=students_perfomance)
# А если мы хотим убрать регрессионную прямую с графика, то задаём аргумент fit_reg=False / зависимость кориляции переменной
sns.lmplot(x='math_score', y='reading_score', hue='gender', data=students_perfomance, fit_reg=False)
# Что бы изменять визуально график его следует сохранить в переменную и уже с переменной и использовать методы которые есть
ax = sns.lmplot(x='math_score', y='reading_score', hue='gender', data=students_perfomance, fit_reg=False)
ax.set_xlabels('Math score')    # переименовали названия
ax.set_ylabels('Reading score')  # переименовали названия

# Разные варианты создания эллементарного граика
income.plot(kind='line')
sns.lineplot(x=income.index, y=income.income)
income.plot()
plt.plot(income.index, income.income)
income['income'].plot()
income.income.plot()
sns.lineplot(data=income)
income.income.hist()
# есть еще множество других

# Создание тепловой карты
# https://datastart.ru/blog/read/seaborn-heatmaps-13-sposobov-nastroit-vizualizaciyu-matricy-korrelyacii
genome_matrix = sns.heatmap(data=genome_matrix, annot=True, cmap="viridis", linewidths=.5)
# в переменную = сеаборн.тепловаякарта(дата = таблица, аннот (помогает отобразить коэффициент корреляции, на квадратах цифры) = Тру,
# cmap(внешность) = viridis, linewidths(толщина границ) = .5 )
genome_matrix.xaxis.set_ticks_position('top')
genome_matrix.xaxis.set_tick_params(rotation=90)

# Violin плот
# https://seaborn.pydata.org/generated/seaborn.violinplot.html
# Два одинаковых способа
sns.violinplot(data=iris['petal length'], color="Purple")
sns.violinplot(y='petal length', data=iris, color="Purple")

# Pair плот
# https://seaborn.pydata.org/generated/seaborn.pairplot.html
# Все информации и гарфики на одном графике
sns.pairplot(iris,  vars=iris.columns[:-1], diag_kind='kde')    # каждый толбец на своем рисунке
sns.pairplot(iris)
sns.pairplot(data=iris, vars=iris.columns[:4], hue="species")
sns.pairplot(data=iris, hue='species', vars=['sepal length', 'sepal width', 'petal length', 'petal width'])



# посчитаем количество степов на пользователя (passed тест сдан)
# 1 способ, не верный (так как пропустили студентов с нулями, около 2к)
# проходим по степу у которого решение ТЕст сдал
# групируем по юзеру и скидываем индекс
# посчитаем число степов у которых был тест сдан
# переименоуем еще, что бы не было id а было колво
print(events_data[events_data.action == 'passed'] \
      .groupby('user_id', as_index=False) \
      .agg({'step_id': 'count'}) \
      .rename(columns={'step_id':'passed_steps'}).head())
# Вывод графика
events_data[events_data.action == 'passed'] \
    .groupby('user_id', as_index=False) \
    .agg({'step_id': 'count'}) \
    .rename(columns={'step_id':'passed_steps'}).passed_steps.hist()
# Вот тут видим, что потерлось значение НОЛЬ хотя по идее должны быть пользователи, которые не решили не единого степа
print(events_data[events_data.action == 'passed'] \
      .groupby('user_id', as_index=False) \
      .agg({'step_id': 'count'}) \
      .rename(columns={'step_id':'passed_steps'}).min())

# 2 способ есди без решений ставим ноль, а не пропускаем
print(events_data.pivot_table(index='user_id', columns='action', values='step_id', aggfunc='count', fill_value=0).reset_index().head())
# index='user_id' в результате каждая строчка будет информацией о каждом уникальном index (в индексе мы указываем для кого будем вести счет)
# columns='action', столбцы будут отвеать за уникальные значения columns (колонка, в которой строки следует сделать столбцами)
# values='step_id', в ячейках будет находиться информация по values (указывается, что будем считать, в нашем случае это степы)( у шага step_id есть статус (viewed/passed/discovered/start.))
# aggfunc='count',  сгруппированная по aggfunc (указываем функцию, которая будет обрабатывать данные колонки step_id и распределять их по viewed/passed/discovered/start.)
# fill_value - если у человека нету степа, заполняет значение нулем.
# в таблице мы увидим для каждого user id есть countы stepов которые были с значением экшен дискауерд

submissions_data['date'] = pd.to_datetime(submissions_data.timestamp, unit = 's')
submissions_data['day'] = submissions_data.date.dt.date

print(submissions_data.head())



# отображение графика
plt.show()