import numpy as np

delta=20

def f1(t, y1, y2):
    return y2

def f2(t, y1, y2):
    return (-delta**3)*(y1**2)*y2 - y1 + np.sin(t)

def update(Y1, Y2, x, h):
    k11 = h * f1(x, Y1, Y2)
    k12 = h * f2(x, Y1, Y2)

    k21 = h * f1(x + 0.5*h, Y1 + 0.5*k11, Y2 + 0.5*k12)
    k22 = h * f2(x + 0.5*h, Y1 + 0.5*k11, Y2 + 0.5*k12)

    k31 = h * f1(x + 0.5*h, Y1 + 0.5*k21, Y2 + 0.5*k22)
    k32 = h * f2(x + 0.5*h, Y1 + 0.5*k21, Y2 + 0.5*k22)

    k41 = h * f1(x + h, Y1 + k31, Y2 + k32)
    k42 = h * f2(x + h, Y1 + k31, Y2 + k32)

    Y1 = Y1 + (k11 + 2*k21 + 2*k31 + k41) / 6.0
    Y2 = Y2 + (k12 + 2*k22 + 2*k32 + k42) / 6.0
    x  = x + h

    return Y1, Y2, x

def RK4_2nd_order(Y1, Y2, x, n, h):
    res = []

    x_show = float(round(x, 12))

    res.append([x_show, float(Y1)])

    for _ in range(n):
        Y1, Y2, x = update(Y1, Y2, x, h)
        x_show = float(round(x, 6))
        res.append([x_show, float(Y1)])

    return res

print([i[0] for i in RK4_2nd_order(0,0,0,1500,0.04)])