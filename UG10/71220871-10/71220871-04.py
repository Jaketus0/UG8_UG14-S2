def hitung_nilai_akhir(daftar_nilai,n):
    nilai_akhir = {}
    for siswa, nilai in daftar_nilai.items():
        nilai_terbaik = sorted(nilai, reverse=True)[:n]
        rata_rata = sum(nilai_terbaik)/n
        nilai_akhir[siswa] = rata_rata
    return sorted(nilai_akhir.items(), key=lambda x: x[1], reverse=True)
daftar_nilai={
    'Udin' : [65, 74, 56, 80, 82, 94],
    'Atun' : [98, 84, 82, 88],
    'Tejo' : [85, 86]
}
n = 2 
hasil = hitung_nilai_akhir(daftar_nilai,n)
for i, nilai_akhir in hasil: 
    print(f'{i} {nilai_akhir}')