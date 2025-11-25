from collections import Counter

input_file = "dataset.txt"

# -------- Первая фаза: считаем частоты --------

counter = Counter()
total = 0

with open(input_file, "r") as f:
    for line in f:
        seq = line.strip()
        if seq:
            counter[seq] += 1
            total += 1

# список: (seq, count, prob)
stats = [(seq, count, (count / total) * 100) for seq, count in counter.items()]

# сортировка по частоте (count), убывание
stats.sort(key=lambda x: x[1], reverse=True)

# -------- Вторая фаза: создаём result_full.txt --------
#
# ВНИМАНИЕ:
# Для миллионов строк лучше НЕ выводить каждый индекс,
# это создаст огромный файл.
# Вместо индексов выводим:
#  - последовательность
#  - сколько раз встретилась
#  - вероятность

with open("result_full.txt", "w") as f:
    f.write("Sequence\tCount\tProbability(%)\n")
    for seq, count, prob in stats:
        f.write(f"{seq}\t{count}\t{prob:.6f}\n")

# -------- Третий файл --------

with open("result_numbers.txt", "w") as f:
    for seq, count, prob in stats:
        f.write(f"{seq}\n")

print("Готово! Файлы result_full.txt и result_numbers.txt созданы.")