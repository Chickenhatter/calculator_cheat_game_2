import math
radwdaw = input('rad(101)? ')
A = input('A(angle): ')
B = input('B(angle): ')
C = input('C(angle): ')
D = 0
E = 0
F = 0
a = input('a(size): ')
b = input('b(size): ')
c = input('c(size): ')
h = input('h(area)')
tt = 'Not True'
if radwdaw[0] == 1:
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


if radwdaw[1] == radwdaw[0]:
    if A:
        D = (A)
    if B:
        E = (B)
    if C:
        F = (C)
elif radwdaw[0] == 0:
    if A:
        D = ((A)*(math.pi)/180)
    if B:
        E = ((B)*(math.pi)/180)
    if C:
        F = ((C)*(math.pi)/180)
else:
    if A:
        D = A*180/(math.pi)
    if B:
        E = B*180/(math.pi)
    if C:
        F = C*180/(math.pi)

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
            print('b',b,' = (sin(',E,')*',a,')/(sin(',D,'))')
        if not B and b:
            B = math.asin(b*math.sin(A)/a)
            if radwdaw[1] == 1:
                E = B
            else:
                E = B*180/(math.pi)
            print('B',E,' = sin-1((',b,'*sin(',D,'))/(',a,'))')
        if C and not c:
            c = (math.sin(C)*a)/(math.sin(A))
            print('c',c,' = (sin(',F,')*',a,')/(sin(',D,'))')
        if not C and c:
            C = math.asin(c*math.sin(A)/a)
            if radwdaw[1] == 1:
                F = C
            else:
                F = C*180/(math.pi)
            print('C',F,' = sin-1((',c,'*sin(',D,'))/(',a,'))')
    if B and b:
        if A and not a:
            a = (math.sin(A)*b)/(math.sin(B))
            print('a',a,' = (sin(',D,')*',b,')/(sin(',E,'))')
        if not A and a:
            A = math.asin(a*math.sin(B)/b)
            if radwdaw[1] == 1:
                D = A
            else:
                D = A*180/(math.pi)
            print('A',D,' = sin-1((',a,'*sin(',E,'))/(',b,'))')
        if C and not c:
            c = (math.sin(C)*b)/(math.sin(B))
            print('c',c,' = (sin(',F,')*',b,')/(sin(',E,'))')
        if not C and c:
            C = math.asin(c*math.sin(B)/b)
            if radwdaw[1] == 1:
                F = C
            else:
                F = C*180/(math.pi)
            print('C',F,' = sin-1((',c,'*sin(',E,'))/(',b,'))')
    if C and c:
        if A and not a:
            a = (math.sin(A)*c)/(math.sin(C))
            print('a',a,' = (sin(',D,')*',c,')/(sin(',F,'))')
        if not A and a:
            A = math.asin(a*math.sin(C)/c)
            if radwdaw[1] == 1:
                D = A
            else:
                D = A*180/(math.pi)
            print('A',D,' = sin-1((',a,'*sin(',F,'))/(',c,'))')
        if B and not b:
            b = (math.sin(B)*c)/(math.sin(C))
            print('b',b,' = (sin(',E,')*',c,')/(sin(',F,'))')
        if not B and b:
            B = math.asin(b*math.sin(C)/c)
            if radwdaw[1] == 1:
                E = B
            else:
                E = B*180/(math.pi)
            print('B',E,' = sin-1((',b,'*sin(',F,'))/(',c,'))')

    if not a and b and c and A:
        a = ((b*b+c*c-2*b*c*math.cos(A))**0.5)
        print('a',a,' = sqrt(',b,'^2+',c,'^2-2*',b,'*',c,'*cos(',D,'))')
    if a and not b and c and B:
        b = ((a*a+c*c-2*a*c*math.cos(B))**0.5)
        print('b',b,' = sqrt(',a,'^2+',c,'^2-2*',a,'*',c,'*cos(',E,'))')
    if a and b and not c and C:
        c = ((b*b+a*a-2*b*a*math.cos(C))**0.5)
        print('c',c,' = sqrt(',b,'^2+',a,'^2-2*',b,'*',a,'*cos(',F,'))')
    if a and b and c and not A:
        A = math.acos((c*c+b*b-a*a)/(2*c*b))
        if radwdaw[1] == 1:
            D = A
        else:
            D = A*180/(math.pi)
        print('A',D,' = cos-1((',c,'^2+',b,'^2-',a,'^2)/(2*',c,'*',b,'))')
    if a and b and c and not B:
        B = math.acos((c*c+a*a-b*b)/(2*c*a))
        if radwdaw[1] == 1:
            E = B
        else:
            E = B*180/(math.pi)
        print('B',E,' = cos-1((',c,'^2+',a,'^2-',b,'^2)/(2*',c,'*',a,'))')
    if a and b and c and not C:
        C = math.acos((a*a+b*b-c*c)/(2*a*b))
        if radwdaw[1] == 1:
            F = C
        else:
            F = C*180/(math.pi)
        print('C',F,' = cos-1((',a,'^2+',b,'^2-',c,'^2)/(2*',a,'*',b,'))')

    if A and c and b and not h:
        h = (c*b*math.sin(A))/(2)
        print('h',h,' = (',c,'*',b,'*sin(',D,'))/(2)')
    if B and c and a and not h:
        h = (c*a*math.sin(B))/(2)
        print('h',h,' = (',c,'*',a,'*sin(',E,'))/(2)')
    if C and a and b and not h:
        h = (a*b*math.sin(C))/(2)
        print('h',h,' = (',a,'*',b,'*sin(',F,'))/(2)')
    if A and c and not b and h:
        b = (2*h)/(c*math.sin(A))
        print('b',b,' = (2*',h,')/(',c,'*sin(',D,'))')
    if A and not c and b and h:
        c = (2*h)/(b*math.sin(A))
        print('c',c,' = (2*',h,')/(',c,'*sin(',D,'))')
    if not A and c and b and h:
        A = math.asin((2*h)/(c*b))
        if radwdaw[1] == 1:
            D = A
        else:
            D = A*180/(math.pi)
        print('A',D,' = sin-1((2*',h,')/(',c,'*',b,'))')
    if B and c and not a and h:
        a = (2*h)/(c*math.sin(B))
        print('a',a,' = (2*',h,')/(',c,'*sin(',E,'))')
    if B and not c and a and h:
        c = (2*h)/(a*math.sin(B))
        print('c',c,' = (2*',h,')/(',a,'*sin(',E,'))')
    if not B and c and a and h:
        B = math.asin((2*h)/(c*a))
        if radwdaw[1] == 1:
            E = B
        else:
            E = B*180/(math.pi)
        print('B',E,' = sin-1((2*',h,')/(',c,'*',a,'))')
    if C and a and not b and h:
        b = (2*h)/(a*math.sin(C))
        print('b',b,' = (2*',h,')/(',a,'*sin(',F,'))')
    if C and not a and b and h:
        a = (2*h)/(b*math.sin(C))
        print('a',a,' = (2*',h,')/(',b,'*sin(',F,'))')
    if not C and a and b and h:
        C = math.asin((2*h)/(a*b))
        if radwdaw[1] == 1:
            F = C
        else:
            F = C*180/(math.pi)
        print('C',F,' = sin-1((2*',h,')/(',b,'*',a,'))')
    if A and B and not C:
        C = (math.pi-A-B)
        if radwdaw[1] == 1:
            F = C
        else:
            F = C*180/(math.pi)
        print('C',F,'pi-',D,'-',E)
    if A and not B and C:
        B = (math.pi-A-C)
        if radwdaw[1] == 1:
            E = B
        else:
            E = B*180/(math.pi)
        print('B',E,'pi-',D,'-',F)
    if not A and B and C:
        A = (math.pi-C-B)
        if radwdaw[1] == 1:
            D = A
        else:
            D = A*180/(math.pi)
        print('A',D,'pi-',F,'-',E)


if A and B and C and a and b and c:
    if abs((A+B+C)-math.pi) < 1:
        if (a+b) > c and (a+c) > b and (c+b) > a:
            tt = 'True'
else:
    tt = 'Unknown'
if A and B and C:
    if (A+B+C) == (2*math.pi):
        tt = 'Not True'
if radwdaw[2] == 1:
    if A:
        print('A ',D)
    if B:
        print('B ',E)
    if C:
        print('C ',F)
else:
    if A:
        print('A ',D*180/(math.pi))
    if B:
        print('B ',E*180/(math.pi))
    if C:
        print('C ',F*180/(math.pi))
if a:
    print('a ',a)
if b:
    print('b ',b)
if c:
    print('c ',c)
if h:
    print('h ',h)
print(tt)
