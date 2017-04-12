# x=['X','X','X','0','0','0','X','X','X']
# print(' |   |    |')
# print(' '+x[8]+   ' |'  +x[7]+  ' |'+x[6])
# print('-----------')
# print(' '+x[5]+   ' |'  +x[4]+  ' |'+x[3])
# print('-----------')
# print(' '+x[2]+   ' |'  +x[1]+  ' |'+x[0])

# def input():
#     marker=''
#     while not (marker=='o' or marker=='x'):
#         marker=input('nothon x or y',marker)
#
#     if marker=='x':
#         return('X','O')
#     else:
#         return ('X','O')


marker=''
marker=input('enter the value x or 0 ').upper()
if marker=='X':
    print('x and o')
elif marker=='0':
    print('o and x')
else:
    pass


