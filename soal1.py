def cek_prima(bilangan):
    if bilangan <= 1:
        return False
    for pembagi in range(2, bilangan):
        if bilangan % pembagi == 0:
            return False
    return True

def cari_prima_terdekat(target):
    prima_kecil = target - 1
    while prima_kecil >= 2:
        if cek_prima(prima_kecil):
            prima_terdekat_kecil = prima_kecil
            break
        prima_kecil -= 1
    else:
        prima_terdekat_kecil = None
    
    prima_besar = target + 1
    while True:
        if cek_prima(prima_besar):
            prima_terdekat_besar = prima_besar
            break
        prima_besar += 1
    
    if prima_terdekat_kecil is None:
        return prima_terdekat_besar
    elif target - prima_terdekat_kecil >= prima_terdekat_besar - target:
        return prima_terdekat_kecil
    else:
        return prima_terdekat_besar

bilangan_input = int(input("Masukkan suatu bilangan: "))
prima_terdekat = cari_prima_terdekat(bilangan_input)
print(f"Bilangan prima terdekat dari {bilangan_input} adalah {prima_terdekat}")
