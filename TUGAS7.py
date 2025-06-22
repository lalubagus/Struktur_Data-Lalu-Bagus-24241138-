# Program pemisah domain 

domain = input("Masukkan domain (contoh: bagus.com): ")
bagian = domain.partition(".")
print("Nama domain:", bagian[0])
print("Ekstensi domain:", bagian[2])