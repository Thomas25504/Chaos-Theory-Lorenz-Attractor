#Importing the required libraries
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Sigma controls the speed of fluid motion
# Rho determines how chaotic the system becomes
# Beta influences how the system dissipates energy

# 
def lorenz(t, state, sigma=10, beta=8/3, rho=28):
    x, y, z = state
    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - beta * z
    return [dx, dy, dz] 

t_max = 100
t = np.linspace(0, t_max, 10000)
initial_state = [0.01, 1.0, -1.05]
sol = solve_ivp(lorenz, [0, t_max], initial_state, t_eval=t)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Extract the first element from the list returned by ax.plot
line, = ax.plot(sol.y[0], sol.y[1], sol.y[2], color='b', lw=0.5)

ax.set_axis_off()

def init():
    ax.set_xlim(-20, 20)
    ax.set_ylim(-30, 30)
    ax.set_zlim(0, 50)
    return line,

def update(frame):
    line.set_data(sol.y[0, :frame], sol.y[1, :frame])
    line.set_3d_properties(sol.y[2, :frame])
    
    # Calculate color based on frame
    color = plt.cm.viridis(frame / len(t))
    line.set_color(color)
    
    return line,

ani = FuncAnimation(fig, update, frames=range(0, len(t), 10), init_func=init, blit=True, interval=10)
plt.show()
