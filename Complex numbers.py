

import cmath

def delta(a, b, c):
    return b ** 2 - 4 * a * c

def quadratic_formula_equal(a, b, c):
    x = -b / (2 * a)
    print("Delta 0 olduğu için çift kök:")
    print("x =", x)

def quadratic_formula_real(a, b, c,d):
    if d == 0:
        x = -b / (2 * a)
        print("Delta 0 olduğu için çift kök:")
        print("x =", x)
    else:
        x1 = (-b + (d ** 0.5)) / (2 * a)
        x2 = (-b - (d ** 0.5)) / (2 * a)
        print("Delta 0'dan büyük olduğu için gerçek kökler:")
        print("Delta: ", d)    
        print("x1 =", x1)
        print("x2 =", x2)


def quadratic_formula_complex(a, b, c,d):
    x1 = (-b + cmath.sqrt(d)) / (2 * a)
    x2 = (-b - cmath.sqrt(d)) / (2 * a)
    print("Delta 0'dan küçük olduğu için karmaşık kökler:")
    print("Delta: ", d)
    print("x1 =", x1)
    print("x2 =", x2)

while True:
    try:
        a = float(input("Değer a: "))
        b = float(input("Değer b: "))
        c = float(input("Değer c: "))
    except ValueError:
        print("Lütfen sadece sayısal değerler girin.")
        continue

    d = delta(a, b, c)

    if d == 0:
        quadratic_formula_equal(a, b, c)
    elif d > 0:
        quadratic_formula_real(a, b, c,d)
    else:
        quadratic_formula_complex(a, b, c,d)

    devam = input("Yeni veri girmek istiyor musunuz? (e/h): ")
    if devam.lower() != "e"s:
        break
    