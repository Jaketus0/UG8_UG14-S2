#FAKTORIAL GENAP 

def faktorial_genap(jumlah, awal): 
    #base case 
    if jumlah == 0: 
        return 1 
    else: 
        #recursive casenya 
        return faktorial_genap(jumlah-1, awal+2)*(awal+2)
print(faktorial_genap(5,0))
#print(faktorial_genap(5,0)) => 2*4*6*8*10