sisi = float(input("Masukkan sisi persegi: "))
pilihan = input("pilih luas/keliling: ")
rumus = {"luas": sisi * sisi, "keliling": 4 * sisi}
print(rumus[pilihan])
