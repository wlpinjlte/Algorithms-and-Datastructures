# counter = 0
#     Z = [False for _ in range(n)]
#     d = 'A'
#     c = 0
#     while counter < n:
#         i = 0
#         while i < n:
#             if not Z[i] and disk[i] == d:
#                 for j in depends[i]:
#                     if not Z[j]:
#                         i += 1
#                         break
#                 else:
#                     #print(i)
#                     Z[i] = True
#                     counter += 1
#                     i = 0
#             else:
#                 i += 1
#
#         c += 1
#         if d == 'A':
#             d = 'B'
#         else:
#             d = 'A'