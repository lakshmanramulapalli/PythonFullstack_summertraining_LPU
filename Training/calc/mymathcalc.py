from mymathcalc import area_of_circle, area_of_sq, circum_of_circle

radius  = int(input('Radius: '))
print(f'Area of circle {area_of_circle(radius)}')
print(f'Circum of circle {circum_of_circle(radius)}')

side = int(input('Side: '))
print(f'Area of square {area_of_sq(side)}')


