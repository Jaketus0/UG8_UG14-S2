def tribonacci(a,b,c,n):
    hasil= [a,b,c]
    start= 2 
    panjang= n-3
    for i in range(panjang): 
        next= hasil[start-2] + hasil[start-1] + hasil[start]
        hasil.append(next)
        start+=1
    return hasil
a= int(input('a: '))
b= int(input('b: '))
c= int(input('c: '))
n= int(input('n: '))
hasil= tribonacci(a,b,c,n)
print(hasil)