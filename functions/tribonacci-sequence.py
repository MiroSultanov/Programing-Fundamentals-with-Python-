def tribonachi(x):
    num_list = [0,0,1]
    for _ in range(x - 1):
        num_list.append(sum(num_list[-3:]))
    return num_list[-x:]


num = int(input())
output = ' '.join([str(x) for x in tribonachi(num)])

print(output)