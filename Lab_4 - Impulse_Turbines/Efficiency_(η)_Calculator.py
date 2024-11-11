# Script to calculate the efficiency η
# 10 November 2024
# Ibrahim Hassan

import numpy as np

# Given obtained from the trials
forces_90 = np.array([0, 0.5, 1.0, 1.4, 2.1, 2.7, 3.0, 2.7])  # Force in N for β=90°
forces_160 = np.array([0, 0.5, 0.9, 1.35, 1.95, 2.35, 3.00, 3.50, 3.88, 4.3])  # Force in N for β=160°
angular_velocities_90 = np.array([1105, 1030, 934, 800, 559, 348, 128, 0])  # ω in rpm for β=90°
angular_velocities_160 = np.array([1438, 1384, 1275, 1163, 970, 818, 520, 305, 160, 0])  # ω in rpm for β=160°

# Constants
r = 0.025  # radius in meters
rho = 1000  # Density of water in kg/m^3
Q = 10.5 / (1000 * 60)  # Volumetric flow rate in m^3/s
Vj = 10.493  # Jet velocity in m/s (calculated in file PVF_Calculator)

# Convert angular velocity from rpm to rad/s
omega_90_rad = angular_velocities_90 * (2 * np.pi / 60)
omega_160_rad = angular_velocities_160 * (2 * np.pi / 60)

# Calculate torque T (T = F * r)
torque_90 = forces_90 * r
torque_160 = forces_160 * r

# Calculate efficiency η = (2 * ω * T) / (ρ * Vj^2 * Q)
efficiency_90 = (2 * omega_90_rad * torque_90) / (rho * Vj**2 * Q)
efficiency_160 = (2 * omega_160_rad * torque_160) / (rho * Vj**2 * Q)

print(efficiency_90)
print(efficiency_160)

print("Percentages:")
print(efficiency_90 * 100)
print(efficiency_160 * 100)

# Debugging intermediate values
print("Angular velocity (rad/s):", omega_90_rad)
print("Torque (Nm):", torque_90)
print("Denominator (ρ * Vj^2 * Q):", rho * Vj**2 * Q)
print("Efficiency:", efficiency_90)
