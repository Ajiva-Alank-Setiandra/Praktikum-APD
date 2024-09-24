#pilihan gender
genderp = ("P = Pria")
genderw = ("W = Wanita")
print(genderp)
print(genderw)
GD = str(input("Pilihlah gender mu, cukup ketik W atau P : "))
if GD not in ["W", "P"]:
    print("Input Invalid")

#masukan BB, TB, Umur
print("Masukan berat badan, tinggi badan, dan umur mu : ")
bb = int(input("Masukan berat badan (gram/gr) = "))
tb = float(input("Masukan tinggi badan anda (kilometer/km) = "))
umur = int(input("Masukan umur = "))

#Masukan jenis aktivitas
akt1 = ("a. Aktivitas kecil")
akt2 = ("b. Aktivitas sedang/medium")
akt3 = ("c. Aktivitas berat/besar")
print(akt1)
print(akt2)
print(akt3)
aktp = input("Masukan jenis aktivtas harian yang anda lakukan dengan menggunakan a/b/c = ")

#masukan rumus
BMRP = (0.01 * bb) + (62500 * tb) - (5 * umur) + 5
BMRW = (0.01 * bb) + (62500 * tb) - (5 * umur) - 161

#proses perhitungan
if GD == "P":
    if aktp == "a":
        tdee = BMRP * 1.25
    elif aktp == "b":
        tdee = BMRP * 1.36
    elif aktp == "c":
        tdee = BMRP * 1.72
    else:
        print("Invalid")

if GD == "W":
    if aktp == "a":
        tdee = BMRW * 1.25
    elif aktp == "b":
        tdee = BMRW * 1.36
    elif aktp == "c":
        tdee = BMRW * 1.72
    else:
        print("Invalid")

print( )
print(GD)
print(bb)
print(tb)
print(umur)
print(aktp)
print("Total kebutuhan kalori harian (TDEE) adalah = ")
print(tdee)