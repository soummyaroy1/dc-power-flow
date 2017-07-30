#Import NumPy and bus and branch data
import numpy as np
bus = np.loadtxt('bus.txt', delimiter = ',', skiprows = 1, dtype = float)
branch = np.loadtxt('branch.txt', delimiter = ',', skiprows = 1, dtype = float)


n = np.shape(bus)       #Find number of buses
n = n[0]                #Find number of buses

m = np.shape(branch)    #Find number of branches
m = m[0]                #Find number of branches


p = bus[:,1,None] - bus[:,2,None]   #Solve for net power at each bus

b = np.zeros((n,n))   #Set up empty 'Y-bus' 2d array of susceptances

for v in range(m):       #For each line
    x = branch[v,0,None]    #Get 'from bus'
    y = branch[v,1,None]    #Get 'to bus'
    b[int(x-1),int(y-1)] = branch[v,2,None]     #Fill in off-diagonal values
    b[int(y-1),int(x-1)] = branch[v,2,None]     #Fill in off-diagonal values
    b[int(x-1),int(x-1)] = (b[int(x-1),int(x-1)] - branch[v,2,None])    #Fill in diagonal values
    b[int(y-1),int(y-1)] = (b[int(y-1),int(y-1)] - branch[v,2,None])    #Fill in diagonal values

p = np.delete(p,0,0)    #Delete swing bus data
p = np.asmatrix(p)      #Convert to matrix

b = np.delete(b,0,0)    #Delete swing bus data
b = np.delete(b,0,1)    #Delete swing bus data
b = np.asmatrix(b)      #Convert to matrix
b = np.linalg.inv(b)    #Invert Y-bus matrix

d = b*p                         #Solve for angles at all buses except swing
d = np.vstack((0,d))            #Add back in swing bus angle of 0

output = branch.astype(float)   #Copy branch array over to an output array

print('Solution:')
for v in range(m):           #For each line
    x = branch[v,0,None]        #Get 'from bus'
    y = branch[v,1,None]        #Get 'to bus'
    output[v,2,None] = -branch[v,2,None]*(d[int(x-1)]-d[int(y-1)])  #Save ouput
    flow = (-branch[v,2,None]*(d[int(x-1)]-d[int(y-1)]))              #Each line's power flow
    
    print('Line from Bus ' + str(int(x)) + ' to Bus ' + str(int(y)) +
          ' has a flow of: ' + str(round(float(flow),4)) + ' per Unit')  #Display solution
          
print('\nSolution as a matrix:')
print(output) #Displays solution in matrix format
