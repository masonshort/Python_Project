
def Newtons_Iter(f, x_n):
    df = f.derivative()
    return x_n -f(x_n)/df(x_n)


def Newtons_Method(f,x_0, epsilon):
    x = x_0
    while abs(f(x)) > epsilon:
        x = Newtons_Iter(f, x)
    return x;
    