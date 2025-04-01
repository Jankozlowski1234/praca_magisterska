import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random


A = 30
B= 30
C=3


def create_upper_tilling(A,B,C):
    col = {}
    ver = {}
    change_to_green = False
    B0 = (B,0)
    for j in range(A+B):
        change_to_red = False
        for i in range(2*C+A+B-1):
            col[(i, j)] = "pink"
            rysuj = False

            b = B % 2
            if (i + j + b) % 2 == 0:
                l = (i, j)
                r = (i + 2, j)

            else:
                l = (i, j + 1)
                r  = (i + 2, j + 1)
            if (l[1] >= -l[0] + B) & (l[1] <= l[0] + B) & (r[1] >= r[0] - (B + 2 * C)) & (
                    r[1] <= -r[0] + (2 * A + B + 2 * C)):
                rysuj = True

            if rysuj:
                b = B%2
                if (i+j+b)%2==0:
                    ver[(i,j)] = np.array([(i,j),(i+2,j),(i+1,j+1)])
                else:
                    ver[(i,j)] = np.array([(i,j+1),(i+2,j+1),(i+1,j)])
                if (not change_to_green and ([B0,(B0[0]+2,B0[1]),(B0[0]+1,B0[1]+1)] == ver[(i,j)]).all() )or\
                        (change_to_green and ([(B0[0]-1,B0[1]+1),(B0[0]+1,B0[1]+1),B0] == ver[(i,j)]).all()):
                    change_to_red = True
                    if change_to_green:
                        B0 = (B0[0] -1, B0[1] + 1)
                    else:
                        B0 = (B0[0]+1,B0[1]+1)
                if change_to_red:
                    if change_to_green:
                        col[(i, j)] = "green"
                    else:
                        col[(i, j)] = "red"
                else:
                    col[(i, j)] = "blue"
        if B0 == (B + A, A):
            change_to_green = True
    return (ver,col)

def create_lower_tilling(A,B,C):
    col = {}
    ver = {}
    change_to_red = False
    B0 = (B+2*C,0)
    for j in range(A+B):
        change_to_blue = False
        for i in range(2*C+A+B-1):
            col[(i, j)] = "pink"
            rysuj = False

            b = B % 2
            if (i + j + b) % 2 == 0:
                l = (i, j)
                r = (i + 2, j)

            else:
                l = (i, j + 1)
                r  = (i + 2, j + 1)
            if (l[1] >= -l[0] + B) & (l[1] <= l[0] + B) & (r[1] >= r[0] - (B + 2 * C)) & (
                    r[1] <= -r[0] + (2 * A + B + 2 * C)):
                rysuj = True

            if rysuj:
                b = B%2
                if (i+j+b)%2==0:
                    ver[(i,j)] = [(i,j),(i+2,j),(i+1,j+1)]
                else:
                    ver[(i,j)] = [(i,j+1),(i+2,j+1),(i+1,j)]
                if (not change_to_red and [(B0[0]-1,B0[1]+1),(B0[0]+1,B0[1]+1),(B0[0],B0[1])] == ver[(i,j)] )or\
                        (change_to_red and [(B0[0],B0[1]),(B0[0]+2,B0[1]),(B0[0]+1,B0[1]+1)] == ver[(i,j)]):
                    change_to_blue = True
                    if change_to_red:
                        B0 = (B0[0] +1, B0[1] + 1)
                    else:
                        B0 = (B0[0]-1,B0[1]+1)
                if change_to_blue:
                    col[(i, j)] = "blue"
                elif change_to_red:
                    col[(i, j)] = "red"
                else:
                    col[(i, j)] = "green"
        if B0 == (2*C, B):
            change_to_red = True
    return (ver,col)




def if_two_dict_equal(d1,d2):
    if len(d2)>len(d1):
        return False
    for key, value in d1.items():
        if d2[key]!= value:
            return False
    return True

def how_can_swap(i,j,col):
    if (col[(i-2,j)]=="blue")&(col[(i-2,j-1)]=="blue"):
        if (col[(i - 1, j)] == "green") & (col[(i, j)] == "green"):
            if (col[(i - 1, j-1)] == "red") & (col[(i, j-1)] == "red"):
                return 1
    if (col[(i,j)]=="blue")&(col[(i,j-1)]=="blue"):
        if (col[(i - 1, j)] == "red") & (col[(i-2, j)] == "red"):
            if (col[(i - 1, j-1)] == "green") & (col[(i-2, j-1)] == "green"):
                return 2
    return 0

def swap_collors(i,j,col,alpha = 0.9):
    if alpha > np.random.uniform(0,1,1):
        return False
    nr = how_can_swap(i,j,col)
    if nr == 1:
        col[(i - 2, j)] = "red"
        col[(i - 1, j)] = "red"
        col[(i - 1, j - 1)] = "green"
        col[(i - 2, j - 1)] = "green"
        col[(i, j)] = "blue"
        col[(i, j - 1)] = "blue"
        return True
    if nr == 2:
        col[(i - 2, j - 1)] = "blue"
        col[(i - 2, j)] = "blue"
        col[(i - 1, j)] = "green"
        col[(i, j)] = "green"
        col[(i - 1, j - 1)] = "red"
        col[(i, j - 1)] = "red"
        return True
    return False

x_to_chose = []
y_to_chose = []
for i in range(A+B+2*C+1):
    for j in range(1,A+B):
        if (i+j-B)%2 ==0:
            if (j > -i + B) & (j < i + B) & (j > i - (B + 2 * C)) & (
                    j < -i + (2 * A + B + 2 * C)):
                x_to_chose.append(i)
                y_to_chose.append(j)
X_to_chose = np.array(x_to_chose)
Y_to_chose = np.array(y_to_chose)
n_to_chose = len(x_to_chose)


ver_u,col_u = create_upper_tilling(A,B,C)
ver_l,col_l = create_lower_tilling(A,B,C)
t = 1
sampled_points = [random.sample(range(n_to_chose),1)[0]]
c_u = col_u.copy()
c_l = col_l.copy()
while if_two_dict_equal(c_u,c_l):
    c_u = col_u.copy()
    c_l = col_l.copy()
    sp = [0 for _ in range(2*t)]
    for i in range(len(sp)):
        if i<t:
            sp[i] = random.sample(range(n_to_chose),1)[0]
        else:
            sp[i] = sampled_points[i-t]
    sampled_points = sp
    t *=2
    for k in sampled_points:
        i = x_to_chose[k]
        j = y_to_chose[k]
        swap_collors(i, j, c_u)
        swap_collors(i, j, c_l)
    print(t)





def create_god_swap(A,B,C,X_to_chose,Y_to_chose,swapes = 10**6):
    ver,col = create_upper_tilling(A,B,C)
    for _ in range(swapes):
        x_to_chose = []
        y_to_chose = []
        for i,j in zip(X_to_chose,Y_to_chose):
            if how_can_swap(i, j, col) > 0:
                x_to_chose.append(i)
                y_to_chose.append(j)
        x_to_chose = np.array(x_to_chose)
        y_to_chose = np.array(y_to_chose)
        n_to_chose = len(x_to_chose)
        k = random.sample(range(n_to_chose), 1)[0]
        i = x_to_chose[k]
        j = y_to_chose[k]
        swap_collors(i, j, col)
        if _%(swapes/100) ==0:
            print(f"{int(100*_/swapes)}%")
    return (ver,col)


ver,col = create_god_swap(A =A ,B = B,C = C,X_to_chose = X_to_chose,Y_to_chose = Y_to_chose,swapes = 10**7)
plt.figure()

plt.xlim(0,A+B+2*C+1)
plt.ylim(0,A+B)
plt.axis("off")

for key,value in ver_u.items():
    t1 = plt.Polygon(value, ec=None, fc=col[key])
    plt.gca().add_patch(t1)

#plt.show()
plt.savefig('foo.png')