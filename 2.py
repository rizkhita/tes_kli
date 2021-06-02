# 2. Buatlah sebuah program yang menghasilkan 100 baris angka,
# berurutan dari 1 sampai dengan 100.
# Apabila sebuah angka habis dibagi 3, maka tampilkan kata Fizz di sebelahnya.
# Jika angkanya habis dibagi 5, tampilkan kata Buzz di sebelahnya.
# Bila angka tersebut habis dibagi 3 dan habis dibagi 5, tampilkan kata FizzBuzz di sebelah angka tersebut.

for i in range(100):
    if i % 3 == 0 and i % 5 == 0:
        print(str(i) + "-> FizzBuzz")
        continue
    elif i % 3 == 0:
        print(str(i) + "-> Fizz")
        continue
    elif i % 5 == 0:
        print(str(i) + "-> Buzz")
        continue
    else:
        print(str(i))