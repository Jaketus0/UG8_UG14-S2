def nol_depan(lst): 
    lst.sort(key=lambda x: x !=0)
    return lst
list= []
start= 0 
panjang_list= int(input('Masukkan panjang: '))
for i in range(panjang_list): 
    if start != panjang_list: 
        masuk= int(input('Masukkan nilai: '))
        list.append(masuk)
        start+=1
list= nol_depan(list)
print(list)