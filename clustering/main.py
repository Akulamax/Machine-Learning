from function import *
from Data_file import *
from K_means_file import *
from Ierarhic_file import *
from K_medium_file import *
import stddraw

test = matrix_to_complex(generation_test2())  # если test1 - изменить количество кластеров (2), если test2 - (2), если test3 - (2)
# data_arr = []  # будущий массив с данными
# data_arr = generation(data_arr)  # генерация этого массива
data_arr = separation(test)
data_learning = learning_data(data_arr[1])  # массив с данными для дообучения, разбитый на группы
data_main = data_arr[0]  # массив с данными для первого прохода
data = Data(data_main)
print(data_main)
data_sample = data.sample()  # выборка данных для иерархической кластеризации

stddraw.setCanvasSize(CANVAS, CANVAS)
stddraw.setYscale(0, CANVAS)
stddraw.setXscale(0, CANVAS)
for i in range(len(data_main)):
    stddraw.point(data_main[i][0][0], data_main[i][0][1])
stddraw.show(10000)

for i in range(len(data_sample)):
    stddraw.setPenColor(stddraw.GREEN)
    stddraw.point(data_sample[i][0][0], data_sample[i][0][1])
stddraw.show(1000)

ierarhic = Ierarhic(data_sample)
clasters = ierarhic.Ierarhic1()  # иерархическая кластеризация, итог - массив с кластерами
centers_of_clasters = Ierarhic2(clasters)  # центры полученных кластеров
print(clasters)
print(centers_of_clasters)
parametr = check(clasters, centers_of_clasters)  # проверка на вложенность кластеров: если вложены, то False иначе True
print(parametr)
while parametr == -1:
    data_sample = data.sample()  # выборка данных для иерархической кластеризации
    ierarhic = Ierarhic(data_sample)
    clasters = ierarhic.Ierarhic1()  # иерархическая кластеризация, итог - массив с кластерами
    centers_of_clasters = Ierarhic2(clasters)  # центры полученных кластеров
    print(clasters)
    print(centers_of_clasters)
    parametr = check(clasters, centers_of_clasters)
    print(parametr)

k_means = K_means(matrix_to_simple(data_main), centers_of_clasters)
ierarhic_main = Ierarhic(data_main)

if parametr:
    while 1:
        answer1 = k_means.K_means()
        k_means2 = K_means(matrix_to_simple(data_main), answer1)
        answer0 = k_means2.K_means()
        if answer0 == answer1:
            break
        k_means = K_means(matrix_to_simple(data_main), answer0)
    print(answer1)  # вывод центров кластеров
    center = answer1
    for i in range(len(answer1)):
        stddraw.setPenColor(stddraw.RED)
        stddraw.setPenRadius(0.01)
        stddraw.point(answer1[i][0], answer1[i][1])
    stddraw.show(10000)
    k_means = K_means(matrix_to_simple(data_main), center)
    cluster = k_means.K_means_cluster()
    print(cluster)
    print(len(cluster[0]), len(cluster[1]))
    for i in range(len(cluster[0])):
        stddraw.setPenColor(stddraw.BLACK)
        stddraw.setPenRadius(0.01)
        stddraw.point(cluster[0][i][0], cluster[0][i][1])
    stddraw.show(10000)
    for i in range(len(cluster[1])):
        stddraw.setPenColor(stddraw.BLUE)
        stddraw.setPenRadius(0.01)
        stddraw.point(cluster[1][i][0], cluster[1][i][1])
    stddraw.show(10000)
    count = 0
    for arr in cluster:
        count += 1
        stddraw.setPenColor(stddraw.BOOK_RED)
        if count == 2:
            stddraw.setPenColor(stddraw.RED)
        for i in range(len(grahamscan(arr))):
            #print(grahamscan(arr), 'graham')
            stddraw.setPenRadius(0.005)
            stddraw.point(grahamscan(arr)[i][0], grahamscan(arr)[i][1])
            if i > 1:
                stddraw.line(grahamscan(arr)[i - 1][0], grahamscan(arr)[i - 1][1], grahamscan(arr)[i][0],
                             grahamscan(arr)[i][1])
        stddraw.line(grahamscan(arr)[0][0], grahamscan(arr)[0][1], grahamscan(arr)[len(grahamscan(arr)) - 1][0],
                     grahamscan(arr)[len(grahamscan(arr)) - 1][1])
        stddraw.line(grahamscan(arr)[0][0], grahamscan(arr)[0][1], grahamscan(arr)[1][0],
                     grahamscan(arr)[1][1])
    stddraw.show(10000)
else:
    cluster = ierarhic_main.Ierarhic1()
    answer2 = Ierarhic2(cluster)
    print(answer2)  # вывод центров кластеров
    center = answer2
    for i in range(len(answer2)):
        stddraw.setPenColor(stddraw.RED)
        stddraw.setPenRadius(0.01)
        stddraw.point(answer2[i][0], answer2[i][1])
    stddraw.show(10000)

    ###

    for i in range(len(cluster[0])):
        stddraw.setPenColor(stddraw.BLACK)
        stddraw.setPenRadius(0.005)
        stddraw.point(cluster[0][i][0], cluster[0][i][1])
    stddraw.show(10000)
    for i in range(len(cluster[1])):
        stddraw.setPenColor(stddraw.BLUE)
        stddraw.setPenRadius(0.005)
        stddraw.point(cluster[1][i][0], cluster[1][i][1])
    stddraw.show(10000)
    print(cluster)
    count = 0
    for arr in cluster:
        count += 1
        stddraw.setPenColor(stddraw.BOOK_RED)
        if count == 2:
            stddraw.setPenColor(stddraw.RED)
        for i in range(len(grahamscan(arr))):
            # print(grahamscan(arr), 'graham')
            stddraw.setPenRadius(0.005)
            stddraw.point(grahamscan(arr)[i][0], grahamscan(arr)[i][1])
            if i > 1:
                stddraw.line(grahamscan(arr)[i - 1][0], grahamscan(arr)[i - 1][1], grahamscan(arr)[i][0],
                             grahamscan(arr)[i][1])
        stddraw.line(grahamscan(arr)[0][0], grahamscan(arr)[0][1], grahamscan(arr)[len(grahamscan(arr)) - 1][0],
                     grahamscan(arr)[len(grahamscan(arr)) - 1][1])
        stddraw.line(grahamscan(arr)[0][0], grahamscan(arr)[0][1], grahamscan(arr)[1][0],
                     grahamscan(arr)[1][1])
stddraw.show(10000)

"""
проверка для k средних: разделение исходного массива на 2/3 и 1/3 
"""
data_to_k_medium = []
print(len(data_arr[0]), data_arr[0])
for i in range(100):
    data_to_k_medium.append(data_arr[0][i])
data_to_k_medium = matrix_to_simple(data_to_k_medium)
print(data_to_k_medium)
print(len(data_to_k_medium))
for j in range(len(data_to_k_medium)):
    stddraw.setPenColor(stddraw.GREEN)
    stddraw.setPenRadius(0.005)
    stddraw.point(data_to_k_medium[j][0], data_to_k_medium[j][1])
stddraw.show(10000)
result = K_medium(data_to_k_medium, cluster, 10)
print(result)
stddraw.show(10000)

# дообучение
for i in range(len(data_learning)):
    stddraw.clear()
    data_main = learning_matrix(data_main, data_learning[i])
    for j in range(len(data_main)):
        stddraw.setPenColor(stddraw.BLACK)
        stddraw.setPenRadius(0.005)
        stddraw.point(data_main[j][0][0], data_main[j][0][1])
    stddraw.show(10000)
    ierarhic_main = Ierarhic(data_main)
    if parametr:
        k_means = K_means(matrix_to_simple(data_main), answer1)
        while 1:
            answer1 = k_means.K_means()
            k_means2 = K_means(matrix_to_simple(data_main), answer1)
            answer0 = k_means2.K_means()
            if answer0 == answer1:
                break
            k_means = K_means(matrix_to_simple(data_main), answer0)
        print(answer1)  # вывод центров кластеров
        for i in range(len(answer1)):
            stddraw.setPenColor(stddraw.BLUE)
            stddraw.setPenRadius(0.01)
            stddraw.point(answer1[i][0], answer1[i][1])
        stddraw.show(10000)
    else:
        cluster = ierarhic_main.Ierarhic1()
        answer2 = Ierarhic2(cluster)
        print(answer2)  # вывод центров кластеров
        for i in range(len(answer2)):
            stddraw.setPenColor(stddraw.RED)
            stddraw.setPenRadius(0.01)
            stddraw.point(answer2[i][0], answer2[i][1])
        stddraw.show(10000)
stddraw.show()
