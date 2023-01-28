x1, y1 = map(int, input('Координаты первой точки (x, y ): ').split())

x2, y2 = map(int, input('Координаты первой точки (x, y ): ').split())

S = round(((x2 - x1)**2 + (y2 - y1)**2 )**(1/2), 3)

print(S)