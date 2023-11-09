def hitungvotes(votes):
    hasilvote= {}
    for vote in votes: 
        if vote in hasilvote: 
            hasilvote[vote]+=1
        else: 
            hasilvote[vote]=1
    return hasilvote
def winner(hasilvote, totalvote): 
    voteterbanyak= 0
    terbanyak= None
    for kandidat, vote in hasilvote.items(): 
        if vote>voteterbanyak: 
            voteterbanyak= vote
            terbanyak= kandidat
        if terbanyak is not None: 
            persen= voteterbanyak/totalvote
            if persen>0.5: 
                return terbanyak
        return
inputvote=[]
n = int(input('Jumlah vote: '))
for i in range(n):
    vt= input('Masukkan vote: ')
    inputvote.append(vt)
hasilvote= hitungvotes(inputvote)
menang= winner(hasilvote, n)
if menang is not None: 
    print(menang)
else: 
    print('None')