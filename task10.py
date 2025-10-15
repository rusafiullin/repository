def volume():
    print("Введине радиус основания")
    R= int(input())
    print("Введите высоту цилиндра")
    h = int(input())
    V=3.14 * R**2 * h
    print(V)