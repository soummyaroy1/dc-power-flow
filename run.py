import numpy as np
bus = np.loadtxt('bus.txt', delimiter = ',', skiprows = 1, dtype = float)
branch = np.loadtxt('branch.txt', delimiter = ',', skiprows = 1, dtype = float)
n = np.shape(bus)
m = np.shape(branch)
p = bus[:,1,None] - bus[:,2,None]
b = np.zeros((n[0],n[0]))
for v in range(m[0]):    
    x = branch[v,0,None]
    y = branch[v,1,None]
    b[int(x-1),int(y-1)] = branch[v,2,None]
    b[int(y-1),int(x-1)] = branch[v,2,None]
    b[int(x-1),int(x-1)] = (b[int(x-1),int(x-1)] - branch[v,2,None])
    b[int(y-1),int(y-1)] = (b[int(y-1),int(y-1)] - branch[v,2,None])

p = np.delete(p,0,0)
p = np.asmatrix(p)
b = np.delete(b,0,0)
b = np.delete(b,0,1)
b = np.asmatrix(b)
b = np.linalg.inv(b)

d = b*p
d = np.vstack((0,d))
output = branch.astype(float)
for v in range(m[0]):    
    x = branch[v,0,None]
    y = branch[v,1,None]
    output[v,2,None] = -branch[v,2,None]*(d[int(x-1)]-d[int(y-1)])
    temp = -branch[v,2,None]*(d[int(x-1)]-d[int(y-1)])
    print('Line from Bus ' + str(int(x)) + ' to Bus ' + str(int(y)) + 
          ' has a flow of: ' + str(float(temp)) + ' per Unit')
