nyawa = 100
baterai_senter = True
punya_kunci = False
punya_peta = False

print('=== PULAU MISTERIUS: TINGKAT LANJUT ===')
print('Kamu terbangun di tepi pantai yang berkabut tebal.')
print('Di tanganmu hanya ada sebuah senter (baterai tersisa sedikit) dan kompas')

print('\n[BABAK 1: PERSIMPANGAN PANTAI]')
print('1. Masuk ke dalam hutan lebat yang geap gulita')
print('2. Menyusuri tebing karang curam yang dihantam ombak.')
pilihan_babak_1 = input('Masukkan pilihanmu (1/2): ')


if pilihan_babak_1 == '1':
    print('\nKamu melangkah masuk di dalam hutan. Suasana sangat mencekam.')
    print('Senter-mu tiba-tiba berkedip dan hampir mati karena baterai melemah.\n')

    print('1. Tetap nyalakan senter (menghabiskan sisa daya)')
    print('2. Matikan senter dan berjalan dalam gelap.')

    pilihan_babak_1 = input('Masukkan pilihanmu (1/2): ' ) 
    if pilihan_babak_1 == '1':
        print('\nSenter mati total! Tapi untungnya sebelum mati, kamu sempat melihat dan mengambil [Peta Kuno].')
        baterai_senter = False

        print('\n--- BABAK 2: PONDOK TERBENGKALAI ---')
        print('Di tengah hutan, kamu menemukan sebuah pondok reyot.')
        print('1. Mendobrak pintu depan pondok.')
        print('2. Mengintip lewat jendela samping.')
        pilihan_babak_2 = input('Masukkan pilihanmu (1/2): ')
        if pilihan_babak_2 == '1':
            print('Pintu terbuka! Di atas meja kamu menemukan [Kunci Emasantik].')

            print('--- BABAK AKHIR: GERBANG BATU ---')
            print('Kamu tiba di sebuah gerbang batu besar dengan lubang kunci misterius.')
            print('Kamu memasukkan Kunci Emas dan menggunakan Peta Kuno untuk membaca arah jalan keluar!')
            print('ENDING SOUR: Kemenangan Sempurna! Kamu keluar pulau dengan selamat dan membawa harta karun.')

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
        print("\nKamu melangkah masuk ke dalam gua dan mengeksplorasi cahaya tersebut...")
    elif pilihan_babak_2 == '2':
        print("\nKamu berjalan hingga ujung tebing dan menemukan mercusuar tua yang berfungsi.")
        print("ENDING NEUTRAL: Kamu menyalakan suar darurat dan diselamatkan oleh kapal penjaga pantai.")
        
        