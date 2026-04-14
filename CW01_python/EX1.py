import csv
import math


def transform_Coordinate_Cartesian2Spherical(x, y):
    r = (x ** 2+y ** 2)**0.5
    theta = math.atan(y/x)
    return [r, theta]


writer = open('circular_data.csv', 'w+', newline='')
lines_write = csv.writer(writer)

reader = open('xy_data.csv', 'r', newline='')
lines_read = list(csv.reader(reader))

for row in range(len(lines_read)):
    if(row == 0):
        lines_write.writerow(['', 'r', 'theta[rad]'])
        continue
    x, y = int(lines_read[row][1]), int(lines_read[row][2])
    [r, theta] = transform_Coordinate_Cartesian2Spherical(x, y)
    lines_write.writerow([row-1, r, theta])

writer.close()
reader.close()
