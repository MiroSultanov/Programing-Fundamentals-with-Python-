from math import sqrt

def center_point_func(x, y):
    dist_x = sqrt(abs(x[0] ** 2)) + (abs(x[1] ** 2))
    dist_y = sqrt(abs(y[0] ** 2)) + (abs(y[1] ** 2))
    if dist_x < dist_y:
        output = (int(x[0] // 1)), int(x[1] // 1)
    elif dist_y < dist_x:
        output = (int(y[0 // 1])), int(y[1] // 1)
    else:
        output = (int(x[0]// 1)), int(x[1] // 1)
    print(output)

point_1 = (float(input()),float(input()))
point_2 = (float(input()),float(input()))
center_point_func(point_1, point_2)