inputvote= []
n= int(input('n: '))
for i in range(n): 
	vt= input('Masukkan angka: ') 
	inputvote.append(vt)
while len(inputvote)>1:
	inputvote= inputvote[1::2]
hasilakhir= inputvote[0]
print(hasilakhir)