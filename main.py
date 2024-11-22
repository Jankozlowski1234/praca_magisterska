import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x,y = 0,0
c = "red"



n = 2  ##size of a hexagon
z = 4*n-1   ### max amount of tectangles in a row
p = 2*(2*n+1)
X = np.array([[x,y] for x in range(p+1) for y in range(2*n+1)])

if y%2==0:
    if x%2 !=0:  # czy normalnie
        pass
    else :  #czy odwrocony
        pass
else:
    if x % 2 == 0:   # czy normalnie
        pass
    else:     #czy odwrocony
        pass
plt.figure()
plt.scatter(X[:, 0], X[:, 1], s = 1)

#t1 = plt.Polygon(X[:3,:], ec = "black",fc = "red")
#plt.gca().add_patch(t1)

#t2 = plt.Polygon(X[3:6,:])
#plt.gca().add_patch(t2)

#plt.show()




### coloring
Mat = np.zeros((2*n,z))
print(Mat)
