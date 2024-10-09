# daftar_buku = {
#      #key        #value
#     "buku1" : "harry poter",
#     "buku2" : "Percy jackson",
#     "buku3" : "twilight"
# }

# catatan, key tidak bileh sama, jika ada yang sama maka program akan mengambil key yang paling baru
# print(daftar_buku["buku2"])
# print(daftar_buku)

# biodata = {
#     "nama" : "aldy ramadhan syahputra", #string
#     "NIM" : "24091079", #int
#     "KRS" : ["prgram web", "struktur data", "basis data"], #list
#     "mahasiswa_aktif" : True, #bool
#     "social media" : { #dictionary
#         "instagram" : "@aldtrmdhns_",
#         "discord" : "\'Izanamai'#6848"
#         }
# }

# film = {
#     "avanger endgame" : "action",
#     "Sherlock holmes" : "mystery",
#     "the conjuring" : "horror"
# }
# print(film)
# del film["the conjuring"]
# hapus = film.pop("the conjuring")
# print(film)
# print(f"item yang di hapus = ")

# film.clear()
# print(film)


# film["zombieland"] = "comedy"  (kurung siku)
# print(film)

# film.update({"hour" : "thirller"})  (fungsi update)
# print(film)

# for i in biodata:
#     print(i)

# for i, j in biodata.items():
#     print(f"key = {i} dan value = {j}")

# for i in biodata:
#     print(biodata[i])

# print(biodata["alamat"])
# catatan, jika ada pemanggilana data, jika menggunakan kurung kotak, maka akan error, jika menggunakan kurung biasa akan terisi kata "none"
# print(biodata.get("alamat"))

# print(biodata.get("alamat", "kosong bang"))

# biodata = {
#     "nama" : "aldy ramadhan syahputra", #string
#     "NIM" : 24091079, #int
#     "KRS" : ["prgram web", "struktur data", "basis data"], #list
#     "mahasiswa_aktif" : True, #bool
#     "social media" : { #dictionary
#         "instagram" : "@aldtrmdhns_",
#         "discord" : "\'Izanamai'#6848"
#         }
# }

# print("jumlah data dalam dict biodata = ", len(biodata))
# pinjamdict =  biodata.copy()
# print(pinjamdict)

# key = "apel", "jeruk", "mangga"
# value = 1

# buah = dict.fromkeys(key, value)
# print(buah)

# film = {
#     "avanger endgame" : "action",
#     "Sherlock holmes" : "mystery",
#     "the conjuring" : "horror"
# }

# for i in film.keys():
#     print(i, end= " ")

# print(film)
# print("dilm : ", film.setdefault("oldbook", "horror"))
# print(film)

# musik = { 
# "The Chainsmoker" : ["All we Know", "The Paris"], 
# "Alan Walker" : ["Alone", "Lily"], 
# "Neffex" : ["Best of Me", "Memories"] 
# } 
# for i, j in musik.items():
#     print(f"musik milik {i} adalah : ")
#     for lagu in j:
#         print(lagu)
#     print("")

# mahasiswa = { 
# 101 : {"Nama" : "Aldy", "Umur" : 19}, 
# 111 : {"Nama" : "Abdul", "Umur" : 18} 
# } 

# print(f"mahasiswa : {mahasiswa}")
# del mahasiswa [111]["Umur"]
# print(f"sesudah : {mahasiswa}")

# print(f"mahasiswa : {mahasiswa}")
# mahasiswa[101]["angkatan"] = 2023
# print(f"sesudah : {mahasiswa}")

# for i, j in mahasiswa.items():
#     print(f"ID : {i}")
#     for keynested, valuenested in j.items():
#         print(f"{keynested} : {valuenested}")

# biodata = {
#     "nama" : "ken",
#     "umur" : 17,
#     "NIM" : "2409106015",
#     "jurusan" : "informatika",
#     "angkatan" : "2024"
# }

# print(biodata)
# print(biodata.get("NIM"))
# biodata.update({"umur" : "19"})
# print(biodata)

# Biodata = {}

# while True:
#     print("1. Tambah")
#     print("2. Tampilakan")
#     print("3. Exit")
#     pilihan =  int(input("(1/2/3) : "))

#     if pilihan == 1:
#         nama = input("Masukkan nama :")
#         umur = input("Masukkan umur :")
#         alamat = input("Masukkan alamat :")

#         Biodata[nama] = { 
#             'Umur' : umur,
#             'Alamat' : alamat
#         }

#     elif pilihan == 2:
#         for nama, info in Biodata.items():
#             print(f"Nama : {nama}")
#             print(f"Umur : {info['Umur']}")
#             print(f"Alamat : {info['Alamat']}")

#     elif pilihan == 3:
#         print("exit ...")
#         break

#     else:
#         print("Invalid ... ... ")