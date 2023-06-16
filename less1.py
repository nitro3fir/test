# Нужно посчитать количество символов в строке (по каждой букве)
# aabbssddfs

# def str_counter(s): # N**2
    # for sym in s:
    #     counter = 0
    #     for sub_sym in s:
    #         if sym == sub_sym:
    #             counter += 1
    #     print(sym, counter)

# def str_counter(s): # N*M
#     for sym in set(s):
#         counter = 0
#         for sub_sym in s:
#             if sym == sub_sym:
#                 counter += 1
#         print(sym, counter)

def str_counter(s): # N
    syms_counter = {}
    for sym in s:
        syms_counter[sym] = syms_counter.get(sym, 0) + 1
    print(syms_counter)

# 9^2 = 81  log9 81 = 2

str_counter("aabbssddfs")