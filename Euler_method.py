import numpy as np

def f(x,y):
    return -4*y+3*np.exp(-x)

def update(Y,x,h):
    Y = Y + h*f(x,Y)
    x = x + h
    return Y, x

def y_exact(x):
    return np.exp(-x) - np.exp(-4*x)


def Euler_method(Y, x, n, h):
    res = []
    x_show = round(x, 12)
    y = y_exact(x_show)
    res.append((x_show, Y, y, Y - y))

    for _ in range(n):
        Y, x = update(Y, x, h)
        x_show = round(x, 12)
        y = y_exact(x_show)
        res.append((x_show, Y, y, Y - y))
    return res

def growthrate_estimaton(Y,x,n,h):
    rate = []
    error = []

    for _ in range(n):
        Y, x = update(Y, x, h)
        x_show = round(x, 12)
        y = y_exact(x_show)
        error.append(abs(Y - y))
        if len(error)!=1:
            rate.append((np.log(error[-1])-np.log(error[-2]))/0.6)

    return rate

def En_xn04(n):
    x = 0.0
    Y = 0.0
    y = y_exact(x)
    for _ in range(n):
        Y, x = update(Y, x, 0.4/n)
    x_show = round(x, 12)
    y = y_exact(x_show)
    res = [n,0.4/n,Y-y]   
    return res

xs=[]
ys=[]

for k in range(16):
    xs.append(k)
    (En_xn04(2**k))
