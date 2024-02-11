num = int(input())

for i in range(1, num + 1):
    for top in range(i):
        print('*', end='')
    print()

for i in range(num - 1, -1, -1):
    for bot in range(i):
        print('*', end='')
    print()


# num = int(input())
#
# for i in range(1, num + 1):
#     for top in range(0, i):
#         print('*', end='')
#     print()
#
# for i in range(num - 1, 0, -1):
#     for bot in range(0, i):
#         print('*', end='')
#     print()

