import math
  

l = float(input('rad(1)? '))
radius = float(input('radius: '))
angle = float(input('angle: '))
if l == 1:
  asi = (angle*radius)
  aos = (1/2)*radius*radius*angle
else:
  asi = ((angle/360)*2*math.pi*radius)
  aos = ((angle/360)*math.pi*radius*radius)
if l == 1:
  aot = (0.5*radius*radius*math.sin(angle))
else:
  aot = (0.5*radius*radius*math.sin(angle*(math.pi/180)))
  aosh = aos-aot


print(asi,'arc size')
print(aos,'area of sector')
print(aot, 'area of triangle')
print(aosh, 'area of shade')
  
