# This python script is intended for MIE312 lab 2 (part 4)
# (c) Ibrahim Hassan 2024
# October 04, 2024
# version 1.0

import numpy as np
import matplotlib.pyplot as plt

# Data from the table (Flow rate in L/hr and pressure drop in mbar)
flow_rate_lph = np.array([500, 1000, 2000, 3000, 4000, 5000])  # Flow rate in L/hr
pressure_drop_mbar = np.array([4, 12, 42, 89, 153, 228])  # ∆P_DPT in mbar

# Scale flow rate by dividing by 1000 to work in easier numbers
flow_rate_scaled = flow_rate_lph / 1000  # Now the values will be 0.5, 1.0, etc.

# Plot the data
plt.figure(figsize=(8, 6))
plt.scatter(flow_rate_lph, pressure_drop_mbar, color='blue', label='Measured data')

# Annotate each point with its coordinates
for i, (x, y) in enumerate(zip(flow_rate_lph, pressure_drop_mbar)):
    plt.annotate(f"({int(x)}, {int(y)})", (x, y), textcoords="offset points", xytext=(5,5), ha='center', fontsize=8)

# Fit a second-degree polynomial (quadratic fit) to the scaled data
coefficients = np.polyfit(flow_rate_scaled, pressure_drop_mbar, 2)
trendline = np.poly1d(coefficients)

# Generate data for the trendline (using scaled flow rate)
flow_rate_fit = np.linspace(min(flow_rate_scaled), max(flow_rate_scaled), 100)
pressure_drop_fit = trendline(flow_rate_fit)

# Plot the trendline
plt.plot(flow_rate_fit * 1000, pressure_drop_fit, color='red', label='Trendline (Quadratic fit)')

# Label the plot
plt.title('Total Head Loss (∆P_DPT) vs Flow Rate (Q)')
plt.xlabel('Flow Rate, Q (L/hr)')
plt.ylabel('Total Head Loss, ∆P_DPT (mbar)')
plt.legend()
plt.grid(True)

# Format the trendline equation for display (revert scaling in equation)
a, b, c = coefficients
equation_text = f'$∆P_{{DPT}} = {a:.4f}Q^2 + {b:.4f}Q + {c:.4f}$'
equation_text = equation_text.replace('Q', '(Q/1000)')  # Adjust Q to indicate the scaling

# Add the equation text to the plot (move to center)
plt.text(0.4 * max(flow_rate_lph), 0.6 * max(pressure_drop_mbar), equation_text, fontsize=12, color='red')

# Show the plot
plt.show()

