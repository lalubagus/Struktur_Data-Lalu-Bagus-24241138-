import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_simple_table(headers, rows):
    """Fungsi untuk mencetak tabel sederhana tanpa border"""
    col_widths = [len(str(header)) for header in headers]
    for row in rows:
        for i, cell in enumerate(row):
            if len(str(cell)) > col_widths[i]:
                col_widths[i] = len(str(cell))

    header_row = "  ".join(f"{str(header):<{col_widths[i]}}" for i, header in enumerate(headers))
    print(header_row)
    print("-" * len(header_row))
    for row in rows:
        print("  ".join(f"{str(cell):<{col_widths[i]}}" for i, cell in enumerate(row)))

def print_kelompok():
    print("\nKELOMPOK:\n")
    print_simple_table(["Nama", "NIM"], [
        ["Lalu Bagus Adi Kusuma Wijaya", "24241138"],
        ["Hasan Wirayuda", "24241133"],
        ["Ahmad Arsyi Sazali", "24241119"],
    ])

def tugas1():
    clear()
    print("\nTUGAS 1: Logika Boolean\n")

    print("Tabel Kebenaran NOT:")
    print_simple_table(["Input", "NOT"], [
        [False, not False],
        [True, not True]
    ])

    print("\nTabel Kebenaran AND:")
    print_simple_table(["AND", "False", "True"], [
        ["False", False and False, False and True],
        ["True", True and False, True and True]
    ])

    print("\nTabel Kebenaran OR:")
    print_simple_table(["OR", "False", "True"], [
        ["False", False or False, False or True],
        ["True", True or False, True or True]
    ])

    print("\nTabel Kebenaran XOR:")
    print_simple_table(["XOR", "False", "True"], [
        ["False", False ^ False, False ^ True],
        ["True", True ^ False, True ^ True]
    ])

def tugas2():
    clear()
    print("\nTUGAS 2: Logika Input Angka\n")
    print("Nama: Lalu Bagus Adi Kusuma Wijaya")
    print("NIM: 24241138")
    print("Nama: Hasan Wirayuda")
    print("Nim: 24241133")
    print("Nama: Ahmad Arsyi Sazali")
    print("Nim: 24241119")

    while True:
        try:
            inputUser = int(input("\nMasukkan angka yang bernilai kurang dari 24 atau lebih dari 38: "))
            break
        except ValueError:
            print("Harap masukkan angka yang valid!")

    iskurangdari = (inputUser < 24)
    islebihdari = (inputUser > 38)
    final = iskurangdari or islebihdari

    print("\nHasil Pengecekan:")
    print_simple_table(["Kondisi", "Hasil"], [
        ["Angka < 24", iskurangdari],
        ["Angka > 38", islebihdari],
        ["Valid (OR kondisi)", final]
    ])

def tugas3():
    clear()
    print("\nTUGAS 3: Nilai Kuliah\n")

    while True:
        try:
            nilai = float(input("Masukkan nilai Anda (0-100): "))
            if 0 <= nilai <= 100:
                break
            print("Nilai harus antara 0-100!")
        except ValueError:
            print("Harap masukkan angka yang valid!")

    print("\nKonversi Nilai:")
    print_simple_table(["Rentang Nilai", "Grade"], [
        [">= 85", "A"],
        ["80 - 84", "A-"],
        ["75 - 79", "B+"],
        ["70 - 74", "B"],
        ["65 - 69", "B-"],
        ["60 - 64", "C+"],
        ["55 - 59", "C"],
        ["50 - 54", "C-"],
        ["40 - 49", "D"],
        ["< 40", "E"]
    ])

    print("\nHasil Konversi:")
    if nilai > 100 or nilai < 0:
        grade = "Tidak valid"
    elif nilai >= 85:
        grade = "A"
    elif nilai >= 80:
        grade = "A-"
    elif nilai >= 75:
        grade = "B+"
    elif nilai >= 70:
        grade = "B"
    elif nilai >= 65:
        grade = "B-"
    elif nilai >= 60:
        grade = "C+"
    elif nilai >= 55:
        grade = "C"
    elif nilai >= 50:
        grade = "C-"
    elif nilai >= 40:
        grade = "D"
    else:
        grade = "E"

    print_simple_table(["Nilai Anda", "Grade"], [[nilai, grade]])

def tugas4():
    clear()
    print("\nTUGAS 4: Cek Umur\n")

    while True:
        try:
            umur = int(input("Masukkan umur: "))
            break
        except ValueError:
            print("Harap masukkan angka yang valid!")

    kategori = "Anak-anak" if umur < 18 else "Dewasa"
    print("\nHasil Kategori Umur:")
    print_simple_table(["Umur", "Kategori"], [[umur, kategori]])

def tugas5():
    clear()
    print("\nTUGAS 5: Cek Password\n")

    password = input("Masukkan password: ")
    panjang = len(password)
    valid = "Lolos" if panjang >= 8 else "Tidak Lolos"

    print("\nHasil Validasi Password:")
    print_simple_table(["Kriteria", "Hasil"], [
        ["Panjang Password", panjang],
        ["Validasi", valid]
    ])

def tugas6():
    clear()
    print("\nTUGAS 6: String Angka\n")

    number = "1234567890"

    print("\nManipulasi String:")
    print_simple_table(["Operasi", "Hasil"], [
        ["Data terakhir", number[-1]],
        ["Data pertama", number[0]],
        ["Data ke-3 sampai 6", number[2:6]]
    ])

def tugas7():
    clear()
    print("\nTUGAS 7: Pemisah Domain\n")

    domain = input("Masukkan domain (contoh: bagus.com): ")
    bagian = domain.partition(".")

    print("\nHasil Pemisahan Domain:")
    print_simple_table(["Komponen", "Nilai"], [
        ["Domain lengkap", domain],
        ["Nama domain", bagian[0]],
        ["Ekstensi domain", bagian[2]]
    ])

def tugas8():
    clear()
    print("\nTUGAS 8: Pembulatan Harga\n")

    harga_normal = 15.5935
    harga_diskon = 16.45987
    harga_retail = 14.96884

    print("\nHasil Pembulatan Harga:")
    print_simple_table(["Jenis Harga", "1 Desimal", "2 Desimal"], [
        ["Harga Normal", round(harga_normal, 1), round(harga_normal, 2)],
        ["Harga Diskon", round(harga_diskon, 1), round(harga_diskon, 2)],
        ["Harga Retail", round(harga_retail, 1), round(harga_retail, 2)]
    ])

def main():
    clear()
    while True:
        print_kelompok()
        print("\nMENU UTAMA\n")
        print_simple_table(["No", "Program"], [
            ["1", "Logika Boolean"],
            ["2", "Logika Input Angka"],
            ["3", "Nilai Kuliah"],
            ["4", "Cek Umur"],
            ["5", "Validasi Password"],
            ["6", "Manipulasi String"],
            ["7", "Pemisah Domain"],
            ["8", "Pembulatan Harga"],
            ["0", "Keluar"]
        ])

        try:
            pilihan = input("\nPilih nomor tugas (0-8): ")
            if pilihan == '1':
                tugas1()
            elif pilihan == '2':
                tugas2()
            elif pilihan == '3':
                tugas3()
            elif pilihan == '4':
                tugas4()
            elif pilihan == '5':
                tugas5()
            elif pilihan == '6':
                tugas6()
            elif pilihan == '7':
                tugas7()
            elif pilihan == '8':
                tugas8()
            elif pilihan == '0':
                print("\nTerima kasih telah menggunakan program kami!")
                break
            else:
                print("Pilihan tidak valid!")
        except Exception as e:
            print(f"Terjadi error: {e}")

        input("\nTekan Enter untuk kembali ke menu utama...")
        clear()

if __name__ == "__main__":
    main()
