import math
A = input('A(angle): ')
B = input('B(angle): ')
C = input('C(angle): ')
a = input('a(size): ')
b = input('b(size): ')
c = input('c(size): ')
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
    
    if not a and b and c and A:
        a = ((b*b+c*c-2*bc*math.cos(A))**0.5)
    
    if a and not b and c and B:
        b = ((a*a+c*c-2*ac*math.cos(B))**0.5)
    
    if a and b and not c and C:
        c = ((b*b+a*a-2*ba*math.cos(C))**0.5)


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