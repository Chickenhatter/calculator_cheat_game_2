import math
A = input('A(angle): ')
B = input('B(angle): ')
C = input('C(angle): ')
a = input('a(size): ')
b = input('b(size): ')
c = input('c(size): ')
if A and a:
    if B and not b:
        b = (math.sin(B)*a)/(math.sin(A))
    if B and not b:
        B = math.asin(b*math.sin(A)/a)
    
    if C and not c:
        c = (math.sin(C)*a)/(math.sin(A))
    if C and not c:
        C = math.asin(c*math.sin(A)/a)


if B and b:
    if A and not a:
        a = (math.sin(A)*b)/(math.sin(B))
    if A and a:
        A = math.asin(a*math.sin(B)/b)
    
    if C and c:
        c = (math.sin(C)*b)/(math.sin(B))
    if C and c:
        C = math.asin(c*math.sin(B)/b)


if C and c:
    if A and a:
        a = (math.sin(A)*c)/(math.sin(C))
    if A and a:
        A = math.asin(a*math.sin(C)/c)
    
    if B and b:
        b = (math.sin(B)*c)/(math.sin(C))
    if B and b:
        B = math.asin(b*math.sin(C)/c)




print(A)
print(B)
print(C)
print(a)
print(b)
print(c)