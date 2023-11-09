def cari_berdasar_operator(contacts, operator):
    hasil = []
    for nama, nomor in contacts.items(): 
        if operator == 'Telkomsel' and (nomor.startswith('0812') or nomor.startswith('0822')): 
            hasil.append(nama)
        elif operator == 'xl' and (nomor.startswith('0817') or nomor.startswith('0818')):
            hasil.append(nama)
        elif operator == 'Three' and nomor.startswith('0898'):
            hasil.append(nama)
        elif operator == 'im3' and (nomor.startswith('0856') or nomor.startswith('0857') or nomor.startswith('0858')): 
            hasil.append(nama)
    return hasil
contacts = { 
    'Badu' : '089879938817',
    'Hana' : '0818662514110',
    'Seto' : '08122290909',
    'Adi' : '0856808080012',
    'Pace' : '0858000000000'
}
operator = 'im3'
hasil = cari_berdasar_operator(contacts,operator)
print(hasil)