def validasi_kartu_kredit(nomor_kartu):
    if len(nomor_kartu) != 16 or not nomor_kartu.isdigit():
        return "Tidak valid"
    
    first_digit = int(nomor_kartu[0])
    if first_digit not in [4, 5, 6]:
        return "Tidak valid"
    
    count = 0
    for i in range(len(nomor_kartu) - 1):
        if nomor_kartu[i] == '8' and nomor_kartu[i] == nomor_kartu[i + 1]:
            count += 1
            if count >= 3:
                return "Valid Platinum"
        else:
            count = 0
    
    return "Valid Reguler"
nomor_kartu = '4234567888823456'
hasil = validasi_kartu_kredit(nomor_kartu)
print(hasil)