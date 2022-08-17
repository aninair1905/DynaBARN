import random
from numpy.random import random_sample
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np
import math
from random import choice
import scipy.stats as ss


def distance(start_location,end_location):
    distance = math.sqrt(((start_location[0] - end_location[0]) ** 2) + ((start_location[1] - end_location[1]) ** 2))
    return distance

def gen_points(n):
    x_s = []
    y_s = []
    for i in range(n):
        # x = round(random.uniform(-10,10),1)
        # y = round(random.uniform(-10,10),1)

        #change these numbers based on the start and end points
        x = round(random.randint(-10,10),1)
        y = round(random.randint(-10,10),1)
        x_s.append(x)
        y_s.append(y)

    return x_s, y_s
def get_random_traj_points(order):

    n=order
    x_s, y_s = gen_points(n + 1)

    z = np.polyfit(x_s, y_s, n)

    p = np.poly1d(z)
    xp = np.linspace(-10,10, 10)
    xp, pxp = xp, p(xp)
    #find where y = 10 and -10
    x_10 = (p - (10)).roots
    x_neg10 = (p - (-10)).roots

    #find where x = 10, -10
    y_10 = p(10)
    y_neg10 = p(-10)

    #check if there are any imaginary components
    # if there are, then disregard them
    if (not (x_10.imag.any(0))):
        x_s = np.concatenate((x_s, x_10.real), axis=None)
        for i in x_10:
            y_s = np.append(y_s,10)
        # print(type(x_s))
        # print(x_10,x_10.imag)
        # print("x_s",x_s)
        # print("y_s",y_s)
    if ( not(x_neg10.imag.any(0))):
        x_s = np.concatenate((x_s, x_neg10.real), axis=None)
        for i in x_10:
            y_s = np.append(y_s,-10)
        # print(type(x_s))
        # print(x_neg10,x_neg10.imag)
        # print("x_s",x_s)
        # print("y_s",y_s)

    if ( not(y_10.imag.any(0))):
        y_s = np.concatenate((y_s, y_10), axis=None)
        x_s = np.append(x_s, 10)
        # print(type(y_s))
        # print(y_10,y_10.imag)
        # print("y_s",y_s)
        # print("x_s",x_s)
    if ( not(y_neg10.imag.any(0))):
        y_s = np.concatenate((y_s, y_neg10), axis=None)
        x_s = np.append(x_s, -10)
        # print(type(y_s))
        # print(y_neg10,y_neg10.imag)
        # print("y_s",y_s)
        # print("x_s",x_s)


    xp = np.append(xp, x_s)
    pxp = np.append(pxp, y_s)

    points = []

    for i in range(len(xp)):
        if (-10 <= xp[i] and xp[i] <= 10) and (-10 <= pxp[i] and pxp[i] <= 10):
            points.append((xp[i], pxp[i]))

    seen = set()
    uniq = [x for x in points if x not in seen and not seen.add(x)]
    uniq = sorted(uniq, key=lambda x: x[0])

    #get border points and put them at the beginning and the end of the sequence
    border_points = []
    normal_points = []
    for i in uniq:
        if (i[0]==10) or (i[0]==-10) or (i[1]==10) or (i[1]==-10):
            border_points.append(i)
        else:
            normal_points.append(i)
    # print("border points", border_points)
    # print('normal points', normal_points)
    border_points = sorted(border_points, key=lambda x: x[0])
    if len(border_points) == 0:
        for i in range(2):
            b = 10
            a = -10
            r = (b - a) * random_sample() + a
            random_point = choice([(choice([a, b]), r), (r, choice([a, b]))])
            border_points.append(random_point)
    if len(border_points) == 1:
        b = 10
        a = -10
        r = (b - a) * random_sample() + a
        random_point = choice([(choice([a, b]), r), (r, choice([a, b]))])
        border_points.append(random_point)
    start_border_point = border_points.pop(0)
    end_border_point = border_points.pop(-1)
    if not border_points:
        uniq = normal_points + border_points
    else:
        uniq = normal_points

    uniq = sorted(uniq, key=lambda x: x[0])
    uniq.insert(0,start_border_point)
    uniq.insert(len(uniq), end_border_point)

    #reverse trajectory at random
    if random.choice([0, 1]) < .5:
        uniq.reverse()

    new_x = []
    new_y = []
    for i in uniq:
        new_x.append(i[0])
        new_y.append(i[1])

    return new_x, new_y, uniq

def calc_time(x,y, points,avg_speed, min_speed, max_speed, std ):
    speeds = np.arange(min_speed, max_speed, 0.1)
    times = [0]
    for i in range(0,len(points)-1):
        d = distance(points[i], points[i+1])
        print('SPEEDS:', speeds)
        print("AVG SPEED:", avg_speed)
        print("STD SPEED:", std)
        prob = ss.norm.pdf(speeds, loc=avg_speed, scale=std)
        print('PROB 1:', prob)
        prob = prob / prob.sum()
        print('PROB 2:', prob)
        speed = 0
        while (speed == 0) or (speed < 0):
            speed = np.random.choice(speeds, 1, p=prob)
        delta_time = d / speed
        next_time = delta_time + times[-1]
        times.append(next_time[0])
    return times
