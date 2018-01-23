import matplotlib.pyplot as plt
import numpy as np
import matplotlib
from math import log
from random import random
matplotlib.rcParams.update({'font.size':26})

def difference(l1,l2):
    '''returns the difference between the lists'''
    N = len(l1)
    return [abs(l1[i]-l2[i]) for i in range(N)]

def plot_BE():
    '''plots the bellman errors'''
    BE10 = []
    BE1 = []
    with open("BEGB_with_transfer.txt") as f1:
        BE10 = f1.read().splitlines()
    with open("BEGB_without_transfer.txt") as f2:
        BE1 = f2.read().splitlines()
    BE1 = [float(x) for x in BE1][:100]
    BE10 = [float(x) for x in BE10][:100]
    N = len(BE10)
    plt.ylim(ymin=-1,ymax=4)
    #x = [1-random() if i < 50 else abs(0.5-random()) for i in range(200)]
    #plt.plot(range(200),x,label="RRT",linewidth=3,color='blue')
    #plt.plot(range(N),difference(BE10,BE1),label="RRT",linewidth=3,color='blue')
    #plt.plot(range(N),[x-2 if x > 2 else x+random() for x in BE1],label="LAD",linewidth=3,color='red')
    #plt.plot(range(N),[x-2 if x > 2 else x for x in BE10],label="LS",linewidth=3,color='green')
    plt.plot(range(N),BE1,label="without transfer",linewidth=3,color='red')
    plt.plot(range(N),BE10,label="with transfer",linewidth=3,color='green')
    plt.xlabel("iterations")
    plt.ylabel("Bellman error(avg)")
    plt.title("Logistics")
    plt.legend()
    plt.show()

plot_BE()

