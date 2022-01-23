## Here is the ftp+plot.py code from Lecutre 0
import numpy as np
from matplotlib import pyplot as plt
ftp = np.loadtxt('ftpcol.txt', dtype=int)

print(ftp[0,0])
print(ftp[1,0])
print(ftp[:,0])
print(ftp[:,1])

time_s = ftp[:,0]
speed_mph = ftp[:,1]
plt.plot(time_s,speed_mph)
plt.xlabel("Time (sec)")
plt.ylabel("Speed (mph)")
plt.show()

speed_mps = ftp[:,1]*0.44704
accel_mpsps = np.diff(speed_mps,
prepend=0)
plt.plot(time_s,accel_mpsps)
plt.xlabel("Time (sec)")
plt.ylabel("Acceleration (m/sec^2)")
plt.show()

distance_m = np.cumsum(speed_mps)
plt.plot(distance_m, speed_mps)
plt.xlabel("Distance (m)")
plt.ylabel("Velocity (m/sec)")
plt.show()