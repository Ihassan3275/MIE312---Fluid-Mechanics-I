# Script to calculate the Peripheral Velocity Factor (PVF) using omega
# 10 November 2024
# Ibrahim Hassan

import numpy as np

# Constants
r = 0.025  # radius in meters
Cv = 0.95  # coefficient
P = 61000  # pressure in Pa
rho = 1000  # density of water in kg/m^3

# Function to convert rpm to rad/s
def rpm_to_rad_s(rpm):
    return rpm * (2 * np.pi / 60)

# Function to calculate Vj (jet velocity)
def calculate_Vj(P, rho, Cv):
    return Cv * np.sqrt(2 * P / rho)

# Function to calculate Vb (peripheral velocity)
def calculate_Vb(omega, r):
    return omega * r

# Given data
omega_90 = np.array([1105, 1030, 934, 800, 559, 348, 128, 0])  # rpm for β = 90°
omega_160 = np.array([1438, 1384, 1275, 1163, 970, 818, 520, 305, 160, 0])  # rpm for β = 160°

# Convert ω (rpm) to rad/s
omega_90_rad_s = rpm_to_rad_s(omega_90)
omega_160_rad_s = rpm_to_rad_s(omega_160)

# Calculate Vj (jet velocity)
Vj = calculate_Vj(P, rho, Cv)

# Calculate Vb (peripheral velocity) for both β = 90° and β = 160°
Vb_90 = calculate_Vb(omega_90_rad_s, r)
Vb_160 = calculate_Vb(omega_160_rad_s, r)

# Calculate PVF (Peripheral Velocity Factor)
PVF_90 = Vb_90 / Vj
PVF_160 = Vb_160 / Vj

# Return the results
print(PVF_90)
print(PVF_160)
