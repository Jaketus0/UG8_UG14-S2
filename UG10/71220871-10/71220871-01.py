def filter_duplikasi(lst, batas):
    counter = {}
    output = []
    for value in lst:
        if value not in counter:
            counter[value] = 1
        else:
            counter[value] += 1

        if counter[value] <= batas:
            output.append(value)
    print(output)
filter_duplikasi([20,37,20,21],1)
filter_duplikasi([1,2,4,2,1,2,3,1,],2)