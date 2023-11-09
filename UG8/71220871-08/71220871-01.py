carikata= input('Masukkan kata yang dicari : ')
carikata= carikata.lower()
namafile= 'romeojuliet.txt'
handle = open(namafile, 'r')
jumlah= 0 
for baris in handle:
    baris = baris.lower()
    jumlah = jumlah + baris.count(carikata)
print(f'Kata {carikata} jumlahnya ada : {jumlah}')
handle.close()