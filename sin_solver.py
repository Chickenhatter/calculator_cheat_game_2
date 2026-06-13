import math
A = input('A(angle): ')
B = input('B(angle): ')
C = input('C(angle): ')
a = input('a(size): ')
b = input('b(size): ')
c = input('c(size): ')
h = input('h(area)')
tt = 'Not True'
if A:
    A = float(A)
    A = (math.radians(A))
if B:
    B = float(B)
    B = (math.radians(B))
if C:
    C = float(C)
    C = (math.radians(C))
if a:
    a = float(a)
if b:
    b = float(b)
if c:
    c = float(c)

for i in range(6):
    # a = b = c
    if A and a:
        if B and not b:
            b = (math.sin(B)*a)/(math.sin(A))
        if not B and b:
            B = math.asin(b*math.sin(A)/a)
        if C and not c:
            c = (math.sin(C)*a)/(math.sin(A))
        if not C and c:
            C = math.asin(c*math.sin(A)/a)
    if B and b:
        if A and not a:
            a = (math.sin(A)*b)/(math.sin(B))
        if not A and a:
            A = math.asin(a*math.sin(B)/b)
        if C and not c:
            c = (math.sin(C)*b)/(math.sin(B))
        if not C and c:
            C = math.asin(c*math.sin(B)/b)
    if C and c:
        if A and not a:
            a = (math.sin(A)*c)/(math.sin(C))
        if not A and a:
            A = math.asin(a*math.sin(C)/c)
        if B and not b:
            b = (math.sin(B)*c)/(math.sin(C))
        if not B and b:
            B = math.asin(b*math.sin(C)/c)
    

    #a^2=b^2+c^2-2bccosA
    if not a and b and c and A:
        a = ((b*b+c*c-2*b*c*math.cos(A))**0.5)
    if a and not b and c and B:
        b = ((a*a+c*c-2*a*c*math.cos(B))**0.5)
    if a and b and not c and C:
        c = ((b*b+a*a-2*b*a*math.cos(C))**0.5)
    if a and b and c and not A:
        A = math.acos((c*c+b*b-a*a)/(2*c*b))
    if a and b and c and not B:
        B = math.acos((c*c+a*a-b*b)/(2*c*a))
    if a and b and c and not C:
        C = math.acos((a*a+b*b-c*c)/(2*a*b))


    # h=1/2sinabc
    if A and c and b and not h:
        h = (c*b*math.sin(A))/(2)
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
        print(C)
    if A and not B and C:
        B = (math.pi-A-C)
    if not A and B and C:
        A = (math.pi-C-B)






if A and B and C and a and b and c:
    if abs((A+B+C)-math.pi) < 1:
        if (a+b) > c and (a+c) > b and (c+b) > a:
            tt = 'True'
    else:
        print('gg')
else:
    tt = 'Unknown'







if A:
    print('A ',math.degrees(A))
if B:
    print('B ',math.degrees(B))
if C:
    print('C ',math.degrees(C))
if a:
    print('a ',a)
if b:
    print('b ',b)
if c:
    print('c ',c)
if h:
    print('h ',h)
print(tt)