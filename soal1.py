def prima(angka):
    if angka <= 1:
        return False
    for i in range(2, angka):
        if angka % i == 0:
            return False
    return True
def primaTerdekat(n):
    lebihKecil = n - 1
    while lebihKecil >= 2:
        if prima(lebihKecil):
            primaTerdekatKecil = lebihKecil
            break
        lebihKecil -= 1
    else:
        primaTerdekatKecil = None
    lebihBesar = n + 1
    while True:
        if prima(lebihBesar):
            primaTerdekatBesar = lebihBesar
            break
        lebihBesar += 1
    if primaTerdekatKecil is None:
        return primaTerdekatBesar
    elif n - primaTerdekatKecil >= n - primaTerdekatBesar:
        return primaTerdekatKecil
    else:
        return primaTerdekatBesar
n = int(input("Masukkan suatu bilangan: "))
prima = primaTerdekat(n)
print(f"Bilangan prima terdekat dari {n} adalah {prima}")
