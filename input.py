print("#### RESERVASI PARKIR ####\n")

nomor_kendaraan_anda = input('Masukkan nomor kendaraan Anda: ')
nomorAnda_cap = nomor_kendaraan_anda.capitalize()
#print(f'Nomor Kendaraan: {nomor_kendaraan_anda}\n')

nomor_dideteksi = input('Nomor dideteksi: ')
nomorDeteksi_cap = nomor_dideteksi.capitalize()
#print(f'Nomor Dideteksi: {nomor_dideteksi}')

if nomorAnda_cap == nomorDeteksi_cap:
    print('Berhasil')
else:
    print('Tempat ini sudah direservasi, mohon pindahkan kendaraan Anda')
