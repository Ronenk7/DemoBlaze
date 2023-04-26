# for i in range(-1, 1):
#     print("#")
# t = [[3-i for i in range(3)] for j in range(3)]
# s = 0
# for i in range(3):
#     s += t[i][i]
# print(s)
# a = 1
# b = 0
# c = a & b
# d = a | b
# e = a ^ b
# print(c + d + e)
# x = 1
# while x < 10:
#     print("#")
#     x = x << 1
# x = [1, 2, 3]
# for i in range(len(x)):
#     x.insert(1, x[i])
# print(x)
# x = [1, 2, 3, 4, 5, 6, 7, 8]
# print(x[::-1])
# dct = {}
# dct["1"] = (1, 2)
# dct["2"] = (2, 1)
#
# for x in dct.keys():
#     print(dct[x][1], end="")
# my_list = [1, 2]
#
# for v in range(2):
#     my_list.insert(-1, my_list[v])
#
# print(my_list)
lst = [[x for x in range(3)] for y in range(3)]

for r in range(3):
    for c in range(3):
        if lst[r][c] % 2 != 0:
            print("#")







