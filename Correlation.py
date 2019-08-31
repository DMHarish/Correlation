import numpy as np
import math

# y=mx+b (y-bar and x-bar)

class correlation:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # print(self.x)
        # print(self.y)

        if len(self.x) != len(self.y):
            print("the number of values in x and y not same:")
        else:
            print("both list have same numbers")

    def correlate(self):
        # print('hi')
        a = []
        b = []
        s = 0
        for i in self.x:
            # print(i)
            s = s + i
            avgx = s / len(self.x)  # x-bar

        for i in self.x:
            a.append(i - avgx)  # x0-xbar
        # print(avgx)
        # print(a)

        t = 0
        for j in self.y:
            t = t + j
            avgy = t / len(self.y)  # y-bar
        for j in self.y:
            b.append(j - avgy)  # y0-ybar

        # print(avgy)
        # print(b)
        c = 0
        list3 = []
        for i, j in zip(a, b):
            list3.append(i * j)
        # print(list3)
        sum = 0
        for i in list3:
            sum = sum + i

        # print(sum)
        list4 = []
        for i in self.x:
            list4.append((i - avgx) * (i - avgx))
        # print(list4)
        list5 = []
        for j in self.y:
            list5.append((j - avgy) * (j - avgy))
        # print(list5)
        sumx = 0
        for i in list4:
            sumx = sumx + i
        # print(sumx)
        sumy = 0
        for j in list5:
            sumy = sumy + j
        # print(sumy)
        mulxy = sumx * sumy
        # print(mulxy)
        sqroot = math.sqrt(mulxy)
        # print(sqroot)
        r = sum / sqroot
        return r

    # m=r*Sy/Sx ---> stand deviation of x and y

    def slope_m(self):
        s_x = np.std(self.x)
        s_y = np.std(self.y)

        slope_m = self.correlate() * s_y / s_x
        return slope_m

    # b=(y-bar)-m(x-bar)
    # b=y-mx

    def find_b(self):
        fb = np.mean(self.y) - self.slope_m() * np.mean(self.x)
        return fb

    # ybar=m*xbar+b
    def predication(self, new_x):
        new_y = self.slope_m() * np.mean(new_x) + self.find_b()
        return new_y


cr = correlation([3, 4, 5], [6, 7, 8])
print(cr.correlate())
print(cr.slope_m())
print(cr.find_b())
print(cr.predication([9, 10, 11]))




