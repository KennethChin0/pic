import random
img = open('pic.ppm', 'w')
img.write('P3\n500 500\n255\n')

for x in range(500):
    if (x < 250):
        x = 250 - x
    row = ""
    for y in range(2):
        r = 0
        if y % 2 == 0:
            for z in range(250):
                row += (str(r) + ' ' + str(x % 250) + ' ' + str(z % 250) + ' ')
        else:
            for z in range(250):
                row += (str(r) + ' ' + str(x % 250) + ' ' + str(250 - z % 250) + ' ')
    img.write((row + '\n'))
img.close()
