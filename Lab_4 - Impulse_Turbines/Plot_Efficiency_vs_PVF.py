# Script to plot efficiency η vs. Peripheral Velocity Factor (PVF)
# Use data obtained from files PVF_Calculator.py and Efficiency_(η)_Calculator.py
# 10 November 2024
# Ibrahim Hassan

import matplotlib.pyplot as plt

# Experimental data (PVF and Efficiency)
experimental_pvf_90 = [0.2757, 0.2570, 0.2330, 0.1996, 0.1395, 0.0868, 0.0319, 0.0000]
experimental_efficiency_90 = [0.00, 13.99, 25.38, 30.44, 31.90, 25.53, 10.43, 0.00]
experimental_pvf_160 = [0.3588, 0.3453, 0.3181, 0.2902, 0.2420, 0.2041, 0.1297, 0.0761, 0.0399, 0.000]
experimental_efficiency_160 = [0.00, 18.80, 31.18, 42.67, 51.40, 52.24, 42.39, 29.01, 16.87, 0.00]

# Theoretical data (PVF and Efficiency)
theoretical_pvf = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
theoretical_efficiency_90 = [0.00, 18.00, 32.00, 42.00, 48.00, 50.00, 48.00, 42.00, 32.00, 18.00, 0.00]
theoretical_efficiency_160 = [0.00, 34.91, 62.07, 81.47, 93.11, 96.98, 93.11, 81.47, 62.07, 34.91, 0.00]

# Plotting the data
plt.figure(figsize=(10,6))

# Experimental plot
plt.plot(experimental_pvf_90, experimental_efficiency_90, 'o-', label="Experimental (β = 90°)", color='green')

# Experimental plot
plt.plot(experimental_pvf_160, experimental_efficiency_160, 'o-', label="Experimental (β = 160°)", color='purple')

# Theoretical plot for β = 90°
plt.plot(theoretical_pvf, theoretical_efficiency_90, 'o-', label="Theoretical (β = 90°)", color='red')

# Theoretical plot for β = 160°
plt.plot(theoretical_pvf, theoretical_efficiency_160, 'o-', label="Theoretical (β = 160°)", color='blue')

# Labels and title
plt.xlabel("Peripheral Velocity Factor (PVF)", fontsize=12)
plt.ylabel("Efficiency (%)", fontsize=12)
plt.title("Efficiency vs Peripheral Velocity Factor", fontsize=14)
plt.legend()

# Show plot
plt.grid(True)
plt.show()
