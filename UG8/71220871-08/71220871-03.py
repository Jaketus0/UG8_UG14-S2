namafile= 'nilai.txt'
handle = open(namafile, 'r')
lines = handle.readlines()
nilai = [int(x.strip()) for x in lines]
tugas1 = nilai[0]*0.05
tugas2 = nilai[1]*0.05
tugas3 = nilai[2]*0.1
tugas4 = nilai[3]*0.05
tugas5 = nilai[4]*0.15
tugas6 = nilai[5]*0.1
uts = nilai[6]*0.22
uas = nilai[7]*0.28
nilaiakhir = tugas1+tugas2+tugas3+tugas4+tugas5+tugas6+uts+uas
print(nilaiakhir)
handle.close()