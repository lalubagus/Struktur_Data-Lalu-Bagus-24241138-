print("Nama:Lalu Bagus Adi Kusuma Wijaya Nim : 24241138")

inputUser = int(input("masukan angka yang bernilai kurang dari 24 atau lebih besar dari 38:"))

#+++++24-------------
#memeriksa angka kurang dari 24
iskurangdari = (inputUser <24)

#memeriksa angka lebih dari 33
islebihdari = (inputUser >38)

final = iskurangdari or islebihdari
print("angka yang anda masukan :",final)