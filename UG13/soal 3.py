# si Gray
# cariangka(2) return 5 
# cariangka(5) return 28
def cekprima(n, divisor=0, result= True): 
    if n <= 1: 
        return False 
    elif n == 2: 
        return True
    elif divisor == 1: 
        return result
    else: 
        if divisor == 0: 
            divisor = n-1
        if (n%divisor == 0): 
            result = result and False
        else: 
            result = result and True 
        return cekprima(n, divisor-1, result)

def cariangka(n):
    sum = 0 
    jumlah_prima_found = 0
    iterate = 1
    while jumlah_prima_found < n: 
        if(cekprima(iterate)): 
            jumlah_prima_found += 1
            sum += iterate
        iterate += 1
    return sum

print(cariangka(2))
print(cariangka(5))
print(cariangka(10))