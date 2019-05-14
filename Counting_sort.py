def counting_sort(list_a):
    list_b = list_a[:]
    list_c = []
    num = max(list_a)+1
    for i in range(num):
        list_c.append(0)
    for j in range(len(list_a)):
        list_c[list_a[j]] += 1
    for i in range(1, num):
        list_c[i] += list_c[i-1]
    for j in range(len(list_a)-1, -1, -1):
        list_b[list_c[list_a[j]]-1] = list_a[j]
        list_c[list_a[j]] -= 1
    return list_b

a = [2, 5, 3, 0, 2, 3, 0, 3, 4, 7, 11]

b = counting_sort(a)
print(b)