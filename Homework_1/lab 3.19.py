# Anthony Flores 1792816 CIS2348 3.19
import math

height = int(input('Enter wall height (feet):' '\n'))

width = int(input('Enter wall width (feet):' '\n'))

wall_area = height * width

print('Wall area:', wall_area, 'square feet')

gallon_paint = 350
paint_area = wall_area / gallon_paint

print('Paint needed:', '{:.2f}'.format(wall_area / gallon_paint), 'gallons')
cans = int(math.ceil(paint_area))
print('Cans needed: {} can(s)'.format(cans))
print()

ColorDict = {'red': 35, 'blue': 25, 'green': 23}
color = input('Choose a color to paint the wall:' '\n')

color_cost = ColorDict.get(color)
actual_cost = cans * color_cost
print(f'Cost of purchasing {color} paint: ${actual_cost}')
