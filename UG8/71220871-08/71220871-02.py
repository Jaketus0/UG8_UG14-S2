namafile= 'buah.txt'
handle= open(namafile, 'r')
handle = handle.readlines()
inputan = input("Masukkan nama buah yang ingin dihapus: ")
index_buah = None
for i in range(len(handle)):
    if handle[i].strip() == inputan:
        index_buah = i
        break
if index_buah is None:
    print("Nama buah tidak ditemukan.")
    exit()

handle.pop(index_buah)
with open("buah.txt","w") as f:
    f.writelines(handle)