def demo(x):
    return lambda a:a*x
d=demo(5)
print(d(11))