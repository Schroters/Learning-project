# https://stepik.org/lesson/3363/step/4?unit=1135
# Программа, которая считывает исходный файл с подобной структурой,
# для каждого абитуриента записывает его среднюю оценку по трём предметам на отдельной строке,
# соответствующей этому абитуриенту, в файл с ответом.
# Также в последней строке средние баллы по математике, физике и русскому языку по всем абитуриентам


mas = []    # общий список со всеми
with open(r"dataset.txt", 'r') as file:
    for line in file:
        line = line.split(';')
        mas = mas + [line]

sumas = len(mas)    # количество студентов
zermas = int(0)       # ноль счетчик по списку
mint, fint, rint = int(0), int(0), int(0) # математика физика русский
omint, ofint, orint = int(0),int(0),int(0) # сумма по предмету
mastud = []             # общий массив с средним балом каждого студента
comstud = int(0)        # средний бал студента
stcomstud = str(comstud)    # стринговый средний бал студента

with open('output.txt', 'w') as auf:
    auf.write(stcomstud)

while zermas < sumas:
    mint = int(mas[zermas][1])
    fint = int(mas[zermas][2])
    rint = int(mas[zermas][3])
    omint += mint
    ofint += fint
    orint += rint
    comstud = (mint + fint + rint) / 3      # средний бал студента
    stcomstud = str(comstud)                # стринговый средний бал студента
    mastud += [stcomstud]                   # добавляем в общий массив

    zermas += 1

omint = str(omint / sumas)  # среднее по мате
ofint = str(ofint /sumas)
orint = str(orint /sumas)

obh = omint + ' ' + ofint + ' ' + orint     # строчка с всеми тремя общими средними
mastud += [obh]     # добавили в общий массив

with open(r"output.txt", "w") as file:
    for line in mastud:
        file.write(line + '\n')