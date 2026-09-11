# Anggota kelompok: Albert Hernando, Anderson Kwan Odelish,  Calderon Sanjaya, Christian Darren, Kelvin

nyawa = 100
baterai_senter = True
punya_kunci = False
punya_peta = False

print('=== PULAU MISTERIUS: TINGKAT LANJUT ===')
print('Kamu terbangun di tepi pantai yang berkabut tebal.')
print('Di tanganmu hanya ada sebuah senter (baterai tersisa sedikit) dan kompas')

print('\n[BABAK 1: PERSIMPANGAN PANTAI]')
print('1. Masuk ke dalam hutan lebat yang gelap gulita')
print('2. Menyusuri tebing karang curam yang dihantam ombak.')
pilihan_babak_1 = input('Masukkan pilihanmu (1/2): ')

#? Bagian jalur hutan
if pilihan_babak_1 == '1':
    print('\nKamu melangkah masuk di dalam hutan. Suasana sangat mencekam.')
    print('Senter-mu tiba-tiba berkedip dan hampir mati karena baterai melemah.\n')

    print('1. Tetap nyalakan senter (menghabiskan sisa daya)')
    print('2. Matikan senter dan berjalan dalam gelap.')

    pilihan_babak_1 = input('Masukkan pilihanmu (1/2): ' ) 
    if pilihan_babak_1 == '1':
        print('\nSenter mati total! Tapi untungnya sebelum mati, kamu sempat melihat dan mengambil [Peta Kuno].')
        baterai_senter = False
        punya_peta = True

       
    elif pilihan_babak_1 == '2':
        nyawa -= 30
        print(f'Kamu menabrak pohon besar dalam gelap! Nyawamu berkurang 30. (Sisa nyawa: {nyawa})')

    print('\n--- BABAK 2: PONDOK TERBENGKALAI ---')
    print('Di tengah hutan, kamu menemukan sebuah pondok reyot.')
    print('1. Mendobrak pintu depan pondok.')
    print('2. Mengintip lewat jendela samping.')
    pilihan_babak_2 = input('Masukkan pilihanmu (1/2): ')
    if pilihan_babak_2 == '1':
        print('Pintu terbuka! Di atas meja kamu menemukan [Kunci Emasantik].')
        punya_kunci = True
        
        
    elif pilihan_babak_2 == '2':
        print('Kamu mengintip jendela, tidak ada apa-apa, hanya ruangan kosong.')

    elif pilihan_babak_2 == '3':
        print('Kamu ragu-ragu, lalu tiba-tiba hari mulai malam.')

    print('\n--- BABAK AKHIR: GERBANG BATU ---')
    print('Kamu tiba di sebuah gerbang batu besar dengan lubang kunci misterius.')
    
    if punya_kunci == True and punya_peta == True:
        print('Kamu memasukkan Kunci Emas dan menggunakan Peta Kuno untuk membaca arah jalan keluar!')
        print('ENDING SOUR: Kemenangan Sempurna! Kamu keluar pulau dengan selamat dan membawa harta karun.')
    elif punya_kunci== True and punya_peta == False:
        print('Kamu memasukkan Kunci Emas.')
        print('ENDING NEUTRAL: Kamu bisa keluar gerbang, namun kamu tersesat di pulau lain')
    elif punya_kunci== False:
        print('Gerbang terkunci rapat dan kamu tidak punya kuncinya. Tiba-tiba harimau hutan menerkammu!')
        print('ENDING GAME OVER: Kamu gagal bertahan hidup.')

#? bagian jalur tebing karang
elif pilihan_babak_1 == '2':
    nyawa -= 20
    print('\nKamu memilih menyusuri tebing karang yang licin.')
    print(f'Kakimu sempat terkilir karena ombak besar. Nyawamu berkurang 20. (sisa nyawa: {nyawa})')

    print("\n--- BABAK 2: GUA LAUT ---")
    print("Kamu menemukan celah gua yang di dalamnya memancarkan cahaya terang.")
    print("1. Masuk ke dalam gua.")
    print("2. Mengabaikan gua dan terus berjalan ke ujung tebing.")
    pilihan_babak_2 = input("Pilihanmu (1/2): ")

    if pilihan_babak_2 == '1':
        print('Kamu menemukan markas peneliti dengan helikopter tua')
        jawaban_kode = int(input('masukkan kode darurat\n7 x 7 - 9 = '))
        if jawaban_kode == 40:
            print('ENDING SOUR (Pahlawan Pulau): Kamu menyalakan helikopter dan pergi dari pulau')
        else:
            print('ENDING GAME OVER: Kamu salah menjawab kode dan alarm menyala')
    elif pilihan_babak_2 == '2':
        print("\nKamu berjalan hingga ujung tebing dan menemukan mercusuar tua yang berfungsi.")
        print("ENDING NEUTRAL: Kamu menyalakan suar darurat dan diselamatkan oleh kapal penjaga pantai.")
        