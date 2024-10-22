Character_info = {}
def menu_intro():
    print( 
    """
    『Character register <3』


    ♦=============================﹁
    ✭⭒          [Menu]        ⋆✯.
    ⭒✧    ⋆                  ✭   .
        ➤⭒1. Adding Character          
    .   ➤⭒2. Show Characters   .               
        ➤⭒3. Change Character    .
        ➤⭒4. Delete Character    ✭
    .   ➤⭒5. Check Interaction    
    .   ➤⭒6. Exit       ✦ ⋆   ⭒✧             
    ✭ .        ✭⭒        .          
    ⭒✧    ⋆        .        ✭      
    ﹂=============================♦
    """
    )
def intro():
    print(
    """
    Welcome to original character generator!
    This is where you can see you original character interaction based on your character MBTI!!
    """
    )
def search(nama):
    if nama in Character_info:
        return True
    else:
        return False
    
#system penambahan character
def info():
    nama = input("How will you name your character : ")
    age = input("How old is your character? : ")
    gender = input("What is your character(s) gender? : ")
    print()
    print("If you're confused or do not know what is your mbti, please have an mbti first or click this link : ")
    print("https://www.16personalities.com/id/tes-kepribadian")
    print()
    mbti = input("Please insert your character's mbti (please insert it with capslock) : ")
    print()
    Character_info[nama] = {
        'age' : age,
        'gender' : gender,
        'mbti' : mbti
    }
#system pembacaan character
def read():
    for i, j in Character_info.items():
        print(f"\n Character {i}\nName : {i}\nAge : {j['age']}\nGender : {j['gender']} \nMbti : {j['mbti']}")
    #system update character
def update():
    prev_name = input("Which character you'd to change? : ")
    if search(prev_name):
        new_name = input("Who is your new character name? : ")
        new_age = input("Is the age still the same? : ")
        new_gender = input("what is your character new gender? : ")
        new_mbti = input("your character new mbti? : ")
        Character_info[new_name] = Character_info.pop(prev_name)
        prev_name = new_name
        Character_info[new_name]['age'] = new_age
        Character_info[new_name]['gender'] = new_gender
        Character_info[new_name]['mbti'] = new_mbti
    #system penghapusan character
def delete():
    old_name = input("Which character that you want to delete? : ")
    if search(old_name):
        del Character_info[old_name]
    #system pengecekan interkasi antar mbti character
def interaction():
    pro_mbti = input("please re-asure what is your character's mbti : ")
    con_mbti = input("which mbti that you wanna check? : ")
    #MBTI INFP

    if pro_mbti == "INFP" and con_mbti == "INFP":
        print("They have a PERFECT interaction")
    if pro_mbti == "INFP" and con_mbti == "ENFP":
        print("They have a good interaction")
    if pro_mbti == "INFP" and con_mbti == "INFJ":
        print("They have a good interaction")
    if pro_mbti == "INFP" and con_mbti == "ENFJ":
        print("They have a good interaction")
    if pro_mbti == "INFP" and con_mbti == "INTJ":
        print("They have a good interaction")
    if pro_mbti == "INFP" and con_mbti == "ENTJ":
        print("They have a good interaction")
    if pro_mbti == "INFP" and con_mbti == "INTP":
        print("They have a good interaction")
    if pro_mbti == "INFP" and con_mbti == "ENTP":
        print("They have a good interaction")
    if pro_mbti == "INFP" and con_mbti == "ISFP":
        print("They have a PERECT interaction")
    if pro_mbti == "INFP" and con_mbti == "ESFP":
        print("They have the WORST interaction")
    if pro_mbti == "INFP" and con_mbti == "ISTP":
        print("They have the WORST interaction")
    if pro_mbti == "INFP" and con_mbti == "ESTP":
        print("They have the WORST interaction")
    if pro_mbti == "INFP" and con_mbti == "ISFJ":
        print("They have the WORST interaction")
    if pro_mbti == "INFP" and con_mbti == "ESFJ":
        print("They have the WORST interaction")
    if pro_mbti == "INFP" and con_mbti == "ISTJ":
        print("They have the WORST interaction")
    if pro_mbti == "INFP" and con_mbti == "ESTJ":
        print("They have the WORST interaction")

#MBTI ENFP
    if pro_mbti == "ENFP" and con_mbti == "INFP":
        print("They have a good interaction")
    if pro_mbti == "ENFP" and con_mbti == "ENFP":
        print("They have a good interaction")
    if pro_mbti == "ENFP" and con_mbti == "INFJ":
        print("They have a PERFECT interaction")
    if pro_mbti == "ENFP" and con_mbti == "ENFJ":
        print("They have a good interaction")
    if pro_mbti == "ENFP" and con_mbti == "INTJ":
        print("They have a PERFECT interaction")
    if pro_mbti == "ENFP" and con_mbti == "ENTJ":
        print("They have a good interaction")
    if pro_mbti == "ENFP" and con_mbti == "INTP":
        print("They have a good interaction")
    if pro_mbti == "ENFP" and con_mbti == "ENTP":
        print("They have a good interaction")
    if pro_mbti == "ENFP" and con_mbti == "ISFP":
        print("They have the WORST interaction")
    if pro_mbti == "ENFP" and con_mbti == "ESFP":
        print("They have the WORST interaction")
    if pro_mbti == "ENFP" and con_mbti == "ISTP":
        print("They have the WORST interaction")
    if pro_mbti == "ENFP" and con_mbti == "ESTP":
        print("They have the WORST interaction")
    if pro_mbti == "ENFP" and con_mbti == "ISFJ":
        print("They have the WORST interaction")
    if pro_mbti == "ENFP" and con_mbti == "ESFJ":
        print("They have the WORST interaction")
    if pro_mbti == "ENFP" and con_mbti == "ISTJ":
        print("They have the WORST interaction")
    if pro_mbti == "ENFP" and con_mbti == "ESTJ":
        print("They have the WORST interaction")

#MBTI INFJ
    if pro_mbti == "INFJ" and con_mbti == "INFP":
        print("They have a good interaction")
    if pro_mbti == "INFJ" and con_mbti == "ENFP":
        print("They have a PERFECT interaction")
    if pro_mbti == "INFJ" and con_mbti == "INFJ":
        print("They have a good interaction")
    if pro_mbti == "INFJ" and con_mbti == "ENFJ":
        print("They have a good interaction")
    if pro_mbti == "INFJ" and con_mbti == "INTJ":
        print("They have a good interaction")
    if pro_mbti == "INFJ" and con_mbti == "ENTJ":
        print("They have a good interaction")
    if pro_mbti == "INFJ" and con_mbti == "INTP":
        print("They have a good interaction")
    if pro_mbti == "INFJ" and con_mbti == "ENTP":
        print("They have a PERFECT interaction")
    if pro_mbti == "INFJ" and con_mbti == "ISFP":
        print("They have the WORST interaction")
    if pro_mbti == "INFJ" and con_mbti == "ESFP":
        print("They have the WORST interaction")
    if pro_mbti == "INFJ" and con_mbti == "ISTP":
        print("They have the WORST interaction")
    if pro_mbti == "INFJ" and con_mbti == "ESTP":
        print("They have the WORST interaction")
    if pro_mbti == "INFJ" and con_mbti == "ISFJ":
        print("They have the WORST interaction")
    if pro_mbti == "INFJ" and con_mbti == "ESFJ":
        print("They have the WORST interaction")
    if pro_mbti == "INFJ" and con_mbti == "ISTJ":
        print("They have the WORST interaction")
    if pro_mbti == "INFJ" and con_mbti == "ESTJ":
        print("They have the WORST interaction")

#MBTI ENFJ
    if pro_mbti == "ENFJ" and con_mbti == "INFP":
        print("They have a good interaction")
    if pro_mbti == "ENFJ" and con_mbti == "ENFP":
        print("They have a PERFECT interaction")
    if pro_mbti == "ENFJ" and con_mbti == "INFJ":
        print("They have a good interaction")
    if pro_mbti == "ENFJ" and con_mbti == "ENFJ":
        print("They have a good interaction")
    if pro_mbti == "ENFJ" and con_mbti == "INTJ":
        print("They have a good interaction")
    if pro_mbti == "ENFJ" and con_mbti == "ENTJ":
        print("They have a good interaction")
    if pro_mbti == "ENFJ" and con_mbti == "INTP":
        print("They have a good interaction")
    if pro_mbti == "ENFJ" and con_mbti == "ENTP":
        print("They have a PERFECT interaction")
    if pro_mbti == "ENFJ" and con_mbti == "ISFP":
        print("They have the WORST interaction")
    if pro_mbti == "ENFJ" and con_mbti == "ESFP":
        print("They have the WORST interaction")
    if pro_mbti == "ENFJ" and con_mbti == "ISTP":
        print("They have the WORST interaction")
    if pro_mbti == "ENFJ" and con_mbti == "ESTP":
        print("They have the WORST interaction")
    if pro_mbti == "ENFJ" and con_mbti == "ISFJ":
        print("They have the WORST interaction")
    if pro_mbti == "ENFJ" and con_mbti == "ESFJ":
        print("They have the WORST interaction")
    if pro_mbti == "ENFJ" and con_mbti == "ISTJ":
        print("They have the WORST interaction")
    if pro_mbti == "ENFJ" and con_mbti == "ESTJ":
        print("They have the WORST interaction")

#MBTI INTJ
    if pro_mbti == "INTJ" and con_mbti == "INFP":
        print("They have a good interaction")
    if pro_mbti == "INTJ" and con_mbti == "ENFP":
        print("They have a PERFECT interaction")
    if pro_mbti == "INTJ" and con_mbti == "INFJ":
        print("They have a good interaction")
    if pro_mbti == "INTJ" and con_mbti == "ENFJ":
        print("They have a good interaction")
    if pro_mbti == "INTJ" and con_mbti == "INTJ":
        print("They have a good interaction")
    if pro_mbti == "INTJ" and con_mbti == "ENTJ":
        print("They have a good interaction")
    if pro_mbti == "INTJ" and con_mbti == "INTP":
        print("They have a good interaction")
    if pro_mbti == "INTJ" and con_mbti == "ENTP":
        print("They have a PERFECT interaction")
    if pro_mbti == "INTJ" and con_mbti == "ISFP":
        print("They have the normal interaction")
    if pro_mbti == "INTJ" and con_mbti == "ESFP":
        print("They have the normal interaction")
    if pro_mbti == "INTJ" and con_mbti == "ISTP":
        print("They have the normal interaction")
    if pro_mbti == "INTJ" and con_mbti == "ESTP":
        print("They have the normal interaction")
    if pro_mbti == "INTJ" and con_mbti == "ISFJ":
        print("They have the bad interaction")
    if pro_mbti == "INTJ" and con_mbti == "ESFJ":
        print("They have the bad interaction")
    if pro_mbti == "INTJ" and con_mbti == "ISTJ":
        print("They have the bad interaction")
    if pro_mbti == "INTJ" and con_mbti == "ESTJ":
        print("They have the bad interaction")

#MBTI ENTJ
    if pro_mbti == "ENTJ" and con_mbti == "INFP":
        print("They have a PERFECT interaction")
    if pro_mbti == "ENTJ" and con_mbti == "ENFP":
        print("They have a good interaction")
    if pro_mbti == "ENTJ" and con_mbti == "INFJ":
        print("They have a good interaction")
    if pro_mbti == "ENTJ" and con_mbti == "ENFJ":
        print("They have a good interaction")
    if pro_mbti == "ENTJ" and con_mbti == "INTJ":
        print("They have a good interaction")
    if pro_mbti == "ENTJ" and con_mbti == "ENTJ":
        print("They have a good interaction")
    if pro_mbti == "ENTJ" and con_mbti == "INTP":
        print("They have a PERFECT interaction")
    if pro_mbti == "ENTJ" and con_mbti == "ENTP":
        print("They have a good interaction")
    if pro_mbti == "ENTJ" and con_mbti == "ISFP":
        print("They have the normal interaction")
    if pro_mbti == "ENTJ" and con_mbti == "ESFP":
        print("They have the normal interaction")
    if pro_mbti == "ENTJ" and con_mbti == "ISTP":
        print("They have the normal interaction")
    if pro_mbti == "ENTJ" and con_mbti == "ESTP":
        print("They have the normal interaction")
    if pro_mbti == "ENTJ" and con_mbti == "ISFJ":
        print("They have the normal interaction")
    if pro_mbti == "ENTJ" and con_mbti == "ESFJ":
        print("They have the normal interaction")
    if pro_mbti == "INTJ" and con_mbti == "ISTJ":
        print("They have the normal interaction")
    if pro_mbti == "ENTJ" and con_mbti == "ESTJ":
        print("They have the normal interaction")

#MBTI INTP
    if pro_mbti == "INTP" and con_mbti == "INFP":
        print("They have a PERFECT interaction")
    if pro_mbti == "INTP" and con_mbti == "ENFP":
        print("They have a good interaction")
    if pro_mbti == "INTP" and con_mbti == "INFJ":
        print("They have a good interaction")
    if pro_mbti == "INTP" and con_mbti == "ENFJ":
        print("They have a good interaction")
    if pro_mbti == "INTP" and con_mbti == "INTJ":
        print("They have a good interaction")
    if pro_mbti == "INTP" and con_mbti == "ENTJ":
        print("They have a PERFECT interaction")
    if pro_mbti == "INTP" and con_mbti == "INTP":
        print("They have a good interaction")
    if pro_mbti == "INTP" and con_mbti == "ENTP":
        print("They have a good interaction")
    if pro_mbti == "INTP" and con_mbti == "ISFP":
        print("They have the normal interaction")
    if pro_mbti == "INTP" and con_mbti == "ESFP":
        print("They have the normal interaction")
    if pro_mbti == "INTP" and con_mbti == "ISTP":
        print("They have the normal interaction")
    if pro_mbti == "INTP" and con_mbti == "ESTP":
        print("They have the normal interaction")
    if pro_mbti == "INTP" and con_mbti == "ISFJ":
        print("They have the bad interaction")
    if pro_mbti == "INTP" and con_mbti == "ESFJ":
        print("They have the bad interaction")
    if pro_mbti == "INTP" and con_mbti == "ISTJ":
        print("They have the bad interaction")
    if pro_mbti == "INTP" and con_mbti == "ESTJ":
        print("They have a PERFECT interaction")

#MBTI ENTP
    if pro_mbti == "ENTP" and con_mbti == "INFP":
        print("They have a good interaction")
    if pro_mbti == "ENTP" and con_mbti == "ENFP":
        print("They have a good interaction")
    if pro_mbti == "ENTP" and con_mbti == "INFJ":
        print("They have a PERFECT interaction")
    if pro_mbti == "ENTP" and con_mbti == "ENFJ":
        print("They have a good interaction")
    if pro_mbti == "ENTP" and con_mbti == "INTJ":
        print("They have a PERFECT interaction")
    if pro_mbti == "ENTP" and con_mbti == "ENTJ":
        print("They have a good interaction")
    if pro_mbti == "ENTP" and con_mbti == "INTP":
        print("They have a good interaction")
    if pro_mbti == "ENTP" and con_mbti == "ENTP":
        print("They have a good interaction")
    if pro_mbti == "ENTP" and con_mbti == "ISFP":
        print("They have the normal interaction")
    if pro_mbti == "ENTP" and con_mbti == "ESFP":
        print("They have the normal interaction")
    if pro_mbti == "ENTP" and con_mbti == "ISTP":
        print("They have the normal interaction")
    if pro_mbti == "ENTP" and con_mbti == "ESTP":
        print("They have the normal interaction")
    if pro_mbti == "ENTP" and con_mbti == "ISFJ":
        print("They have the bad interaction")
    if pro_mbti == "ENTP" and con_mbti == "ESFJ":
        print("They have the bad interaction")
    if pro_mbti == "ENTP" and con_mbti == "ISTJ":
        print("They have the bad interaction")
    if pro_mbti == "ENTP" and con_mbti == "ESTJ":
        print("They have the bad interaction")

#MBTI ISFP
    if pro_mbti == "ISFP" and con_mbti == "INFP":
        print("They have the WORST interaction")
    if pro_mbti == "ISFP" and con_mbti == "ENFP":
        print("They have the WORST interaction")
    if pro_mbti == "ISFP" and con_mbti == "INFJ":
        print("They have the WORST interaction")
    if pro_mbti == "ISFP" and con_mbti == "ENFJ":
        print("They have a PERFECT interaction")
    if pro_mbti == "ISFP" and con_mbti == "INTJ":
        print("They have the normal interaction")
    if pro_mbti == "ISFP" and con_mbti == "ENTJ":
        print("They have the normal interaction")
    if pro_mbti == "ISFP" and con_mbti == "INTP":
        print("They have the normal interaction")
    if pro_mbti == "ISFP" and con_mbti == "ENTP":
        print("They have the normal interaction")
    if pro_mbti == "ISFP" and con_mbti == "ISFP":
        print("They have the bad interaction")
    if pro_mbti == "ISFP" and con_mbti == "ESFP":
        print("They have the bad interaction")
    if pro_mbti == "ISFP" and con_mbti == "ISTP":
        print("They have the bad interaction")
    if pro_mbti == "ISFP" and con_mbti == "ESTP":
        print("They have the bad interaction")
    if pro_mbti == "ISFP" and con_mbti == "ISFJ":
        print("They have the normal interaction")
    if pro_mbti == "ISFP" and con_mbti == "ESFJ":
        print("They have a PERFECT interaction")
    if pro_mbti == "ISFP" and con_mbti == "ISTJ":
        print("They have the normal interaction")
    if pro_mbti == "ISFP" and con_mbti == "ESTJ":
        print("They have a PERFECT interaction")

#MBTI ESFP
    if pro_mbti == "ESFP" and con_mbti == "INFP":
        print("They have the WORST interaction")
    if pro_mbti == "ESFP" and con_mbti == "ENFP":
        print("They have the WORST interaction")
    if pro_mbti == "ESFP" and con_mbti == "INFJ":
        print("They have the WORST interaction")
    if pro_mbti == "ESFP" and con_mbti == "ENFJ":
        print("They have the WORST interaction")
    if pro_mbti == "ESFP" and con_mbti == "INTJ":
        print("They have the normal interaction")
    if pro_mbti == "ESFP" and con_mbti == "ENTJ":
        print("They have the normal interaction")
    if pro_mbti == "ESFP" and con_mbti == "INTP":
        print("They have the normal interaction")
    if pro_mbti == "ESFP" and con_mbti == "ENTP":
        print("They have the normal interaction")
    if pro_mbti == "ESFP" and con_mbti == "ISFP":
        print("They have the bad interaction")
    if pro_mbti == "ESFP" and con_mbti == "ESFP":
        print("They have the bad interaction")
    if pro_mbti == "ESFP" and con_mbti == "ISTP":
        print("They have the bad interaction")
    if pro_mbti == "ESFP" and con_mbti == "ESTP":
        print("They have the bad interaction")
    if pro_mbti == "ESFP" and con_mbti == "ISFJ":
        print("They have a PERFECT interaction")
    if pro_mbti == "ESFP" and con_mbti == "ESFJ":
        print("They have the normal interaction")
    if pro_mbti == "ESFP" and con_mbti == "ISTJ":
        print("They have a PERFECT interaction")
    if pro_mbti == "ESFP" and con_mbti == "ESTJ":
        print("They have the normal interaction")

#MBTI ISTP
    if pro_mbti == "ISTP" and con_mbti == "INFP":
        print("They have the WORST interaction")
    if pro_mbti == "ISTP" and con_mbti == "ENFP":
        print("They have the WORST interaction")
    if pro_mbti == "ISTP" and con_mbti == "INFJ":
        print("They have the WORST interaction")
    if pro_mbti == "ISTP" and con_mbti == "ENFJ":
        print("They have the WORST interaction")
    if pro_mbti == "ISTP" and con_mbti == "INTJ":
        print("They have the normal interaction")
    if pro_mbti == "ISTP" and con_mbti == "ENTJ":
        print("They have the normal interaction")
    if pro_mbti == "ISTP" and con_mbti == "INTP":
        print("They have the normal interaction")
    if pro_mbti == "ISTP" and con_mbti == "ENTP":
        print("They have the normal interaction")
    if pro_mbti == "ISTP" and con_mbti == "ISFP":
        print("They have the bad interaction")
    if pro_mbti == "ISTP" and con_mbti == "ESFP":
        print("They have the bad interaction")
    if pro_mbti == "ISTP" and con_mbti == "ISTP":
        print("They have the bad interaction")
    if pro_mbti == "ISTP" and con_mbti == "ESTP":
        print("They have the bad interaction")
    if pro_mbti == "ISTP" and con_mbti == "ISFJ":
        print("They have the normal interaction")
    if pro_mbti == "ISTP" and con_mbti == "ESFJ":
        print("They have a PERFECT interaction")
    if pro_mbti == "ISTP" and con_mbti == "ISTJ":
        print("They have the normal interaction")
    if pro_mbti == "ISTP" and con_mbti == "ESTJ":
        print("They have a PERFECT interaction")

#MBTI ESTP
    if pro_mbti == "ESTP" and con_mbti == "INFP":
        print("They have the WORST interaction")
    if pro_mbti == "ESTP" and con_mbti == "ENFP":
        print("They have the WORST interaction")
    if pro_mbti == "ESTP" and con_mbti == "INFJ":
        print("They have the WORST interaction")
    if pro_mbti == "ESTP" and con_mbti == "ENFJ":
        print("They have the WORST interaction")
    if pro_mbti == "ESTP" and con_mbti == "INTJ":
        print("They have the normal interaction")
    if pro_mbti == "ESTP" and con_mbti == "ENTJ":
        print("They have the normal interaction")
    if pro_mbti == "ESTP" and con_mbti == "INTP":
        print("They have the normal interaction")
    if pro_mbti == "ESTP" and con_mbti == "ENTP":
        print("They have the normal interaction")
    if pro_mbti == "ESTP" and con_mbti == "ISFP":
        print("They have the bad interaction")
    if pro_mbti == "ESTP" and con_mbti == "ESFP":
        print("They have the bad interaction")
    if pro_mbti == "ESTP" and con_mbti == "ISTP":
        print("They have the bad interaction")
    if pro_mbti == "ESTP" and con_mbti == "ESTP":
        print("They have the bad interaction")
    if pro_mbti == "ESTP" and con_mbti == "ISFJ":
        print("They have a PERFECT interaction")
    if pro_mbti == "ESTP" and con_mbti == "ESFJ":
        print("They have the normal interaction")
    if pro_mbti == "ESTP" and con_mbti == "ISTJ":
        print("They have a PERFECT interaction")
    if pro_mbti == "ESTP" and con_mbti == "ESTJ":
        print("They have the normal interaction")

#MBTI ISFJ
    if pro_mbti == "ISFJ" and con_mbti == "INFP":
        print("They have the WORST interaction")
    if pro_mbti == "ISFJ" and con_mbti == "ENFP":
        print("They have the WORST interaction")
    if pro_mbti == "ISFJ" and con_mbti == "INFJ":
        print("They have the WORST interaction")
    if pro_mbti == "ISFJ" and con_mbti == "ENFJ":
        print("They have the WORST interaction")
    if pro_mbti == "ISFJ" and con_mbti == "INTJ":
        print("They have the bad interaction")
    if pro_mbti == "ISFJ" and con_mbti == "ENTJ":
        print("They have the normal interaction")
    if pro_mbti == "ISFJ" and con_mbti == "INTP":
        print("They have the bad interaction")
    if pro_mbti == "ISFJ" and con_mbti == "ENTP":
        print("They have the bad interaction")
    if pro_mbti == "ISFJ" and con_mbti == "ISFP":
        print("They have the normal interaction")
    if pro_mbti == "ISFJ" and con_mbti == "ESFP":
        print("They have a PERFECT interaction")
    if pro_mbti == "ISFJ" and con_mbti == "ISTP":
        print("They have the normal interaction")
    if pro_mbti == "ISFJ" and con_mbti == "ESTP":
        print("They have a PERFECT interaction")
    if pro_mbti == "ISFJ" and con_mbti == "ISFJ":
        print("They have a good interaction")
    if pro_mbti == "ISFJ" and con_mbti == "ESFJ":
        print("They have a good interaction")
    if pro_mbti == "ISFJ" and con_mbti == "ISTJ":
        print("They have a good interaction")
    if pro_mbti == "ISFJ" and con_mbti == "ESTJ":
        print("They have a good interaction")

#MBTI ESFJ
    if pro_mbti == "ESFJ" and con_mbti == "INFP":
        print("They have the WORST interaction")
    if pro_mbti == "ESFJ" and con_mbti == "ENFP":
        print("They have the WORST interaction")
    if pro_mbti == "ESFJ" and con_mbti == "INFJ":
        print("They have the WORST interaction")
    if pro_mbti == "ESFJ" and con_mbti == "ENFJ":
        print("They have the WORST interaction")
    if pro_mbti == "ESFJ" and con_mbti == "INTJ":
        print("They have the bad interaction")
    if pro_mbti == "ESFJ" and con_mbti == "ENTJ":
        print("They have the normal interaction")
    if pro_mbti == "ESFJ" and con_mbti == "INTP":
        print("They have the bad interaction")
    if pro_mbti == "ESFJ" and con_mbti == "ENTP":
        print("They have the bad interaction")
    if pro_mbti == "ESFJ" and con_mbti == "ISFP":
        print("They have a PERFECT interaction")
    if pro_mbti == "ESFJ" and con_mbti == "ESFP":
        print("They have the normal interaction")
    if pro_mbti == "ESFJ" and con_mbti == "ISTP":
        print("They have a PERFECT interaction")
    if pro_mbti == "ESFJ" and con_mbti == "ESTP":
        print("They have the normal interaction")
    if pro_mbti == "ESFJ" and con_mbti == "ISFJ":
        print("They have a good interaction")
    if pro_mbti == "ESFJ" and con_mbti == "ESFJ":
        print("They have a good interaction")
    if pro_mbti == "ESFJ" and con_mbti == "ISTJ":
        print("They have a good interaction")
    if pro_mbti == "ESFJ" and con_mbti == "ESTJ":
        print("They have a good interaction")

#MBTI ISTJ
    if pro_mbti == "ISTJ" and con_mbti == "INFP":
        print("They have the WORST interaction")
    if pro_mbti == "ISTJ" and con_mbti == "ENFP":
        print("They have the WORST interaction")
    if pro_mbti == "ISTJ" and con_mbti == "INFJ":
        print("They have the WORST interaction")
    if pro_mbti == "ISTJ" and con_mbti == "ENFJ":
        print("They have the WORST interaction")
    if pro_mbti == "ISTJ" and con_mbti == "INTJ":
        print("They have the bad interaction")
    if pro_mbti == "ISTJ" and con_mbti == "ENTJ":
        print("They have the normal interaction")
    if pro_mbti == "ISTJ" and con_mbti == "INTP":
        print("They have the bad interaction")
    if pro_mbti == "ISTJ" and con_mbti == "ENTP":
        print("They have the bad interaction")
    if pro_mbti == "ISTJ" and con_mbti == "ISFP":
        print("They have the normal interaction")
    if pro_mbti == "ISTJ" and con_mbti == "ESFP":
        print("They have a PERFECT interaction")
    if pro_mbti == "ISTJ" and con_mbti == "ISTP":
        print("They have the normal interaction")
    if pro_mbti == "ISTJ" and con_mbti == "ESTP":
        print("They have a PERFECT interaction")
    if pro_mbti == "ISTJ" and con_mbti == "ISFJ":
        print("They have a good interaction")
    if pro_mbti == "ISTJ" and con_mbti == "ESFJ":
        print("They have a good interaction")
    if pro_mbti == "ISTJ" and con_mbti == "ISTJ":
        print("They have a good interaction")
    if pro_mbti == "ISTJ" and con_mbti == "ESTJ":
        print("They have a good interaction")

#MBTI ESFJ
    if pro_mbti == "ESFJ" and con_mbti == "INFP":
        print("They have the WORST interaction")
    if pro_mbti == "ESFJ" and con_mbti == "ENFP":
        print("They have the WORST interaction")
    if pro_mbti == "ESFJ" and con_mbti == "INFJ":
        print("They have the WORST interaction")
    if pro_mbti == "ESFJ" and con_mbti == "ENFJ":
        print("They have the WORST interaction")
    if pro_mbti == "ESFJ" and con_mbti == "INTJ":
        print("They have the bad interaction")
    if pro_mbti == "ESFJ" and con_mbti == "ENTJ":
        print("They have the normal interaction")
    if pro_mbti == "ESFJ" and con_mbti == "INTP":
        print("They have a PERFECT interaction")
    if pro_mbti == "ESFJ" and con_mbti == "ENTP":
        print("They have the bad interaction")
    if pro_mbti == "ESFJ" and con_mbti == "ISFP":
        print("They have a PERFECT interaction")
    if pro_mbti == "ESFJ" and con_mbti == "ESFP":
        print("They have the normal interaction")
    if pro_mbti == "ESFJ" and con_mbti == "ISTP":
        print("They have a PERFECT interaction")
    if pro_mbti == "ESFJ" and con_mbti == "ESTP":
        print("They have the normal interaction")
    if pro_mbti == "ESFJ" and con_mbti == "ISFJ":
        print("They have a good interaction")
    if pro_mbti == "ESFJ" and con_mbti == "ESFJ":
        print("They have a good interaction")
    if pro_mbti == "ESFJ" and con_mbti == "ISTJ":
        print("They have a good interaction")
    if pro_mbti == "ESFJ" and con_mbti == "ESTJ":
        print("They have a good interaction")


def done():
    print("Thank you for using this program, we'll see you later, adios!")
    print("17")


menu_intro()
intro()
while True:
        choose = int(input("Please choose your selection : "))
        if choose == 1:
            info()
        elif choose == 2:
            read()
        elif choose == 3:
            update()
        elif choose == 4:
            delete()
        elif choose == 5:
            interaction()
        elif choose == 6:
            done()
            print("17")
            break
        else:
            print("Wrong input")
            reaction = input("Do you like it? Yes/no")
