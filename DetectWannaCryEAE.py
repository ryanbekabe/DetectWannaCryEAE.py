import os
import hashlib

print('.: Deteksi dan bersihkan virus jaringan WannaCry EAE :.')

def cekfile(lokasinya):
    with open(lokasinya, 'rb') as inidatanya:
        md5cek = hashlib.md5()
        while True:
            data = inidatanya.read(8192)
            if not data:
                break
            md5cek.update(data)
        return md5cek.hexdigest()

if cekfile('C:\Windows\mssecsvc.exe') == '3d3b7e106612cc5086ef3e8aff697829':
	print('File virus positif ada.')
	print('MD5 virus WannaCry EAE : ', cekfile('C:\Windows\mssecsvc.exe'))
	print('Hentikan proses virus.')
	print('Bersihkan virus dari komputer ini.')
	os.system("taskkill /f /im mssecsvc.exe")
	os.system("rename C:\Windows\mssecsvc.exe C:\Windows\mssecsvc.exe.karantinaBKB")
else:
	print('Tidak ditemukan file virus.')

input('Tekan Enter untuk menutup program ini...')
