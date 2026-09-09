nyawa = 100
baterai_senter = True
punya_kunci = False
punya_peta = False

print('=== PULAU MISTERIUS: TINGKAT LANJUT ===')
print('Kamu terbangun di tepi pantai yang berkabut tebal.')
print('Di tanganmu hanya ada sebuah senter (baterai tersisa sedikit) dan kompas')

print('[BABAK 1: PERSIMPANGAN PANTAI]')
print('1. Masuk ke dalam hutan lebat yang geap gulita')
print('2. Menyusuri tebing karang curam yang dihantam ombak.')
pilihan_babak_1 = input('masukkan pilihanmu (1/2): ')


if pilihan_babak_1 == '1':
    print('Kamu melangkah masuk di dalam hutan. Suasana sangat mencekam.')
    print('Senter-mu tiba-tiba berkedip dan hampir mati karena baterai melemah.')

elif pilihan_babak_1 == '2':
    print('Kamu memilih menyusuri tebing karang yang curam.')
    print('Ombak besar menghantam tebing dan membuat perjalananmu semakin berbahaya.')

    print('[BABAK 2: EKSPLORASI GUA]')
    print('Di depanmu terlihat sebuah celah gua dengan cahaya terang.')
    print('1. Masuk ke dalam gua')
    print('2. Mengabaikan gua dan terus berjalan')

    pilihan_babak_2 = input('Masukkan pilihanmu (1/2): ')

    if pilihan_babak_2 == '1':
        print('Kamu masuk ke dalam gua dan menemukan markas peneliti dengan helikopter tua.')

    elif pilihan_babak_2 == '2':
        print('Kamu mengabaikan gua dan terus berjalan menuju ujung tebing.')

    else:
        print('Pilihan tidak tersedia.')

else:
    print('Pilihan tidak tersedia.')


