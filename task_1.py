# Дана последовательность чисел.
# Получить список уникальных элементов заданной последовательности.
# ​Пример:​[1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]​

import random


incoming_list = [1, 2, 3, 5, 1, 5, 3, 10]
outcoming_list2 = list(filter(lambda x: incoming_list.count(x) == 1, incoming_list))

print(outcoming_list2)