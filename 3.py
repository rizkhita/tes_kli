# 3. Buatlah sebuah program yang menghasilkan deret angka sederhana yang susunan angkanya merupakan penjumlahan dari dua angka sebelumnya (0,1,1,2,3,5,8,13,21)

numbers = [5, 10, 15, 20, 25, 30, 30]

for i in range(len(numbers)):
    if i == 0:
        print(numbers[i])
    else:
        print(numbers[i - 1] + numbers[i])