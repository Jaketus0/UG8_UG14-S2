import re

def cek_kodepos(kodepos):
    if not re.match(r"^[1-9][0-9]{4}$", kodepos):
        print("Tidak Valid")
        return

    if re.search(r"(\d)\1{3,}", kodepos):
        print("Tidak Valid")
        return

    pairs = re.findall(r"(\d)(?=(\d)\1)", kodepos)
    if len(pairs) > 1:
        print("Tidak Valid")
        return

    print("Valid")

# Contoh penggunaan
cek_kodepos('12145')
cek_kodepos('32432')
cek_kodepos('55252')
cek_kodepos('55511')
cek_kodepos('55155')