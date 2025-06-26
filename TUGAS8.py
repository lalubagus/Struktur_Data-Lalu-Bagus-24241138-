# Mendefinisikan harga
harga_normal = 15.5935
harga_diskon = 16.45987
harga_retail = 14.96884

# Mengambil satu digit di belakang koma
harga_normal_satu_digit = round(harga_normal, 1)
harga_diskon_satu_digit = round(harga_diskon, 1)
harga_retail_satu_digit = round(harga_retail, 1)

# Mengambil dua digit di belakang koma
harga_normal_dua_digit = round(harga_normal, 2)
harga_diskon_dua_digit = round(harga_diskon, 2)
harga_retail_dua_digit = round(harga_retail, 2)

# Menampilkan hasil
print(f"Harga Normal (1 digit): {harga_normal_satu_digit}")
print(f"Harga Diskon (1 digit): {harga_diskon_satu_digit}")
print(f"Harga Retail (1 digit): {harga_retail_satu_digit}")

print(f"Harga Normal (2 digit): {harga_normal_dua_digit}")
print(f"Harga Diskon (2 digit): {harga_diskon_dua_digit}")
print(f"Harga Retail (2 digit): {harga_retail_dua_digit}")