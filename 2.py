x1 = int(input('Координата X первой точки: '))
y1 = int(input('Координата Y первой точки: '))
x2 = int(input('Координата X второй точки: '))
y2 = int(input('Координата Y второй точки: '))

if (x1>0 and y1>0 and x2>0 and y2>0) or (x1<0 and y1>0 and x2<0 and y2>0) or (x1<0 and y1<0 and x2<0 and y2<0) or (x1>0 and y1<0 and x2>0 and y2<0):
    print('YES')
else:
    print('NO')