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
    nyawa -= 20
    print('Kamu memilih menyusuri tebing karang yang licin.')
    print(f'Kakimu sempat terkilir karena ombak besar. Nyawamu berkurang 20. (sisa nyawa: {nyawa})')

