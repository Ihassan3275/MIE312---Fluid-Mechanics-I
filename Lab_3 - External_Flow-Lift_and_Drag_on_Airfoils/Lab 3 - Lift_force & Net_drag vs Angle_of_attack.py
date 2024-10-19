# Script to plot Lift Force and Net Drag Force vs. Angle of Attack, with Stall angle marked -- for MIE312 - Lab 3
# 14 October 2024
# Ibrahim Hassan

import matplotlib.pyplot as plt
import numpy as np

# Data for Angle of Attack, Lift Force, and Net Drag Force
angle_of_attack = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 40, 50, 60, 70, 80, 90]
lift_force = [0, 0.13, 0.34, 0.49, 0.64, 0.78, 0.93, 0.69, 0.77, 0.89, 1.00, 1.10, 1.03, 0.93, 0.72, 0.43, 0.11]
net_drag_force = [-0.01728, 0.02272, 0.01272, 0.10272, 0.15272, 0.19272, 0.23272, 0.38272, 0.45272, 0.54272,
                  0.64272, 0.96272, 1.18272, 1.51272, 1.75272, 1.90272, 1.93272]

# Find the stall angle (the angle at which lift is maximum)
stall_index = np.argmax(lift_force)
stall_angle = angle_of_attack[stall_index]
stall_lift_force = lift_force[stall_index]

# Create the plot
plt.figure(figsize=(10,6))

# Plotting Lift Force vs Angle of Attack
plt.plot(angle_of_attack, lift_force, label='Lift Force (N)', color='blue', marker='o')

# Plotting Net Drag Force vs Angle of Attack
plt.plot(angle_of_attack, net_drag_force, label='Net Drag Force (N)', color='red', marker='s')

# Mark the stall point on the graph
plt.scatter(stall_angle, stall_lift_force, color='green', zorder=5, label=f'Stall Angle = {stall_angle}°')
plt.axvline(x=stall_angle, color='green', linestyle='--')

# Adding title and labels
plt.title('Lift Force and Net Drag Force vs. Angle of Attack with Stall Angle')
plt.xlabel('Angle of Attack (degrees)')
plt.ylabel('Force (N)')

# Adding legend
plt.legend()

# Show the plot
plt.grid(True)
plt.show()
