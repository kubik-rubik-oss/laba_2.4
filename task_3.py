try:
    numbers = list(map(int, input("Введите числа через пробел: ").split()))
except ValueError:
    print("Ошибка: введите числа!")
    exit()

with open("resourse/count.txt", "w") as file:
    file.write(" ".join(map(str, numbers)) + "\n")

x = 73 ** 2 + 29
temp_path = "resourse/count_tmp.txt"

with open("resourse/count.txt", "r") as src, open(temp_path, "w") as tmp:
    for line in src:
        processed = []
        for token in line.split():
            num = int(token)
            if num % 7 == 0:
                num = round(num * 100 / x, 2)
            processed.append(str(num))
        tmp.write(" ".join(processed) + "\n")

with open(temp_path, "r") as tmp, open("resourse/count.txt", "w") as dst:
    for line in tmp:
        dst.write(line)

print("Файл успешно обработан.")