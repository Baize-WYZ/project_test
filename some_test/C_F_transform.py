def transform_CtoF(C_figure):
    F_f = C_figure * 1.8 + 32
    print('%.2f'%F_f,end = 'F')

def transform_FtoC(F_figure):
    C_c = (F_figure - 32) / 1.8
    print('%.2f'%C_c,end = 'C')

x = input('please input data:')
flag = x[-1]
figure = float(x[-len(x):-1])
if flag == 'C' or flag == 'c':
    transform_CtoF(figure)
elif flag == 'F' or flag == 'f':
    transform_FtoC(figure)
else:
    print('输入格式错误')