import math
radwdaw = int(input('rad(1)? '))
A = input('A(angle): ')
B = input('B(angle): ')
C = input('C(angle): ')
a = input('a(size): ')
b = input('b(size): ')
c = input('c(size): ')
h = input('h(area)')
tt = 'Not True'
if radwdaw == 1:
    if A:
        A = float(A)
    if B:
        B = float(B)
    if C:
        C = float(C)
else:
    if A:
        A = float(A)
        A = ((A)*(math.pi)/180)
    if B:
        B = float(B)
        B = ((B)*(math.pi)/180)
    if C:
        C = float(C)
        C = ((C)*(math.pi)/180)
if a:
    a = float(a)
if b:
    b = float(b)
if c:
    c = float(c)

for i in range(6):
    if A and a:
        if B and not b:
            b = (math.sin(B)*a)/(math.sin(A))
            print(f'{b} = (sin({B})*{a})/(sin({A}))')
        if not B and b:
            B = math.asin(b*math.sin(A)/a)
            print(f'{B} = sin-1(({b}*sin({A}))/({a}))')
        if C and not c:
            c = (math.sin(C)*a)/(math.sin(A))
            print(f'{c} = (sin({C})*{a})/(sin({A}))')
        if not C and c:
            C = math.asin(c*math.sin(A)/a)
            print(f'{C} = sin-1(({c}*sin({A}))/({a}))')
    if B and b:
        if A and not a:
            a = (math.sin(A)*b)/(math.sin(B))
            print(f'{a} = (sin({A})*{b})/(sin({B}))')
        if not A and a:
            A = math.asin(a*math.sin(B)/b)
            print(f'{A} = sin-1(({a}*sin({B}))/({b}))')
        if C and not c:
            c = (math.sin(C)*b)/(math.sin(B))
            print(f'{c} = (sin({C})*{b})/(sin({B}))')
        if not C and c:
            C = math.asin(c*math.sin(B)/b)
            print(f'{C} = sin-1(({c}*sin({B}))/({b}))')
    if C and c:
        if A and not a:
            a = (math.sin(A)*c)/(math.sin(C))
            print(f'{a} = (sin({A})*{c})/(sin({C}))')
        if not A and a:
            A = math.asin(a*math.sin(C)/c)
            print(f'{A} = sin-1(({a}*sin({C}))/({c}))')
        if B and not b:
            b = (math.sin(B)*c)/(math.sin(C))
            print(f'{b} = (sin({B})*{c})/(sin({C}))')
        if not B and b:
            B = math.asin(b*math.sin(C)/c)
            print(f'{B} = sin-1(({b}*sin({C}))/({c}))')

    if not a and b and c and A:
        a = ((b*b+c*c-2*b*c*math.cos(A))**0.5)
        print(f'{a} = sqrt({b}^2+{c}^2-2*{b}*{c}*cos({A}))')
    if a and not b and c and B:
        b = ((a*a+c*c-2*a*c*math.cos(B))**0.5)
        print(f'{b} = sqrt({a}^2+{c}^2-2*{a}*{c}*cos({B}))')
    if a and b and not c and C:
        c = ((b*b+a*a-2*b*a*math.cos(C))**0.5)
        print(f'{c} = sqrt({b}^2+{a}^2-2*{b}*{a}*cos({C}))')
    if a and b and c and not A:
        A = math.acos((c*c+b*b-a*a)/(2*c*b))
        print(f'{A} = cos-1(({c}^2+{b}^2-{a}^2)/(2*{c}*{b}))')
    if a and b and c and not B:
        B = math.acos((c*c+a*a-b*b)/(2*c*a))
        print(f'{B} = cos-1(({c}^2+{a}^2-{b}^2)/(2*{c}*{a}))')
    if a and b and c and not C:
        C = math.acos((a*a+b*b-c*c)/(2*a*b))
        print(f'{C} = cos-1(({a}^2+{b}^2-{c}^2)/(2*{a}*{b}))')

    if A and c and b and not h:
        h = (c*b*math.sin(A))/(2)
        print(f'{h} = ({c}*{b}*sin({A}))/(2)')
    if B and c and a and not h:
        h = (c*a*math.sin(B))/(2)
    if C and a and b and not h:
        h = (a*b*math.sin(C))/(2)
    if A and c and not b and h:
        b = (2*h)/(c*math.sin(A))
    if A and not c and b and h:
        c = (2*h)/(b*math.sin(A))
    if not A and c and b and h:
        A = math.asin((2*h)/(c*b))
    if B and c and not a and h:
        a = (2*h)/(c*math.sin(B))
    if B and not c and a and h:
        c = (2*h)/(a*math.sin(B))
    if not B and c and a and h:
        B = math.asin((2*h)/(c*a))
    if C and a and not b and h:
        b = (2*h)/(a*math.sin(C))
    if C and not a and b and h:
        a = (2*h)/(b*math.sin(C))
    if not C and a and b and h:
        C = math.asin((2*h)/(a*b))
    if A and B and not C:
        C = (math.pi-A-B)
    if A and not B and C:
        B = (math.pi-A-C)
    if not A and B and C:
        A = (math.pi-C-B)


if A and B and C and a and b and c:
    if abs((A+B+C)-math.pi) < 1:
        if (a+b) > c and (a+c) > b and (c+b) > a:
            tt = 'True'
else:
    tt = 'Unknown'
if A and B and C:
    if (A+B+C) == (2*math.pi):
        tt = 'Not True'
if radwdaw == 1:
    if A:
        print('A ',A)
    if B:
        print('B ',B)
    if C:
        print('C ',C)
else:
    if A:
        print('A ',A*180/(math.pi))
    if B:
        print('B ',B*180/(math.pi))
    if C:
        print('C ',C*180/(math.pi))
if a:
    print('a ',a)
if b:
    print('b ',b)
if c:
    print('c ',c)
if h:
    print('h ',h)
print(tt)