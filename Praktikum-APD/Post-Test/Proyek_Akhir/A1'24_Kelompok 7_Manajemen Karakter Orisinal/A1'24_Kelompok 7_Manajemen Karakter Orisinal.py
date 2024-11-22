# variabel global
karakter_info = {}
# Menyimpan username dan password
users = {
    'admin': 'admin123'
}
# penyimpanan user yang sedang login
users_aktif = None
# penyimpanan jenis-jenis MBTI
list_mbti = ["ISTJ", "ISFJ", "INFJ", "INTJ", "ISTP", "ISFP", "INFP", "INTP", "ESTP", "ESFP", "ENFP", "ENTP", "ESTJ", "ESFJ", "ENFJ", "ENTJ"]

# tampilan menu login
def menu_login():
    print( 
        """
                『Menu Login <3』


        ♦=============================﹁
        ✭⭒          [Menu]        ⋆✯.
        ⭒✧    ⋆                  ✭   .
            ➤⭒1. Registrasi         
        .   ➤⭒2. Login   .               
            ➤⭒3. Keluar       ✦ ⋆   ⭒✧             
        ✭ .        ✭⭒        .          
        ⭒✧    ⋆        .        ✭      
        ﹂=============================♦
        """
        )

# prosedur registrasi
def registrasi():
    try:
        username = input("Masukkan username: ")
        # pengecekan username
        if not username:
            raise ValueError('Username tidak boleh kosong, coba lagi.')
        if username in users:
            raise ValueError("Username sudah pernah terdaftar, silakan gunakan username lain.")
        
        password = input("Masukkan password: ")
        # pengecekan password
        if not password:
            raise ValueError('Password tidak boleh kosong, coba lagi.')
        
        # penyimpanan data di dictionary apabila registrasi berhasil
        users[username] = password
        print("Registrasi berhasil! Silakan login.")

    except ValueError as ve:
        print(ve)

# prosedur login
def login():
    try:
        global users_aktif
        username = input("Masukkan username: ")
        # pengecekan username
        if not username:
            raise ValueError('Username tidak boleh kosong, coba lagi.')
        
        password = input("Masukkan password: ")
        # pengecekan password
        if not password:
            raise ValueError('Password tidak boleh kosong, coba lagi.')

        # inputan pengguna sesuai
        if username in users and users[username] == password:
            users_aktif = username
            print(f"Selamat datang, {username}! Anda masuk sebagai {"admin" if username == "admin" else "user"}.")
            return True # login berhasil
        else:
            print("Username atau password tidak sesuai. Silakan coba lagi.")
            return False # login gagal
    except ValueError as ve:
        print(ve)

# tampilan menu program utama
def menu_kedua(peran):
    if peran == 'admin': # menu untuk admin
        print( """
            『Register Karakter <3』


        ♦=============================﹁
        ✭⭒          [Menu]        ⋆✯.
        ⭒✧    ⋆                  ✭   .
            ➤⭒1. Tambah Karakter          
        .   ➤⭒2. Tampilkan Karakter   .               
            ➤⭒3. Ubah Karakter        .
            ➤⭒4. Hapus Karakter     ✭
        .   ➤⭒5. Cek Interaksi    
        .   ➤⭒6. Logout       ✦ ⋆   ⭒✧             
        ✭ .        ✭⭒        .          
        ⭒✧    ⋆        .        ✭      
        ﹂=============================♦
        """
        )
    else: # menu untuk user
        print( 
        """
            『Register Karakter <3』


        ♦=============================﹁
        ✭⭒          [Menu]        ⋆✯.
        ⭒✧    ⋆                  ✭   .
            ➤⭒1. Tambah Karakter          
        .   ➤⭒2. Tampilkan Karakter   .               
            ➤⭒3. Cek Interaksi     ✭
        .   ➤⭒4. Logout        
        ✭ .        ✭⭒        .          
        ⭒✧    ⋆        .        ✭      
        ﹂=============================♦
        """
        )

# pembukaan
def intro():
    print(
    """
    Selamat datang di generator karakter orisinil!
    Disini kamu bisa melihat bagaimana interaksi antar karakter original-mu berdasarkan MBTI mereka!!
    """
    )
# mencari data di variabel global
def search(nama):
    if nama in karakter_info:
        return True
    else:
        return False
    
# sitem penambahan character
def add_data():
    try: 
        nama = input("Siapa nama karaktermu?: ") # variabel lokal
        if not nama: # pengecekan nama
            raise ValueError('Nama tidak boleh kosong, coba lagi.')

        umur = input("Berapa usia karaktermu?: ") # variabel lokal
        if not umur: # pengecekan umur
            raise ValueError('Umur tidak boleh kosong, coba lagi.')
        if not umur.isdigit():
            raise TypeError('Umur harus berupa angka, coba lagi.')
        
        gender = input("Apa jenis kelamin karaktermu?: ") # variabel lokal
        if not gender: # pengecekan jenis kelamin
            raise ValueError('Jenis kelamin tidak boleh kosong, coba lagi.')
        
        print("""
    Apabila kamu bingung atau tidak tahu jenis MBTI-mu, silahkan lakukan tes MBTI di link bawah ini:
                ⋆✯.     https://www.16personalities.com/id/tes-kepribadian        ⭒✧
        """)

        mbti = input("Masukkan MBTI karaktermu (isi dengan CAPSLOCK): ") # variabel lokal
        if not mbti: # pengecekan mbti
            raise ValueError('MBTI tidak boleh kosong, coba lagi.')
        
        print()
        karakter_info[nama] = {
            'umur' : umur,
            'gender' : gender,
            'mbti' : mbti
        }
    except ValueError as ve:
        print(ve)
    except TypeError as te:
        print(te)

# sistem pembacaan character
def read_data():
    if not karakter_info:
        print('Tidak ada karakter yang tersimpan.')
    else:
        for i, j in karakter_info.items():
            print(f"\nKarakter {i}\nNama : {i}\nUmur : {j['umur']}\nGender : {j['gender']} \nMBTI : {j['mbti']}")

# sistem update character
def update_data():
    try:
        nama_lama = input("Siapa karakter yang ingin kamu ubah?: ")
        if not nama_lama: # pengecekan inputan nama
            raise ValueError('Masukkan nama karaktermu yang ingin kamu ubah.')
        if not search(nama_lama):
            raise ValueError(f'Karakter {nama_lama} tidak ditemukan. Coba lagi.')
        
        nama_baru = input("Siapa nama baru dari karaktermu?: ")
        if not nama_baru: # pengecekan nama
            raise ValueError('Nama baru tidak boleh kosong, coba lagi.')
        
        umur_baru = input("Berapa umur karaktermu?: ")
        if not umur_baru: # pengecekan umur
            raise ValueError('Umur baru tidak boleh kosong, coba lagi.')
        if not umur_baru.isdigit():
            raise TypeError('Umur harus berupa angka, coba lagi.')
        
        gender_baru = input("Apa jenis kelamin karaktermu?: ")
        if not gender_baru: # pengecekan jenis kelamin
            raise ValueError('Jenis kelamin tidak boleh kosong, coba lagi.')
        
        mbti_baru = input("Apa MBTI baru karaktermu?: ")
        if not mbti_baru: # pengecekan mbti
            raise ValueError('MBTI tidak boleh kosong, coba lagi.')
        # pembaruan data pada variabel global
        karakter_info[nama_baru] = karakter_info.pop(nama_lama)
        karakter_info[nama_baru]['umur'] = umur_baru
        karakter_info[nama_baru]['gender'] = gender_baru
        karakter_info[nama_baru]['mbti'] = mbti_baru

        print(f'Karakter {nama_lama} berhasil diperbarui menjadi {nama_baru}!')

    except ValueError as ve:
        print(ve)
    except TypeError as te:
        print(te)

# sistem penghapusan character
def delete_data():
    try:
        nama_lama = input("Siapa karakter yang ingin kamu hapus?: ")
        if not nama_lama: # pengecekan inputan nama
            raise ValueError('Nama tidak boleh kosong, coba lagi.')
        if not search(nama_lama):
            raise ValueError(f'Karakter {nama_lama} tidak ditemukan. Coba lagi.')
        else:
            del karakter_info[nama_lama]
            print(f'Karakter {nama_lama} berhasil dihapus!')
    except ValueError as ve:
        print(ve)

# sistem pengecekan interkasi antar mbti karakter
def interaction():
    try:
        pro_mbti = input("Masukkan MBTI karakter (isi dengan CAPSLOCK): ")
        # pengecekan mbti pertama
        if not pro_mbti:
            raise ValueError('MBTI pertama tidak boleh kosong, coba lagi.')
        if pro_mbti not in list_mbti:
            raise ValueError('MBTI yang anda masukkan tidak sesuai, silahkan coba lagi.')
        
        con_mbti = input("Masukkan MBTI yang ingin kamu cek (isi dengan CAPSLOCK): ")
        # pengecekan mbti pembanding
        if not con_mbti:
            raise ValueError('MBTI kedua tidak boleh kosong, coba lagi.')
        if con_mbti not in list_mbti:
            raise ValueError('MBTI yang anda masukkan tidak sesuai, silahkan coba lagi.')

        # MBTI INFP
        # interaksi PERFECT
        if pro_mbti == "INFP" and con_mbti == "INFP":
            print("Interaksi mereka PERFECT")
        if pro_mbti == "INFP" and con_mbti == "ISFP":
            print("Interaksi mereka PERFECT")
        # interaksi GOOD
        if pro_mbti == "INFP" and con_mbti == "ENFP":
            print("Interaksi mereka GOOD")
        if pro_mbti == "INFP" and con_mbti == "INFJ":
            print("Interaksi mereka GOOD")
        if pro_mbti == "INFP" and con_mbti == "ENFJ":
            print("Interaksi mereka GOOD")
        if pro_mbti == "INFP" and con_mbti == "INTJ":
            print("Interaksi mereka GOOD")
        if pro_mbti == "INFP" and con_mbti == "ENTJ":
            print("Interaksi mereka GOOD")
        if pro_mbti == "INFP" and con_mbti == "INTP":
            print("Interaksi mereka GOOD")
        if pro_mbti == "INFP" and con_mbti == "ENTP":
            print("Interaksi mereka GOOD")
        # interaksi WORST
        if pro_mbti == "INFP" and con_mbti == "ESFP":
            print("Interaksi mereka WORST")
        if pro_mbti == "INFP" and con_mbti == "ISTP":
            print("Interaksi mereka WORST")
        if pro_mbti == "INFP" and con_mbti == "ESTP":
            print("Interaksi mereka WORST")
        if pro_mbti == "INFP" and con_mbti == "ISFJ":
            print("Interaksi mereka WORST")
        if pro_mbti == "INFP" and con_mbti == "ESFJ":
            print("Interaksi mereka WORST")
        if pro_mbti == "INFP" and con_mbti == "ISTJ":
            print("Interaksi mereka WORST")
        if pro_mbti == "INFP" and con_mbti == "ESTJ":
            print("Interaksi mereka WORST")

        # MBTI ENFP
        # interaksi PERFECT
        if pro_mbti == "ENFP" and con_mbti == "INFJ":
            print("Interaksi mereka PERFECT")
        if pro_mbti == "ENFP" and con_mbti == "INTJ":
            print("Interaksi mereka PERFECT")
        # interaksi GOOD
        if pro_mbti == "ENFP" and con_mbti == "INFP":
            print("Interaksi mereka GOOD")
        if pro_mbti == "ENFP" and con_mbti == "ENFP":
            print("Interaksi mereka GOOD")
        if pro_mbti == "ENFP" and con_mbti == "ENFJ":
            print("Interaksi mereka GOOD")
        if pro_mbti == "ENFP" and con_mbti == "ENTJ":
            print("TInteraksi mereka GOOD")
        if pro_mbti == "ENFP" and con_mbti == "INTP":
            print("Interaksi mereka GOOD")
        if pro_mbti == "ENFP" and con_mbti == "ENTP":
            print("Interaksi mereka GOOD")
        # interaksi WORST
        if pro_mbti == "ENFP" and con_mbti == "ISFP":
            print("Interaksi mereka WORST")
        if pro_mbti == "ENFP" and con_mbti == "ESFP":
            print("Interaksi mereka WORST")
        if pro_mbti == "ENFP" and con_mbti == "ISTP":
            print("Interaksi mereka WORST")
        if pro_mbti == "ENFP" and con_mbti == "ESTP":
            print("Interaksi mereka WORST")
        if pro_mbti == "ENFP" and con_mbti == "ISFJ":
            print("Interaksi mereka WORST")
        if pro_mbti == "ENFP" and con_mbti == "ESFJ":
            print("Interaksi mereka WORST")
        if pro_mbti == "ENFP" and con_mbti == "ISTJ":
            print("Interaksi mereka WORST")
        if pro_mbti == "ENFP" and con_mbti == "ESTJ":
            print("Interaksi mereka WORST")

        # MBTI INFJ
        # interaksi PERFECT
        if pro_mbti == "INFJ" and con_mbti == "ENFP":
            print("Interaksi mereka PERFECT")
        if pro_mbti == "INFJ" and con_mbti == "ENTP":
            print("Interaksi mereka PERFECT")
        # interaksi GOOD
        if pro_mbti == "INFJ" and con_mbti == "INFP":
            print("Interaksi mereka GOOD")
        if pro_mbti == "INFJ" and con_mbti == "INFJ":
            print("Interaksi mereka GOOD")
        if pro_mbti == "INFJ" and con_mbti == "ENFJ":
            print("Interaksi mereka GOOD")
        if pro_mbti == "INFJ" and con_mbti == "INTJ":
            print("Interaksi mereka GOOD")
        if pro_mbti == "INFJ" and con_mbti == "ENTJ":
            print("Interaksi mereka GOOD")
        if pro_mbti == "INFJ" and con_mbti == "INTP":
            print("Interaksi mereka GOOD")
        # interaksi WORST
        if pro_mbti == "INFJ" and con_mbti == "ISFP":
            print("Interaksi mereka WORST")
        if pro_mbti == "INFJ" and con_mbti == "ESFP":
            print("Interaksi mereka WORST")
        if pro_mbti == "INFJ" and con_mbti == "ISTP":
            print("Interaksi mereka WORST")
        if pro_mbti == "INFJ" and con_mbti == "ESTP":
            print("Interaksi mereka WORST")
        if pro_mbti == "INFJ" and con_mbti == "ISFJ":
            print("Interaksi mereka WORST")
        if pro_mbti == "INFJ" and con_mbti == "ESFJ":
            print("Interaksi mereka WORST")
        if pro_mbti == "INFJ" and con_mbti == "ISTJ":
            print("Interaksi mereka WORST")
        if pro_mbti == "INFJ" and con_mbti == "ESTJ":
            print("Interaksi mereka WORST")

        # MBTI ENFJ
        # interaksi PERFECT
        if pro_mbti == "ENFJ" and con_mbti == "ENFP":
            print("Interaksi mereka PERFECT")
        if pro_mbti == "ENFJ" and con_mbti == "ENTP":
            print("Interaksi mereka PERFECT")
        # interaksi GOOD
        if pro_mbti == "ENFJ" and con_mbti == "INFP":
            print("Interaksi mereka GOOD")
        if pro_mbti == "ENFJ" and con_mbti == "INFJ":
            print("Interaksi mereka GOOD")
        if pro_mbti == "ENFJ" and con_mbti == "ENFJ":
            print("Interaksi mereka GOOD")
        if pro_mbti == "ENFJ" and con_mbti == "INTJ":
            print("Interaksi mereka GOOD")
        if pro_mbti == "ENFJ" and con_mbti == "ENTJ":
            print("Interaksi mereka GOOD")
        if pro_mbti == "ENFJ" and con_mbti == "INTP":
            print("Interaksi mereka GOOD")
        # interaksi WORST
        if pro_mbti == "ENFJ" and con_mbti == "ISFP":
            print("Interaksi mereka WORST")
        if pro_mbti == "ENFJ" and con_mbti == "ESFP":
            print("Interaksi mereka WORST")
        if pro_mbti == "ENFJ" and con_mbti == "ISTP":
            print("Interaksi mereka WORST")
        if pro_mbti == "ENFJ" and con_mbti == "ESTP":
            print("Interaksi mereka WORST")
        if pro_mbti == "ENFJ" and con_mbti == "ISFJ":
            print("Interaksi mereka WORST")
        if pro_mbti == "ENFJ" and con_mbti == "ESFJ":
            print("Interaksi mereka WORST")
        if pro_mbti == "ENFJ" and con_mbti == "ISTJ":
            print("Interaksi mereka WORST")
        if pro_mbti == "ENFJ" and con_mbti == "ESTJ":
            print("Interaksi mereka WORST")

        # MBTI INTJ
        # interaksi PERFECT
        if pro_mbti == "INTJ" and con_mbti == "ENFP":
            print("Interaksi mereka PERFECT")
        if pro_mbti == "INTJ" and con_mbti == "ENTP":
            print("Interaksi mereka PERFECT")
        # interaksi GOOD
        if pro_mbti == "INTJ" and con_mbti == "INFP":
            print("Interaksi mereka GOOD")
        if pro_mbti == "INTJ" and con_mbti == "INFJ":
            print("Interaksi mereka GOOD")
        if pro_mbti == "INTJ" and con_mbti == "ENFJ":
            print("Interaksi mereka GOOD")
        if pro_mbti == "INTJ" and con_mbti == "INTJ":
            print("Interaksi mereka GOOD")
        if pro_mbti == "INTJ" and con_mbti == "ENTJ":
            print("Interaksi mereka GOOD")
        if pro_mbti == "INTJ" and con_mbti == "INTP":
            print("Interaksi mereka GOOD")
        # interaksi NORMAL
        if pro_mbti == "INTJ" and con_mbti == "ISFP":
            print("Interaksi mereka NORMAL")
        if pro_mbti == "INTJ" and con_mbti == "ESFP":
            print("Interaksi mereka NORMAL")
        if pro_mbti == "INTJ" and con_mbti == "ISTP":
            print("Interaksi mereka NORMAL")
        if pro_mbti == "INTJ" and con_mbti == "ESTP":
            print("Interaksi mereka NORMAL")
        # interaksi BAD
        if pro_mbti == "INTJ" and con_mbti == "ISFJ":
            print("Interaksi mereka BAD")
        if pro_mbti == "INTJ" and con_mbti == "ESFJ":
            print("Interaksi mereka BAD")
        if pro_mbti == "INTJ" and con_mbti == "ISTJ":
            print("Interaksi mereka BAD")
        if pro_mbti == "INTJ" and con_mbti == "ESTJ":
            print("Interaksi mereka BAD")

        # MBTI ENTJ
        # interaksi PERFECT
        if pro_mbti == "ENTJ" and con_mbti == "INFP":
            print("Interaksi mereka PERFECT")
        if pro_mbti == "ENTJ" and con_mbti == "INTP":
            print("Interaksi mereka PERFECT")
        # interaksi GOOD
        if pro_mbti == "ENTJ" and con_mbti == "ENFP":
            print("Interaksi mereka GOOD")
        if pro_mbti == "ENTJ" and con_mbti == "INFJ":
            print("Interaksi mereka GOOD")
        if pro_mbti == "ENTJ" and con_mbti == "ENFJ":
            print("Interaksi mereka GOOD")
        if pro_mbti == "ENTJ" and con_mbti == "INTJ":
            print("Interaksi mereka GOOD")
        if pro_mbti == "ENTJ" and con_mbti == "ENTJ":
            print("Interaksi mereka GOOD")
        if pro_mbti == "ENTJ" and con_mbti == "ENTP":
            print("Interaksi mereka GOOD")
        # interaksi NORMAL
        if pro_mbti == "ENTJ" and con_mbti == "ISFP":
            print("Interaksi mereka NORMAL")
        if pro_mbti == "ENTJ" and con_mbti == "ESFP":
            print("Interaksi mereka NORMAL")
        if pro_mbti == "ENTJ" and con_mbti == "ISTP":
            print("Interaksi mereka NORMAL")
        if pro_mbti == "ENTJ" and con_mbti == "ESTP":
            print("Interaksi mereka NORMAL")
        if pro_mbti == "ENTJ" and con_mbti == "ISFJ":
            print("Interaksi mereka NORMAL")
        if pro_mbti == "ENTJ" and con_mbti == "ESFJ":
            print("Interaksi mereka NORMAL")
        if pro_mbti == "INTJ" and con_mbti == "ISTJ":
            print("Interaksi mereka NORMAL")
        if pro_mbti == "ENTJ" and con_mbti == "ESTJ":
            print("Interaksi mereka NORMAL")

        # MBTI INTP
        # interaksi PERFECT
        if pro_mbti == "INTP" and con_mbti == "INFP":
            print("Interaksi mereka PERFECT")
        if pro_mbti == "INTP" and con_mbti == "ENTJ":
            print("Interaksi mereka PERFECT")
        if pro_mbti == "INTP" and con_mbti == "ESTJ":
            print("Interaksi mereka PERFECT")
        # interaksi GOOD
        if pro_mbti == "INTP" and con_mbti == "ENFP":
            print("Interaksi mereka GOOD")
        if pro_mbti == "INTP" and con_mbti == "INFJ":
            print("Interaksi mereka GOOD")
        if pro_mbti == "INTP" and con_mbti == "ENFJ":
            print("Interaksi mereka GOOD")
        if pro_mbti == "INTP" and con_mbti == "INTJ":
            print("Interaksi mereka GOOD")
        if pro_mbti == "INTP" and con_mbti == "INTP":
            print("Interaksi mereka GOOD")
        if pro_mbti == "INTP" and con_mbti == "ENTP":
            print("Interaksi mereka GOOD")
        # interaksi NORMAL
        if pro_mbti == "INTP" and con_mbti == "ISFP":
            print("Interaksi mereka NORMAL")
        if pro_mbti == "INTP" and con_mbti == "ESFP":
            print("Interaksi mereka NORMAL")
        if pro_mbti == "INTP" and con_mbti == "ISTP":
            print("Interaksi mereka NORMAL")
        if pro_mbti == "INTP" and con_mbti == "ESTP":
            print("Interaksi mereka NORMAL")
        # interaksi BAD
        if pro_mbti == "INTP" and con_mbti == "ISFJ":
            print("Interaksi mereka BAD")
        if pro_mbti == "INTP" and con_mbti == "ESFJ":
            print("Interaksi mereka BAD")
        if pro_mbti == "INTP" and con_mbti == "ISTJ":
            print("Interaksi mereka BAD")

        # MBTI ENTP
        # interaksi PERFECT
        if pro_mbti == "ENTP" and con_mbti == "INFJ":
            print("Interaksi mereka PERFECT")
        if pro_mbti == "ENTP" and con_mbti == "INTJ":
            print("Interaksi mereka PERFECT")
        # interaksi GOOD
        if pro_mbti == "ENTP" and con_mbti == "INFP":
            print("Interaksi mereka GOOD")
        if pro_mbti == "ENTP" and con_mbti == "ENFP":
            print("Interaksi mereka GOOD")
        if pro_mbti == "ENTP" and con_mbti == "ENFJ":
            print("Interaksi mereka GOOD")
        if pro_mbti == "ENTP" and con_mbti == "ENTJ":
            print("Interaksi mereka GOOD")
        if pro_mbti == "ENTP" and con_mbti == "INTP":
            print("Interaksi mereka GOOD")
        if pro_mbti == "ENTP" and con_mbti == "ENTP":
            print("Interaksi mereka GOOD")
        # interaksi NORMAL
        if pro_mbti == "ENTP" and con_mbti == "ISFP":
            print("Interaksi mereka NORMAL")
        if pro_mbti == "ENTP" and con_mbti == "ESFP":
            print("Interaksi mereka NORMAL")
        if pro_mbti == "ENTP" and con_mbti == "ISTP":
            print("Interaksi mereka NORMAL")
        if pro_mbti == "ENTP" and con_mbti == "ESTP":
            print("TInteraksi mereka NORMAL")
        # interaksi BAD
        if pro_mbti == "ENTP" and con_mbti == "ISFJ":
            print("Interaksi mereka BAD")
        if pro_mbti == "ENTP" and con_mbti == "ESFJ":
            print("Interaksi mereka BAD")
        if pro_mbti == "ENTP" and con_mbti == "ISTJ":
            print("Interaksi mereka BAD")
        if pro_mbti == "ENTP" and con_mbti == "ESTJ":
            print("Interaksi mereka BAD")

        # MBTI ISFP
        # interaksi PERFECT
        if pro_mbti == "ISFP" and con_mbti == "ENFJ":
            print("Interaksi mereka PERFECT")
        if pro_mbti == "ISFP" and con_mbti == "ESFJ":
            print("Interaksi mereka PERFECT")
        if pro_mbti == "ISFP" and con_mbti == "ESTJ":
            print("Interaksi mereka PERFECT")
        # interaksi NORMAL
        if pro_mbti == "ISFP" and con_mbti == "INTJ":
            print("Interaksi mereka NORMAL")
        if pro_mbti == "ISFP" and con_mbti == "ENTJ":
            print("Interaksi mereka NORMAL")
        if pro_mbti == "ISFP" and con_mbti == "INTP":
            print("Interaksi mereka NORMAL")
        if pro_mbti == "ISFP" and con_mbti == "ENTP":
            print("Interaksi mereka NORMAL")
        if pro_mbti == "ISFP" and con_mbti == "ISFJ":
            print("Interaksi mereka NORMAL")
        if pro_mbti == "ISFP" and con_mbti == "ISTJ":
            print("Interaksi mereka NORMAL")
        # interaksi BAD
        if pro_mbti == "ISFP" and con_mbti == "ISFP":
            print("Interaksi mereka BAD")
        if pro_mbti == "ISFP" and con_mbti == "ESFP":
            print("Interaksi mereka BAD")
        if pro_mbti == "ISFP" and con_mbti == "ISTP":
            print("Interaksi mereka BAD")
        if pro_mbti == "ISFP" and con_mbti == "ESTP":
            print("Interaksi mereka BAD")
        # interaksi WORST
        if pro_mbti == "ISFP" and con_mbti == "INFP":
            print("Interaksi mereka WORST")
        if pro_mbti == "ISFP" and con_mbti == "ENFP":
            print("Interaksi mereka WORST")
        if pro_mbti == "ISFP" and con_mbti == "INFJ":
            print("Interaksi mereka WORST")

        # MBTI ESFP
        # interaksi PERFECT
        if pro_mbti == "ESFP" and con_mbti == "ISFJ":
            print("Interaksi mereka PERFECT")
        if pro_mbti == "ESFP" and con_mbti == "ISTJ":
            print("Interaksi mereka PERFECT")
        # interaksi NORMAL
        if pro_mbti == "ESFP" and con_mbti == "INTJ":
            print("Interaksi mereka NORMAL")
        if pro_mbti == "ESFP" and con_mbti == "ENTJ":
            print("Interaksi mereka NORMAL")
        if pro_mbti == "ESFP" and con_mbti == "INTP":
            print("Interaksi mereka NORMAL")
        if pro_mbti == "ESFP" and con_mbti == "ENTP":
            print("Interaksi mereka NORMAL")
        if pro_mbti == "ESFP" and con_mbti == "ESFJ":
            print("Interaksi mereka NORMAL")
        if pro_mbti == "ESFP" and con_mbti == "ESTJ":
            print("Interaksi mereka NORMAL")
        # interaksi BAD
        if pro_mbti == "ESFP" and con_mbti == "ISFP":
            print("Interaksi mereka BAD")
        if pro_mbti == "ESFP" and con_mbti == "ESFP":
            print("Interaksi mereka BAD")
        if pro_mbti == "ESFP" and con_mbti == "ISTP":
            print("Interaksi mereka BAD")
        if pro_mbti == "ESFP" and con_mbti == "ESTP":
            print("Interaksi mereka BAD")
        # interaksi WORST
        if pro_mbti == "ESFP" and con_mbti == "INFP":
            print("Interaksi mereka WORST")
        if pro_mbti == "ESFP" and con_mbti == "ENFP":
            print("Interaksi mereka WORST")
        if pro_mbti == "ESFP" and con_mbti == "INFJ":
            print("Interaksi mereka WORST")
        if pro_mbti == "ESFP" and con_mbti == "ENFJ":
            print("Interaksi mereka WORST")

        # MBTI ISTP
        # interaksi PERFECT
        if pro_mbti == "ISTP" and con_mbti == "ESFJ":
            print("Interaksi mereka PERFECT")
        if pro_mbti == "ISTP" and con_mbti == "ESTJ":
            print("Interaksi mereka PERFECT")
        # interaksi NORMAL
        if pro_mbti == "ISTP" and con_mbti == "INTJ":
            print("Interaksi mereka NORMAL")
        if pro_mbti == "ISTP" and con_mbti == "ENTJ":
            print("Interaksi mereka NORMAL")
        if pro_mbti == "ISTP" and con_mbti == "INTP":
            print("Interaksi mereka NORMAL")
        if pro_mbti == "ISTP" and con_mbti == "ENTP":
            print("Interaksi mereka NORMAL")
        if pro_mbti == "ISTP" and con_mbti == "ISFJ":
            print("Interaksi mereka NORMAL")
        if pro_mbti == "ISTP" and con_mbti == "ISTJ":
            print("Interaksi mereka NORMAL")
        # interaksi BAD
        if pro_mbti == "ISTP" and con_mbti == "ISFP":
            print("Interaksi mereka BAD")
        if pro_mbti == "ISTP" and con_mbti == "ESFP":
            print("Interaksi mereka BAD")
        if pro_mbti == "ISTP" and con_mbti == "ISTP":
            print("Interaksi mereka BAD")
        if pro_mbti == "ISTP" and con_mbti == "ESTP":
            print("Interaksi mereka BAD")
        # interaksi WORST
        if pro_mbti == "ISTP" and con_mbti == "INFP":
            print("Interaksi mereka WORST")
        if pro_mbti == "ISTP" and con_mbti == "ENFP":
            print("Interaksi mereka WORST")
        if pro_mbti == "ISTP" and con_mbti == "INFJ":
            print("Interaksi mereka WORST")
        if pro_mbti == "ISTP" and con_mbti == "ENFJ":
            print("Interaksi mereka WORST")

        # MBTI ESTP
        # interaksi PERFECT
        if pro_mbti == "ESTP" and con_mbti == "ISFJ":
            print("Interaksi mereka PERFECT")
        if pro_mbti == "ESTP" and con_mbti == "ISTJ":
            print("Interaksi mereka PERFECT")
        # interaksi NORMAL
        if pro_mbti == "ESTP" and con_mbti == "INTJ":
            print("Interaksi mereka NORMAL")
        if pro_mbti == "ESTP" and con_mbti == "ENTJ":
            print("Interaksi mereka NORMAL")
        if pro_mbti == "ESTP" and con_mbti == "INTP":
            print("Interaksi mereka NORMAL")
        if pro_mbti == "ESTP" and con_mbti == "ENTP":
            print("Interaksi mereka NORMAL")
        if pro_mbti == "ESTP" and con_mbti == "ESFJ":
            print("Interaksi mereka NORMAL")
        if pro_mbti == "ESTP" and con_mbti == "ESTJ":
            print("Interaksi mereka NORMAL")
        # interaksi BAD
        if pro_mbti == "ESTP" and con_mbti == "ISFP":
            print("Interaksi mereka BAD")
        if pro_mbti == "ESTP" and con_mbti == "ESFP":
            print("Interaksi mereka BAD")
        if pro_mbti == "ESTP" and con_mbti == "ISTP":
            print("Interaksi mereka BAD")
        if pro_mbti == "ESTP" and con_mbti == "ESTP":
            print("Interaksi mereka BAD")
        # interaksi WORST
        if pro_mbti == "ESTP" and con_mbti == "INFP":
            print("Interaksi mereka WORST")
        if pro_mbti == "ESTP" and con_mbti == "ENFP":
            print("Interaksi mereka WORST")
        if pro_mbti == "ESTP" and con_mbti == "INFJ":
            print("Interaksi mereka WORST")
        if pro_mbti == "ESTP" and con_mbti == "ENFJ":
            print("Interaksi mereka WORST")

        # MBTI ISFJ
        # interaksi PERFECT
        if pro_mbti == "ISFJ" and con_mbti == "ESFP":
            print("Interaksi mereka PERFECT")
        if pro_mbti == "ISFJ" and con_mbti == "ESTP":
            print("Interaksi mereka PERFECT")
        # interaksi GOOD
        if pro_mbti == "ISFJ" and con_mbti == "ISFJ":
            print("Interaksi mereka GOOD")
        if pro_mbti == "ISFJ" and con_mbti == "ESFJ":
            print("Interaksi mereka GOOD")
        if pro_mbti == "ISFJ" and con_mbti == "ISTJ":
            print("Interaksi mereka GOOD")
        if pro_mbti == "ISFJ" and con_mbti == "ESTJ":
            print("Interaksi mereka GOOD")
        # interaksi NORMAL
        if pro_mbti == "ISFJ" and con_mbti == "ENTJ":
            print("Interaksi mereka NORMAL")
        if pro_mbti == "ISFJ" and con_mbti == "ISFP":
            print("Interaksi mereka NORMAL")
        if pro_mbti == "ISFJ" and con_mbti == "ISTP":
            print("Interaksi mereka NORMAL")
        # interaksi BAD
        if pro_mbti == "ISFJ" and con_mbti == "INTJ":
            print("Interaksi mereka BAD")
        if pro_mbti == "ISFJ" and con_mbti == "INTP":
            print("Interaksi mereka BAD")
        if pro_mbti == "ISFJ" and con_mbti == "ENTP":
            print("Interaksi mereka BAD")
        # interaksi WORST
        if pro_mbti == "ISFJ" and con_mbti == "INFP":
            print("Interaksi mereka WORST")
        if pro_mbti == "ISFJ" and con_mbti == "ENFP":
            print("Interaksi mereka WORST")
        if pro_mbti == "ISFJ" and con_mbti == "INFJ":
            print("Interaksi mereka WORST")
        if pro_mbti == "ISFJ" and con_mbti == "ENFJ":
            print("Interaksi mereka WORST")

        # MBTI ESFJ
        # interaksi PERFECT
        if pro_mbti == "ESFJ" and con_mbti == "ISFP":
            print("Interaksi mereka PERFECT")
        if pro_mbti == "ESFJ" and con_mbti == "ISTP":
            print("Interaksi mereka PERFECT")
        # interaksi GOOD
        if pro_mbti == "ESFJ" and con_mbti == "ISFJ":
            print("Interaksi mereka GOOD")
        if pro_mbti == "ESFJ" and con_mbti == "ESFJ":
            print("Interaksi mereka GOOD")
        if pro_mbti == "ESFJ" and con_mbti == "ISTJ":
            print("Interaksi mereka GOOD")
        if pro_mbti == "ESFJ" and con_mbti == "ESTJ":
            print("Interaksi mereka GOOD")
        # interaksi NORMAL
        if pro_mbti == "ESFJ" and con_mbti == "ENTJ":
            print("Interaksi mereka NORMAL")
        if pro_mbti == "ESFJ" and con_mbti == "ESFP":
            print("Interaksi mereka NORMAL")
        if pro_mbti == "ESFJ" and con_mbti == "ESTP":
            print("Interaksi mereka NORMAL")
        # interaksi BAD
        if pro_mbti == "ESFJ" and con_mbti == "INTJ":
            print("Interaksi mereka BAD")
        if pro_mbti == "ESFJ" and con_mbti == "INTP":
            print("Interaksi mereka BAD")
        if pro_mbti == "ESFJ" and con_mbti == "ENTP":
            print("Interaksi mereka BAD")
        # interaksi WORST
        if pro_mbti == "ESFJ" and con_mbti == "INFP":
            print("Interaksi mereka WORST")
        if pro_mbti == "ESFJ" and con_mbti == "ENFP":
            print("Interaksi mereka WORST")
        if pro_mbti == "ESFJ" and con_mbti == "INFJ":
            print("Interaksi mereka WORST")
        if pro_mbti == "ESFJ" and con_mbti == "ENFJ":
            print("Interaksi mereka WORST")

        # MBTI ISTJ
        # interaksi PERFECT
        if pro_mbti == "ISTJ" and con_mbti == "ESFP":
            print("Interaksi mereka PERFECT")
        if pro_mbti == "ISTJ" and con_mbti == "ESTP":
            print("Interaksi mereka PERFECT")
        # interaksi GOOD
        if pro_mbti == "ISTJ" and con_mbti == "ISFJ":
            print("Interaksi mereka GOOD")
        if pro_mbti == "ISTJ" and con_mbti == "ESFJ":
            print("Interaksi mereka GOOD")
        if pro_mbti == "ISTJ" and con_mbti == "ISTJ":
            print("Interaksi mereka GOOD")
        if pro_mbti == "ISTJ" and con_mbti == "ESTJ":
            print("Interaksi mereka GOOD")
        # interaksi NORMAL
        if pro_mbti == "ISTJ" and con_mbti == "ENTJ":
            print("Interaksi mereka NORMAL")
        if pro_mbti == "ISTJ" and con_mbti == "ISFP":
            print("Interaksi mereka NORMAL")
        if pro_mbti == "ISTJ" and con_mbti == "ISTP":
            print("Interaksi mereka NORMAL")
        # interaksi BAD
        if pro_mbti == "ISTJ" and con_mbti == "INTJ":
            print("Interaksi mereka BAD")
        if pro_mbti == "ISTJ" and con_mbti == "INTP":
            print("Interaksi mereka BAD")
        if pro_mbti == "ISTJ" and con_mbti == "ENTP":
            print("Interaksi mereka BAD")
        # interaksi WORST
        if pro_mbti == "ISTJ" and con_mbti == "INFP":
            print("Interaksi mereka WORST")
        if pro_mbti == "ISTJ" and con_mbti == "ENFP":
            print("Interaksi mereka WORST")
        if pro_mbti == "ISTJ" and con_mbti == "INFJ":
            print("Interaksi mereka WORST")
        if pro_mbti == "ISTJ" and con_mbti == "ENFJ":
            print("Interaksi mereka WORST")

        # MBTI ESFJ
        # interaksi PERFECT
        if pro_mbti == "ESFJ" and con_mbti == "INTP":
            print("Interaksi mereka PERFECT")
        if pro_mbti == "ESFJ" and con_mbti == "ISFP":
            print("Interaksi mereka PERFECT")
        if pro_mbti == "ESFJ" and con_mbti == "ISTP":
            print("Interaksi mereka PERFECT")
        # interaksi GOOD
        if pro_mbti == "ESFJ" and con_mbti == "ISFJ":
            print("Interaksi mereka GOOD")
        if pro_mbti == "ESFJ" and con_mbti == "ESFJ":
            print("Interaksi mereka GOOD")
        if pro_mbti == "ESFJ" and con_mbti == "ISTJ":
            print("Interaksi mereka GOOD")
        if pro_mbti == "ESFJ" and con_mbti == "ESTJ":
            print("Interaksi mereka GOOD")
        # interaksi NORMAL
        if pro_mbti == "ESFJ" and con_mbti == "ENTJ":
            print("Interaksi mereka NORMAL")
        if pro_mbti == "ESFJ" and con_mbti == "ESFP":
            print("Interaksi mereka NORMAL")    
        if pro_mbti == "ESFJ" and con_mbti == "ESTP":
            print("Interaksi mereka NORMAL")
        # interaksi BAD
        if pro_mbti == "ESFJ" and con_mbti == "INTJ":
            print("Interaksi mereka BAD")
        if pro_mbti == "ESFJ" and con_mbti == "ENTP":
            print("Interaksi mereka BAD")
        # interaksi WORST
        if pro_mbti == "ESFJ" and con_mbti == "INFP":
            print("Interaksi mereka WORST")
        if pro_mbti == "ESFJ" and con_mbti == "ENFP":
            print("Interaksi mereka WORST")
        if pro_mbti == "ESFJ" and con_mbti == "INFJ":
            print("Interaksi mereka WORST")
        if pro_mbti == "ESFJ" and con_mbti == "ENFJ":
            print("Interaksi mereka WORST")

    except ValueError as ve:
        print(ve)

# fungsi keluar dari program
def exit():
    print("Terima kasih telah menggunakan program ini! See you in another time, adios!")

# fungsi utama
def main():
    while True:
        menu_login()
        try:
            pilihan = input("Pilih menu (1/2/3): ")
            # pengecekan inputan pengguna
            if not pilihan:
                raise ValueError('Input tidak boleh kosong. Pilih menu 1-3.')
            if not pilihan.isdigit():
                raise TypeError('Input harus berupa angka.')

            # program berlanjut jika inputan pengguna sesuai
            if pilihan == '1':
                registrasi()
            elif pilihan == '2':
                if login():
                    peran = 'admin' if users_aktif == 'admin' else 'user'
                    while True:
                        menu_kedua(peran)
                        try:
                            pilihan = input('Pilih opsi: ')
                            # pengecekan inputan pengguna
                            if not pilihan:
                                raise ValueError('Input tidak boleh kosong. Pilih menu yang anda inginkan.')
                            if not pilihan.isdigit():
                                raise TypeError('Input harus berupa angka, coba lagi.')       
                                
                            # program berlanjut jika inputan pengguna sesuai
                            if pilihan == '1': # tambah karakter
                                add_data()
                            elif pilihan == '2': # lihat karakter
                                read_data()
                            elif pilihan == '3' and peran == 'admin': # ubah karakter
                                update_data()
                            elif pilihan == '4' and peran == 'admin': # hapus karakter
                                delete_data()
                            elif (pilihan == '5' and peran == 'admin') or (pilihan == '3' and peran == 'user'): # cek interaksi
                                interaction()
                            elif (pilihan == '6' and peran == 'admin') or (pilihan == '4' and peran == 'user'): # logout dari akun
                                print(f'Berhasil logout!')
                                break
                            else:
                                print('Pilihan tidak valid. Silahkan coba lagi.')
                        except ValueError as ve:
                            print(ve)
                        except TypeError as te:
                            print(te)
            elif pilihan == '3':
                exit()
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")
        except ValueError as ve:
            print(ve)
        except TypeError as te:
            print(te)

# memanggil fungsi utama
main()