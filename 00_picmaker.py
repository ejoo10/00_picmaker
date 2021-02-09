from random import *
import math
import cmath
import colorsys

def dot(x, y):
    s = [0, 0, 0]
    for k in range(3):
        for i in range(len(x)):
            for j in range(len(x)):
                s[k] += x[i][j] * y[i][j][k]
    return s

def Kernel(array, matrix):
    w = len(array)
    h = len(array[0])
    new = [[[0, 0, 0] for i in range(h)] for i in range(w)]
    b = 1
    for i in range(w):
        for j in range(h):
            c = [[[0 for p in range(2*b+1)] for q in range(2*b+1)] for r in range(3)]
            for x in range(-b, b+1):
                for y in range(-b, b+1):
                    c[x+1][y+1] = array[(i + x + w) % w][(j + y + h) % h]
            new[i][j] = dot(matrix, c);
    return new

def f(z):
    if (z!=0):
        return cmath.sin(z**(-1))
    else:
        return 0

def image():
    a = open("00_picmaker.ppm", "w")
    a.write("P3 501 501 255 \n")
    data = [[[0, 0, 0] for i in range(501)] for j in range(501)]
    for i in range(501):
        for j in range(501):
            z = complex((i-251)/250.0, (j-251)/250.0)
            for o in range(2):
                z = f(z)
            theta = (cmath.phase(z)/cmath.pi/2 + 0.5) % 1
            data[i][j] = colorsys.hls_to_rgb(theta, abs(z) ** 0.5/(abs(z)+1) ** 0.5, 1)

    blur = [[.0625, .125, .0625], [.125, .25, .125], [.0625, .125, .0625]]

    #for i in range(10):
    data = Kernel(data, blur)

    for j in range(501):
        for i in range(501):
            a.write(str(int(255*data[i][j][0])) + " " + str(int(255*data[i][j][1])) + " " + str(int(255*data[i][j][2])) + " ")
        a.write("\n")

    a.close()

image()
