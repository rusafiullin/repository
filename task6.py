def pot_energy():
    print("Введите массу в кг")
    m = int(input())
    print("Высоту в метрах")
    h = int(input())
    print("Введите ускорение свободного падения")
    g = int(input())
    P = m*g*h
    print(P)