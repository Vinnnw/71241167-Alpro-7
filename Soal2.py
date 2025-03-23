def deret_angka(n):
    for i in range(n, 0, -1):
        faktorial = 1
        for j in range(1, i + 1):
            faktorial *= j
        deret = ' '.join(str(x) for x in range(i, 0, -1))
        print(f"{faktorial} {deret}")
n = int(input("Masukkan nilai n: "))
deret_angka(n)
