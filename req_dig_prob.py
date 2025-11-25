required_digits = {"1", "2", "3", "4"}
input_file = "dataset.txt"

total_lines = 0
counter = {}  # для подсчёта частоты подходящих чисел

with open(input_file, "r") as f:
    for line in f:
        seq = line.strip()
        if not seq:
            continue

        total_lines += 1

        # проверяем содержит ли число все цифры 0,1,2,5
        if required_digits.issubset(set(seq)):
            counter[seq] = counter.get(seq, 0) + 1

# -------- сортировка по вероятности --------
# делаем список формата (число, вероятность)
result = []
for seq, count in counter.items():
    prob = (count / total_lines) * 100
    result.append((seq, prob))

# сортируем от большего к меньшему
result.sort(key=lambda x: x[1], reverse=True)

# -------- вывод --------
print("Число\tВероятность")
for seq, prob in result:
    print(f"{seq}\t{prob:.6f}")