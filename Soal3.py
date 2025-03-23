def cetak_tabel(baris, kolom):
    for angka in range(1, baris * kolom + 1):
        if angka % kolom == 0:
            print(angka, end=" ")
            print(" ")
        else:
            print(angka, end=" ")

jumlah_baris = int(input("Masukkan suatu bilangan untuk menentukan tinggi: "))
jumlah_kolom = int(input("Masukkan suatu bilangan untuk menentukan lebar: "))
cetak_tabel(jumlah_baris, jumlah_kolom)
