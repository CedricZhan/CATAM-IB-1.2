import math

def f(x,y):
    return -4*y+3*math.exp(-x)

def y_exact(x):
    return math.exp(-x) - math.exp(-4*x)

def update(Y, x, h):
    k1 = h*f(x, Y)
    k2 = h*f(x+0.5*h,Y+0.5*k1)
    k3 = h*f(x+0.5*h,Y+0.5*k2)
    k4 = h*f(x+h, Y+k3)
    Y = Y + (k1+2*k2+2*k3+k4)/6.0
    x = x + h
    return Y, x

def RK4_method(Y, x, n, h):
    res = []
    x_show = round(x, 12)
    res.append((x_show, Y))

    for _ in range(n):
        Y, x = update(Y, x, h)
        x_show = round(x, 12)
        res.append((x_show, Y))
    return res

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

res=[]
for k in range(16):
    res.append(En_xn04(2**k)[-1])
print(res)